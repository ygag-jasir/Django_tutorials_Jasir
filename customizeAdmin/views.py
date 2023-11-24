from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import HttpResponse

# Create your views here.
class QitafResponseSimulator(APIView):
    def post(self, request):
        # return xml response like below


        if request.data.get('type')=='success':
            respponse_xml = """<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
                    <s:Body>
                    <GenerateOTPResponse xmlns="http://tempuri.org/">
                    <GenerateOTPResult
                    xmlns:a="http://schemas.datacontract.org/2004/07/Redemption.LiteIntegration.Service.Interface
                    " xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
                    <a:ResponseCode>0</a:ResponseCode>
                    <a:ResponseText>Success</a:ResponseText>
                    </GenerateOTPResult>
                    </GenerateOTPResponse>
                    </s:Body>
                    </s:Envelope>"""
        elif request.data.get('type')=='failure':
            respponse_xml="""<s:Envelope xmlns:s="http://schemas.xmlsoap.org/soap/envelope/">
<s:Body><GenerateOTPResponse xmlns="http://tempuri.org/">
<GenerateOTPResult xmlns:a="http://schemas.datacontract.org/2004/07/Redemption.Lite.Integration.Service.Interface" xmlns:i="http://www.w3.org/2001/XMLSchema-instance">
<a:ResponseCode>1019</a:ResponseCode><a:ResponseText>
QitafNot Found Or Available</a:ResponseText>
</GenerateOTPResult></GenerateOTPResponse></s:Body></s:Envelope>"""
        else:
            respponse_xml = {"error": "invalid type"}
            return Response(respponse_xml, status=status.HTTP_200_OK)
        
        return HttpResponse(respponse_xml, content_type='application/xml')