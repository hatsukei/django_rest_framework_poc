from rest_framework import serializers
from serverInvent.models import ServerInvent
from django.contrib.auth.models import User

# Serializer for Server Inventory
class ServerInventSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ServerInvent
        fields = ('id', 'server_name', 'domain_name', 'ip_address',
                'location', 'operating_system', 'status', 'owner')

# Serializer for Users 
class UserSerializer(serializers.HyperlinkedModelSerializer):
    serverinvent = serializers.HyperlinkedRelatedField(many=True, view_name='serverinvent-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'serverinvent')