from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['username']

class GoalStatusSerializer(serializers.ModelSerializer):
	class Meta:
		model = GoalStatus
		fields = ('visible', 'id', 'name', 'status')

class ScrumyUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = ScrumyUser
		fields = ('nickname', 'goalstatus_set')				