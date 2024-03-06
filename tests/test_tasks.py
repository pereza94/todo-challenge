import pytest
from rest_framework import status
from rest_framework.test import APIClient
from freezegun import freeze_time

from tasks.models import Task, SubTask, TaskStatus
from users.models import User


@pytest.fixture
def authenticated_client():
    client = APIClient()
    user = User.objects.create_user(username="test", password="test")
    client.force_authenticate(user=user)

    return client


@pytest.mark.django_db
def test_task_cannot_be_created_without_credentials():
    """
    Check the status code response is not OK (200) if credentials are not passed
    """
    client = APIClient()
    response = client.post('/tasks/')
    assert response.status_code == 401


@freeze_time("2023-03-03 14:00:00")
@pytest.mark.django_db
def test_task_created_properly(authenticated_client):
    """
    Check the instance task are properly created
    """
    url = '/tasks/'
    payload = {
        "name": "First Task",
        "description": 'A task description',
        "owner": 1
    }
    response = authenticated_client.post(url, payload, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    assert Task.objects.count() == 1
    task = Task.objects.first()
    assert task.name == 'First Task'
    assert task.description == 'A task description'
    assert task.owner.username == 'test'
    assert task.creation_date.strftime("%Y-%m-%d %H:%M:%S") == '2023-03-03 14:00:00'
    assert task.general_task_status == "NOT_STARTED"
    assert task.subtasks_amount == 0


@freeze_time("2023-03-03 14:00:00")
@pytest.mark.django_db
def test_task_updated_properly(authenticated_client):
    """
    Check the instance task are properly updated
    """
    Task.objects.create(name="First Task", description="A task description", owner_id=1)
    task = Task.objects.get(pk=1)
    assert task.description == "A task description"

    payload = {'description': 'A new description'}
    response = authenticated_client.patch("/tasks/1/", payload, format='json')
    task = Task.objects.get(pk=1)
    assert response.status_code == status.HTTP_200_OK
    assert task.description == "A new description"


@pytest.mark.django_db
def test_task_removed_properly(authenticated_client):
    """
    Check the instance task are properly removed
    """
    Task.objects.create(name="First Task", description="A task description", owner_id=1)
    Task.objects.create(name="Second Task", description="A task description", owner_id=1)
    Task.objects.create(name="Third Task", description="A task description", owner_id=1)
    assert Task.objects.count() == 3

    response = authenticated_client.delete("/tasks/2/")
    tasks_name = sorted([task.name for task in Task.objects.all()])
    assert response.status_code == status.HTTP_204_NO_CONTENT
    assert tasks_name == ["First Task", "Third Task"]


@pytest.mark.django_db
def test_subtasks_amount_property_computed_properly():
    """
    Check the subtaks_amount property is properly computed
    """
    User.objects.create_user(username="test", password="test")
    task = Task.objects.create(name="First Task", description="A task description", owner_id=1)
    SubTask.objects.create(name="SubTask 1", description="A task", task=task, owner_id=1)
    SubTask.objects.create(name="SubTask 2", description="A task", task=task, owner_id=1)
    SubTask.objects.create(name="SubTask 3", description="A task", task=task, owner_id=1)
    task = Task.objects.first()

    assert task.subtasks_amount == 3


@pytest.mark.django_db
@pytest.mark.parametrize("subtasks, expected_result", [
    # All the subtasks are uncompleted
    (
            [
                {
                    'name': "Subtask 1",
                    "description": "A",
                    'owner_id': 1,
                    'completed': False
                },
                {
                    'name': "Subtask 2",
                    "description": "B",
                    'owner_id': 1,
                    'completed': False
                }
            ],
            TaskStatus.IN_PROGRESS.value
    ),
    # All the subtasks are completed
    (
            [
                {
                    'name': "Subtask 1",
                    "description": "A",
                    'owner_id': 1,
                    'completed': True
                },
                {
                    'name': "Subtask 2",
                    "description": "B",
                    'owner_id': 1,
                    'completed': True
                }
            ],
            TaskStatus.COMPLETED.value
    ),
    # No subtasks created
    (
            [],
            TaskStatus.NOT_STARTED.value
    ),
])
def test_task_general_status_properly(subtasks, expected_result):
    """
    Check the general_status property is properly computed
    """
    User.objects.create_user(username="test", password="test")
    task = Task.objects.create(name="First Task", description="A task description", owner_id=1)
    for subtask in subtasks:
        subtask['task'] = task
        SubTask.objects.create(**subtask)

    assert task.general_task_status == expected_result


@pytest.mark.django_db
def test_a_user_cannot_modify_task_of_another_user(client):
    User.objects.create_user(username="test", password="test", id=1)
    user_2 = User.objects.create_user(username="test2", password="test2", id=2)
    Task.objects.create(name="First Task", description="A task description", owner_id=1, id=1)

    client = APIClient()
    client.force_authenticate(user=user_2)

    response = client.patch('/tasks/1/', {"name": "new task"}, format='json')

    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_a_user_can_modify_own_tasks():
    user_1 = User.objects.create_user(username="test", password="test", id=1)
    User.objects.create_user(username="test2", password="test2", id=2)

    Task.objects.create(name="First Task", description="A task description", owner_id=1, id=1)

    client = APIClient()
    client.force_authenticate(user=user_1)

    response = client.patch('/tasks/1/', {"name": "new task"}, format="json")

    assert response.status_code == status.HTTP_200_OK
