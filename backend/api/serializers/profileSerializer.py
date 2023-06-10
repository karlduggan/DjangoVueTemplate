from rest_framework import serializers
from ..models.profileModel import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'avatar']
        read_only_fields = ['id']