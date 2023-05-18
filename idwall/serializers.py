from rest_framework import serializers
from .models import WantedPerson

class WantedPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = WantedPerson
        fields = '__all__'
        