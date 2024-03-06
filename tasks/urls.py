from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskListView, SubTaskModelView

router = DefaultRouter()
router.register(r'task', TaskListView, basename='task')
router.register(r'subtask', SubTaskModelView, basename='subtask')


urlpatterns = [
    path('', include(router.urls))
]
