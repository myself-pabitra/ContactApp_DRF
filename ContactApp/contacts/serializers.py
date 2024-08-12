from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'first_name', 'last_name',
                  'mobile', 'email', 'message']

    def validate(self, data):
        if data['first_name'] == data['last_name']:
            raise serializers.ValidationError(
                "First name and last name cannot be the same.")
        return data
