from rest_framework import serializers
from ..models.permissionModel import Permission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'name', 'description']
        read_only_fields = ['id']
