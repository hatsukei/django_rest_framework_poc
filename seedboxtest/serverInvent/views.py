from serverInvent.models import ServerInvent
from serverInvent.serializers import ServerInventSerializer, UserSerializer
from rest_framework import generics, permissions
from django.contrib.auth.models import User

# Server Inventory Views
class ServerInventList(generics.ListCreateAPIView):
    queryset = ServerInvent.objects.all()
    serializer_class = ServerInventSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ServerInventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ServerInvent.objects.all()
    serializer_class = ServerInventSerializer
    permission_classes = (permissions.IsAuthenticated,)

# User Views
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
