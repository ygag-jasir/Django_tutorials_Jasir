import logging
import json

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from youpayclient.utils import wait_redis_lock
from youpayclient.models import YouPayClientTransactionData
from youpayclient.libs.authentication import SignatureAuthentication
from youpayclient.v1.serializer import YouPayClientTransactionDataSerializers

logger = logging.getLogger(__name__)


class WebhookListener(APIView):
    """
    This class is to process the webhook data from YouPay
    """
    authentication_classes = (SignatureAuthentication,)

    def post(self, request):
        
        print("Request Meta {} \n\n: ".format(request.META))
        """
        Post method to receive the data from YouPay
        """
        
        
        request_data = json.loads(request.data)
        
        request_data =     {'payment': {'product_code': 'HPCRED', 'payment_platform': 'IOS', 'ip': '115.246.244.245', 'language': 'en', 'invoice_id': 3282, 'loyalty_level': 0, 'order_reference': 'Invoice-3282|ew|ZP84HKSZ5M'}, 'order': {'amount': '1.630', 'currency': 'AED', 'service_fee': '0', 'base_amount': '1.630', 'VAT_amount': '0'}, 'customer': {'email': 'ajmal@yougotagift.com', 'phone': '', 'name': 'Muhammed Ajmal', 'registered_since': '2022-01-07 06:15:54+00:00'}, 'order_history': [], 'order_items': [], 'urls': {'success_url': 'https://ecom-wallet-ew-300.sit.yougotagift.co/payments/api/v2/youpay/success', 'failure_url': 'https://ecom-wallet-ew-300.sit.yougotagift.co/payments/api/v2/youpay/failure', 'cancel_url': 'https://ecom-wallet-ew-300.sit.yougotagift.co/payments/api/v2/youpay/cancel', 'verify_url': 'https://ecom-wallet-ew-300.sit.yougotagift.co/payments/api/v2/youpay/verify'}, 'session_id': 'P7V158852O4FID2X'}
        
        print("headers ",type(request.headers.keys()))
        print("Type ",type(request_data))
        print("DATA ",request_data)
        invoice_id = request_data.get("invoice_id")
        transaction_id = request_data.get("transaction_id")

        try:
            logger.info("Received YouPay webhook for invoice {}".format(
                invoice_id))
            lock_name = 'lock:WebhookListener:invoice_%d' % (
                int(invoice_id),)
            with wait_redis_lock(lock_name=lock_name):
                transaction_obj = self.get_transaction_data_object(
                    request_data.get(
                        'transaction_id', None))

                request_data["vat_amount"] = request_data.get('VAT_amount')
                request_data["customer_ip_address"] = request_data.get('ip')

                if transaction_obj:
                    serializer = YouPayClientTransactionDataSerializers(
                        transaction_obj, data=request_data, partial=True)
                else:
                    serializer = YouPayClientTransactionDataSerializers(
                        data=request_data, partial=True)

                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    response_message = (
                        "youpayclient webhook listener successfully processed"
                        " for transaction id {}, invoice id {}".format(
                            transaction_id, invoice_id))
                    response_status = True
                else:
                    response_message = (
                        "youpayclient webhook listener not processed for "
                        "transaction id {}, invoice id {}".format(
                        transaction_id, invoice_id))
                    response_status = False

                response_data = {
                    'message': response_message,
                    'status': response_status}

                response_status = status.HTTP_200_OK
                logger.info(response_message)
        except Exception as e:
            logger.error(
                "youpayclient webhook failed with error {}".format(e))
            response_data = {'message': "Data not updated", 'status': False}
            response_status = status.HTTP_400_BAD_REQUEST
        return Response({'data': response_data, 'status': response_status})

    def get_transaction_data_object(self, transaction_id):
        transaction_obj = None
        if transaction_id:
            try:
                transaction_obj = (
                    YouPayClientTransactionData.objects.get(
                        transaction_id=transaction_id))
            except YouPayClientTransactionData.DoesNotExist:
                transaction_obj = None
        return transaction_obj
