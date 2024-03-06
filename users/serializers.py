from rest_framework.serializers import ModelSerializer, CharField

from .models import User


class UserSerializer(ModelSerializer):
    password = CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'email', 'password', 'first_name', 'last_name', 'is_staff', 'is_superuser']

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)

        # All the created are created as regular user, then an existing superuser can give the permissions to them
        user.is_superuser = False
        user.is_superuser = False

        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super(UserSerializer, self).update(instance, validated_data)
        if validated_data.get('password'):
            user.set_password(validated_data['password'])
        user.save()
        return user
