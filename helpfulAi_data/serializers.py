from rest_framework import serializers
from .models import userDat
from .models import Person

class MessSerializer(serializers.ModelSerializer):
    class Meta:
        model = userDat
        fields = ('user_name', 'message',)

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person # this is the model that is being serialized
        fields = ('username', "password",)