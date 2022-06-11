
# todo/views.py

from django.shortcuts import render
from rest_framework import viewsets          # add this
from .serializers import TodoSerializer      # add this
from .models import datos_empresas                    # add this
        
class empresaView(viewsets.ModelViewSet):       # add this
  serializer_class = TodoSerializer          # add this
  queryset = datos_empresas.objects.all()              # add this