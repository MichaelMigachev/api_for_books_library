from rest_framework.serializers import ModelSerializer

from users.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = "__all__"
        # fields = ['id', 'email', "phone", "is_superuser", "is_staff", "is_active", "user_permissions", 'groups']
        exclude = ['password']
