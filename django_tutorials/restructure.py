from rest_framework import serializers

from core.models import Currency
from payments.constants import PURCHASE_PLATFORM_CHOICES


def currency_validator(currency):
    if not Currency.objects.filter(iso_code=currency):
        raise serializers.ValidationError("Currency is not supported")
    return currency


def amount_validator(amount):
    if amount < 0:
        raise serializers.ValidationError("Amount must be positive")
    return amount


def phone_number_validator(customer_phone):
    """
    To validate phone number with or with out + sign
    """
    if customer_phone.startswith("+"):
        customer_phone = customer_phone[1:]

    if not customer_phone.isdigit():
        raise serializers.ValidationError("customer_phone must be numeric")
    return customer_phone


def lang_validator(lang):
    """
    As per tabby documentation(05 Aug 2022) lang must be "ar" "en"
    ref : https://docs.tabby.ai/#tag/Checkout
    """
    if lang not in ["en", "ar"]:
        raise serializers.ValidationError("lang must be en or ar")
    return lang


def loyalty_level_validator(loyalty_level):
    """
    loyalty level must be numeric value  
    """
    if not loyalty_level.isdigit():
        raise serializers.ValidationError("loyalty_level must be numeric")
    return loyalty_level


class OrderItemSerializer(serializers.Serializer):
    """
    Serializer to validate order items
    """
    title = serializers.CharField(required=True)
    reference_id = serializers.CharField(required=True)


class PaymentRequestSerializer(serializers.Serializer):
    """
    Serializer for payment request data
    """
    amount = serializers.DecimalField(decimal_places=4, max_digits=12,
                                      validators=[amount_validator])
    customer_email = serializers.EmailField(required=True)
    customer_name = serializers.CharField(required=True)
    customer_phone = serializers.CharField(required=False, allow_blank=True,
                                           validators=[
                                               phone_number_validator])

    platform = serializers.ChoiceField(choices=PURCHASE_PLATFORM_CHOICES,
                                       required=True)
    language = serializers.CharField(required=True, validators=[
        lang_validator])
    currency = serializers.CharField(required=True, validators=[
        currency_validator])
    loyalty_level = serializers.CharField(required=False,
                                          validators=[loyalty_level_validator]
                                          )
    order_items = OrderItemSerializer(many=True, required=False,
                                      allow_null=True)
