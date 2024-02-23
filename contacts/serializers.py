from rest_framework import serializers
from .models import PersonContact


class PersonContactSerializer(serializers.ModelSerializer):
    #url = serializers.HyperlinkedRelatedField(view_name='contacts:personcontact-detail')
    
    class Meta:
        model = PersonContact
        fields = ['id', 'first_name', 'last_name', 'phone_number','email', 'date_of_birth']