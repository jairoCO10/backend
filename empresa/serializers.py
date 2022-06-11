
# todo/serializers.py

from rest_framework import serializers
from .models import datos_empresas
      
class TodoSerializer(serializers.ModelSerializer):
  class Meta:
    model = datos_empresas
    fields = ('__all__')