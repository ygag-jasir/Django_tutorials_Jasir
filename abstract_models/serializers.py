from .models import Base
from rest_framework import serializers

class BaseSerializers(serializers.ModelSerializer):
    """
    Base class for all serializers
    """
    class Meta:
        model = Base
        fields = '__all__'
        read_only_fields = ('created_at', 'updated_at')
        extra_kwargs = {
            'name': {'required': True},
        }