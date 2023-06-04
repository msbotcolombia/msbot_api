from rest_framework import serializers
from django.contrib.auth import get_user_model


class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password', 'job_title', 'role', 'phone_number', 'genre', 'suffix')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = get_user_model().objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            job_title=validated_data['job_title'],
            role=validated_data['role'],
            phone_number=validated_data['phone_number'],
            genre=validated_data['genre'],
            suffix=validated_data['suffix']
        )
        return user
