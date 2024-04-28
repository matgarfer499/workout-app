from rest_framework import viewsets
from .serializer import UserSerializer
from .models import *

# Create your views here.
class UserAuthorization(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()