"""Extracting token_name from html response"""

from bs4 import BeautifulSoup
import re

html_response = {
    "data": "\n\n<!DOCTYPE html>\n<html>\n<!-- Return for case of Http Method is Post -->\n<head>\n\t<script src=\"https://sbcdn.payfort.com/monitoring/js/cloudwatch-rum-sb.js\"></script>\n<title>Return URL</title>\n<meta http-equiv=\"Content-Type\" content=\"text/html; charset=UTF-8\">\n<script\n\tsrc=\"/FortAPI/resources/scripts/jquery/jquery-2.1.4.min.js\"></script>\n<script\n\tsrc=\"/FortAPI/resources/scripts/fortscripts/returnUrl.js\"></script>\n<script type=\"text/javascript\">\n\tvar returnUrlParams = {\"response_code\":\"18000\",\"card_number\":\"455701******8902\",\"card_holder_name\":\"youpaysample\",\"signature\":\"ed31eab7ad1f209f4cf0b45393226c6fd63eb62c781f90fcf7eac39fca422586\",\"merchant_identifier\":\"4b25f279\",\"expiry_date\":\"2505\",\"access_code\":\"Bz3HTCcHYeOsQkVmIvyS\",\"language\":\"en\",\"service_command\":\"TOKENIZATION\",\"response_message\":\"Success\",\"merchant_reference\":\"OrderRef-2095-sample\",\"token_name\":\"0630cebcc3af4bb2be1889d94215b302\",\"card_bin\":\"455701\",\"status\":\"18\"};\n</script>\n</head>\n<body>\n\t<form method=\"POST\" action=\"https://example.com\" id=\"returnUrlForm\"\n\t\tname=\"returnUrlForm\"></form>\n</body>\n</html>",
    "status": 200,
    "message": "API request completed successfully",
    "code": 1000
}

html_data = html_response.get("data")

soup = BeautifulSoup(html_data, 'html.parser')

script_tags = soup.find_all('script')

token_name_value = None
for idx, script_tag in enumerate(script_tags, start=1):
    if script_tag.string:
        token_name_match = re.search(
            r'"token_name"\s*:\s*"([^"]+)"', script_tag.string)
        if token_name_match:
            token_name_value = token_name_match.group(1)

print(token_name_value)
