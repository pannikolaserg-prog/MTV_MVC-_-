from rest_framework import serializers
from apps.diary.models import DiaryEntry
from apps.users.models import User

class DiaryEntrySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = DiaryEntry
        fields = ['id', 'user', 'title', 'content', 'tags', 'is_public', 'created_at', 'updated_at']
        read_only_fields = ['user', 'created_at', 'updated_at']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']
