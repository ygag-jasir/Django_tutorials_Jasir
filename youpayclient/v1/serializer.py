from rest_framework import serializers

from youpayclient.models import YouPayClientTransactionData


class YouPayClientTransactionDataSerializers(serializers.ModelSerializer):
    class Meta:
        model = YouPayClientTransactionData
        fields = "__all__"
        read_only_fields = ('created_on', 'modified_on')
