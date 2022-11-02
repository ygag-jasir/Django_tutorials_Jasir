import json
import pprint
import requests

data_createsession_1 = {
    "amount": 5149.52,
    "currency": "SAR",
    "language": "en",
    "platform": "IOS",
    "invoice_id": 487,
    "order_items": [
        {
            "title": "YouGotaGift Teacher's Card",
            "category": "Gift Card",
            "reference_id": "1005"
        }
    ],
    "customer_name": "",
    "loyalty_level": 0,
    "order_history": [
        {
            "buyer": {
                "name": "JASIR AUTOMATIC TEST",
                "email": "jasirTest@gmail.com",
                "phone": ""
            },
            "items": [
                {
                    "title": "YouGotaGift Teacher's Card",
                    "category": "Gift Card",
                    "reference_id": "1002"
                }
            ],
            "amount": 5137.0,
            "status": "new",
            "purchased_at": "2022-07-29T06:08:52Z",
            "payment_method": "Visa"
        },
        {
            "buyer": {
                "name": "JASIR AUTOMATIC TEST",
                "email": "jas@gmail.com",
                "phone": ""
            },
            "items": [
                {
                    "title": "YouGotaGift Teacher's Card",
                    "category": "Gift Card",
                    "reference_id": "968"
                }
            ],
            "amount": 2058.0,
            "status": "new",
            "purchased_at": "2022-07-28T09:00:12Z",
            "payment_method": "Visa"
        }
    ],
    "customer_email": "emilygagtest1@gmail.com",
    "customer_phone": "918660892844",
    "order_reference": "JasirAutoTest-487|ygag|S3W4GRFFCK",
    "registered_since": "2020-06-03T14:05:34Z",
    "payment_reference": "Gift-Invoice-487|ygag|S3W4GRFFCK|WODP1RUPB6",
    "customer_ip_address": "103.119.255.239",
    "success_url": "https://your-store/success",
    "failure_url": "https://your-store/success",
    "cancel": "https://your-store/cancel"
}

data_createsession_2 = {
  "invoice_id": "1234",
  "amount": 10,
  "currency": "AED",
  "customer_phone": "500000001",
  "customer_email": "otp.success@tabby.ai",
  "customer_name": "JASIR AUTOMATIC TEST",
  "order_reference": "JasirAutoTest-1227",
  "order_items": [
    {
      "title": "t1",
      "reference_id": "t1r1"
    },
    {
      "title": "t2",
      "reference_id": "t2r1"
    }
  ],
  "customer_ip_address": "192.168.1.25",
  "platform": "Android",
  "registered_since": "2019-08-24T14:15:22Z",
  "loyalty_level": 0,
  "order_history": [
    {
      "purchased_at": "2019-08-24T14:15:22Z",
      "amount": "0.00",
      "payment_method": "card",
      "status": "new",
      "buyer": {
        "phone": "500000001",
        "email": "otp.success@tabby.ai",
        "name": "JASIR AUTOMATIC TEST"
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
  "language": "en",
  "success_url": "https://your-store/success",
  "failure_url": "https://your-store/success",
  "cancel": "https://your-store/cancel"
}


# URLs
URL_LOCAL = "http://localhost:8000/"
URL_QA = "https://tabbypg-tab-12.qa.yougotagift.co/" # QA
URL_SANDBOX = "https://tabbypg-sandbox.yougotagift.com/" # Sandbox
URL_PRODUCTION = "https://tabbypg-sandbox.yougotagift.com/" # Production

# API Key
API_KEY_LOCAL = "honXEBeHd4xIN-02LiUBAxukxUooKzcar0FIQ9e81bs"
API_KEY_QA = "VYLmLeg4FIaXQQOcxLQCoJO1Jf1X4FDJeYz56ftZHBk"
API_KEY_SANDBOX = "VYLmLeg4FIaXQQOcxLQCoJO1Jf1X4FDJeYz56ftZHBk"
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
    "Api-key": API_KEY,
}

create_session_path = 'gateway/api/v1/payment/'

response = requests.post(url+create_session_path, data=json.dumps(data_createsession_2), headers=headers)
response_data = response.json()
print("INFO : Response status code is {}".format(response.status_code))
print("INFO : Response data is \n {}".format( json.dumps(response_data, indent = 4) ))


if response_data['installments_url']:
    product_url = response_data['installments_url']
elif response_data['monthly_billing_url']:
    product_url = response_data['monthly_billing_url']
elif response_data['credit_card_installments_url']:
    product_url = response_data['credit_card_installments_url']
else:
    product_url = ""

payment_ref_no = response_data['payment_ref_no']

if product_url:
    print("Copy the url and paste it in the browser for payment processing \n > ")
    print("INFO : Product url is : {}".format(product_url))
    otp = input("\nPress any key to continue...")

print("INFO : Session created successfully")

status_choices = ["1", "2", ]
while True:
    status = input("Enter the status you want to test \n1.authorized \n2.expired  \n > ")        
    if status not in status_choices:
        key = input("Invalid status choice. Please choose again... or press q to quit")
        if key == "q":
            exit()
        else:
            continue
    else:
        break


data_webhook = {
    "id": "1cc985d1-cbbe-43d9-956f-3948a3038652",
    "meta": {
        "payment_reference": payment_ref_no,
        "client_payment_request_id": 43935
    },
    "buyer": {
        "dob": "",
        "name": "JASIR AUTOMATIC TEST",
        "email": "jasirtest@gmail.com",
        "phone": "5000000001",
    },
    "order": {
        "items": [
            {
                "title": "Careem",
                "category": "EGiftCard",
                "quantity": 0,
                "image_url": "",
                "size_type": "",
                "unit_price": "0",
                "description": "",
                "product_url": "",
                "reference_id": "11206996"
            }
        ],
        "tax_amount": "0",
        "updated_at": "0001-01-01T00:00:00Z",
        "reference_id": "Invoice-1025780|ygag|PWC8UD6L4D",
        "discount_amount": "0",
        "shipping_amount": "0"
    },
    "amount": "50.00",
    "status": status,
    "is_test": False,
    "product": {
        "type": "installments",
        "installment_period": "P1M",
        "installments_count": 2
    },
    "refunds": "",
    "captures": [
        {
            "id": "8a6bf0fe-c2d1-41fb-9c3b-7fb130fb6aa1",
            "items": [],
            "amount": "50",
            "created_at": "2022-08-09T13:17:38Z",
            "tax_amount": "0",
            "discount_amount": "0",
            "shipping_amount": "0"
        }
    ],
    "currency": "SAR",
    "closed_at": "",
    "cancelable": False,
    "created_at": "2022-08-09T13:16:11Z",
    "expires_at": "2023-08-09T13:17:30Z",
    "is_expired": False,
    "customer_id": "ae5164c3-50bd-4693-b533-39762220484c",
    "description": "",
    "merchant_id": "m_39b5c619-eac5-465d-b592-e98b3db6115b",
    "buyer_history": {
        "loyalty_level": 0,
        "wishlist_count": 0,
        "registered_since": "2022-07-14T01:10:26Z",
        "is_email_verified": "",
        "is_phone_number_verified": "",
        "is_social_networks_connected": ""
    },
    "order_history": [
        {
            "buyer": {
                "dob": "",
                "name": "JASIR AUTOMATIC TEST",
                "email": "jasirtest@gmail.com",
                "phone": "5000000001",
            },
            "items": [
                {
                    "title": "Careem",
                    "ordered": 0,
                    "shipped": 0,
                    "captured": 0,
                    "category": "Gift Card",
                    "quantity": 0,
                    "refunded": 0,
                    "image_url": "",
                    "size_type": "",
                    "unit_price": "0",
                    "description": "",
                    "product_url": "",
                    "reference_id": ""
                }
            ],
            "amount": "50",
            "status": "new",
            "purchased_at": "2022-08-08T13:28:43Z",
            "payment_method": "Tabby Pay",
            "shipping_address": {
                "zip": "",
                "city": "",
                "address": ""
            }
        }
    ],
    "shipping_address": {
        "zip": "",
        "city": "",
        "address": ""
    }
}

print("INFO : Webhook Worked ")

# path for webhook
webhook_path = "tpg/api/v1/webhooks/receiver/"

webhook_response = requests.post(url+webhook_path, data=json.dumps(data_webhook), headers=headers)
webhook_response_data = webhook_response.json()
print("INFO : Webhook response is \n {}".format( json.dumps(webhook_response_data, indent = 4) ))

print("INFO : Webhook Status updated to {}".format(status))

# verify payment
verify_payment_path = "gateway/api/v1/payment/verify/?payment_id="

payment_id = input("Enter the payment id you want to verify \n > ")

verify_payment_response = requests.get(url+verify_payment_path+payment_id, headers={})
verify_payment_response_data = verify_payment_response.json()
print("INFO : Verify payment response is \n {}".format( json.dumps(verify_payment_response_data, indent = 4) ))
print("INFO : Payment verified successfully")
