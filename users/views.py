from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response

from .serializers import UserSerializer
from .permissions import UserPermission
from .models import User


class UserViewSet(ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all().order_by("-date_joined")
    permission_classes = [UserPermission, ]

    def update(self, request, *args, **kwargs):
        is_risky_change = ('is_superuser' in request.data or 'is_staff' in request.data)
        if is_risky_change and not request.user.is_superuser:
            return Response(
                "Fields  'is_superuser' and 'is_staff' are "
                "only modificable for superusers.",
                status=status.HTTP_403_FORBIDDEN
            )
        return super().update(request, *args, **kwargs)
