from wsgiref.validate import validator

from pkg_resources import require
from .models import Base, ModelA
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

def validate_level(value):
    if value < 0:
        raise serializers.ValidationError("Level must be greater than 0")
    return value
class ModelASerializers(BaseSerializers):
    """
    Model A serializer
    """
    name = serializers.CharField(max_length=255,required=True)
    level = serializers.IntegerField(required=True,validators=[validate_level])
    class Meta:
        model = ModelA
        fields = '__all__'
        
    # class Meta(BaseSerializers.Meta):
    #     model = ModelA
    #     fields = '__all__'
    #     extra_kwargs = {
    #         'level': {'required': True},
    #     }