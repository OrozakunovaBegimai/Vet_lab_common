from .models import Contacts
from rest_framework import serializers


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields = ['phone_number', 'address', 'email']