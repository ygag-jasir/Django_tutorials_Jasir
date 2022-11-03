import json
import requests


AMOUNT = input("Enter amount: ")

if AMOUNT == "":
    print("ERROR : Amount is empty, defaulting to 100")
    AMOUNT = "100"


data_createsession_1 = {
    "payment": {
        "product_code": "",
        "payment_platform": "Web",
        "ip": "192.168.1.1",
        "language": "en",
        "invoice_id": "11112",
        "order_reference": "OrderRef-5555-jasir"
    },
    "order": {
        "amount": AMOUNT,
        "currency": "AED",
        "service_fee": 123,
        "base_amount": 2344,
        "VAT_amount": 13
    },
    "customer": {
        "email": "jasir+checks@yougotagift.com",
        "phone": 12324234,
        "name": "jasir-00",
        "registered_since": "26-03-1994"
    },
    "order_history": [
        {
            "purchased_at": "2019-08-24T14:15:22Z",
            "amount": AMOUNT,
            "payment_method": "card",
            "status": "new",
            "buyer": {
                "phone": "9312345678",
                "email": "jomon+sand@yougotagift.com",
                "name": "jomon"
            },
            "items": [
                {
                    "title": "t22",
                    "category": "t2222"
                },
                {
                    "title": "t23",
                    "category": "t2333"
                }
            ]
        }
    ],
    "order_items": [
        {
            "title": "Centrepoint",
            "category": "Gift Card",
            "reference_id": "11509661"
        }
    ],
    "urls": {
        "success_url": "https://example.com/test-success",
        "failure_url": "https://example.com/test-failure",
        "cancel_url": "https://example.com/test-cancel",
        "verify_url": "http://localhost:8000/services/api/v1/test-payment/"
    },
    "session_id": "123123"
}


# URLs
URL_LOCAL = "http://localhost:8000/"
URL_QA = "https://youpay-ygp-1.sit.yougotagift.co/" # QA
URL_SANDBOX = "https://app.youpay.sandbox.yougotagift.com/" # Sandbox
URL_PRODUCTION = "" # Production

# API Key
API_KEY_LOCAL = "9qKHiHmonor7YxvKnSvvqNyaNEZwGkIPlV71_xM10nM"
API_KEY_QA = "3zqREqrRZOIA0DjwKROW8uG8OOJBu0gNn33r3Egiw-8"
API_KEY_SANDBOX = "FfsZ21AKMiGSW2AaKIs00nClpyJBVgoDMgj-3Oy7nYk"
API_KEY_PRODUCTION = ""

# Test Environment
env_choice = ["1", "2", "3", "4"]
env = input("Enter the environment you want to test \n1.local \n2.qa \n3.sandbox \n4.production \n > ")

if env not in env_choice:
    print("Invalid environment choice. Exiting...")
    exit()

if env == "1": url=URL_LOCAL; API_KEY=API_KEY_LOCAL
elif env == "2": url=URL_QA; API_KEY=API_KEY_QA
elif env == "3": url=URL_SANDBOX; API_KEY=API_KEY_SANDBOX
elif env == "4": url=URL_PRODUCTION; API_KEY=API_KEY_PRODUCTION

print("Automated Flow check:")
print("INFO : Your environment is {}".format(env))
print("INFO : Your URL is {}".format(url))
print("INFO : Your API Key is {}".format(API_KEY))

# Create Session API 

headers = {
    "Content-Type": "application/json",
    "x-api-key": API_KEY,
}

encrypt_payload = json.dumps(data_createsession_1)
encrypt_payload_path = 'services/api/v1/test-payment/'

request_url = URL_LOCAL + encrypt_payload_path
print("INFO : Request URL is {}".format(request_url))
response = requests.post(request_url, data=encrypt_payload, headers=headers)
print("INFO : Encrypt API response is {}".format(response))
response_data = response.json()
print("INFO : Response status code is {}".format(response.status_code))
print("INFO : Response data is \n {}".format( json.dumps(response_data, indent = 4) ))

encrypted_data = response_data['response']

create_transaction_path = "services/api/v1/payment/"

request_url = url + create_transaction_path

response = requests.post(request_url, data=json.dumps(encrypted_data), headers=headers)
print("INFO : Create Transaction API response is {}".format(response.text))
response_data = response.json()
print("INFO : Response status code is {}".format(response.status_code))
print("INFO : Response data is \n {}".format( json.dumps(response_data, indent = 4) ))

redirect_url = response_data['url']

print("INFO : Redirect URL is {}".format(redirect_url))

#take transactionid from redirect url 
transaction_id = redirect_url.split("/")[-1]

print("INFO : Transaction ID is \n{}".format(transaction_id))

#call config API --todo

#saved card payment
saved_card_payment_payload = {
    "transaction_id":transaction_id,
    "token":"src_yuav57gh7r7e5elzraijbfwxbm",
    "customer_name":"Jasir-local",
    "cvv":100
}

request_url = url + "services/api/v1/checkout/saved-card/"

response = requests.post(request_url, data=json.dumps(saved_card_payment_payload), headers=headers)
print("INFO : Saved Card API response is {}".format(response))
response_data = response.json()
print("INFO : Response status code is {}".format(response.status_code))
print("INFO : Response data is \n {}".format( json.dumps(response_data, indent = 4) ))

print("INFO : Copy this url and paste it on browser \n\n{}\n\n".format(response_data['redirect_url']))

print("take the params from url and paste it here")

params_to_verify = input("Enter the params from url \n or to exit type q> ")

#convert params_to_verify to lowercase

if  params_to_verify.lower() == "q":
    print("Exiting...")
    exit()
    
verify_payment_path = "services/api/v1/checkout/verify/?"+params_to_verify

request_url = url + verify_payment_path

print("INFO : Request URL is {}".format(request_url))

response = requests.get(request_url, data={}, headers={})
print("INFO : Verify API response is {}".format(response))
response_data = response.json()
print("INFO : Response status code is {}".format(response.status_code))
print("INFO : \n {} : Response data is for amount {} \n {}".format(response_data['transaction_message']["response_summary"],AMOUNT, json.dumps(response_data, indent = 4) ))

