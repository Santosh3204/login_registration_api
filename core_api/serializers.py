from rest_framework import serializers


from django.contrib.auth.models import User
from django.db import models

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'username',
            'password',
            'first_name',
            'last_name',
            

        )
        User.username= User.email
