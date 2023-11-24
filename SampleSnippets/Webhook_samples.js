Approved = {
    "id": 46538,
    "created_on": "2023-10-12T11:20:56.458209+04:00",
    "modified_on": "2023-10-12T13:22:12.368803+04:00",
    "order_reference": "1697095229-pmZ560nX",
    "amount": "56.5600",
    "currency": "AED",
    "customer_name": "Anandhu S",
    "customer_email": "anandhu.s+5054@yougotagift.com",
    "customer_ip_address": null,
    "idempotency_key": "1f735e70-8776-4c56-88bf-2a45ffa15e0a",
    "payment_reference": "Gift-1697095229-pmZ560nX|X9AXE3OFR8",
    "request_source": null,
    "api_request_data": {
        "3ds": {
            "enabled": true,
            "attempt_n3d": true
        },
        "amount": 5656,
        "source": {
            "type": "token",
            "token": null
        },
        "capture": true,
        "currency": "AED",
        "customer": {
            "name": null,
            "email": "anandhu.s+5054@yougotagift.com"
        },
        "metadata": {
            "udf1": null,
            "is_save_user_token": false
        },
        "reference": "Gift-1697095229-pmZ560nX|X9AXE3OFR8",
        "payment_ip": "115.246.244.245",
        "failure_url": "https://youpay.sandbox.yougotagift.com/en/payment-response/?id=gAAAAABlJ55WM8IY6StUYSTyjk9ubYgvUPfrBWGLpPDeMu33LqxmKO6zoh6K5dmjCiTrfYvhhX_yEsHpFbzxiZ_fVX_sDwYHfLstCkp5XEv_oLRZcovN9zAWW7WD2qCrpcZ-StSqL-lT&gty=PAYMTCPG",
        "success_url": "https://youpay.sandbox.yougotagift.com/en/payment-response/?id=gAAAAABlJ55WM8IY6StUYSTyjk9ubYgvUPfrBWGLpPDeMu33LqxmKO6zoh6K5dmjCiTrfYvhhX_yEsHpFbzxiZ_fVX_sDwYHfLstCkp5XEv_oLRZcovN9zAWW7WD2qCrpcZ-StSqL-lT&gty=PAYMTCPG"
    },
    "api_response_data": {
        "applepay": "dummy data"
    },
    "is_notification": false,
    "approved": true,
    "status": "Authorized",
    "auth_code": "124203",
    "response_summary": "Approved",
    "is_fraud": false,
    "is_flagged": false,
    "card_bin": "520424",
    "card_last4": "1454",
    "payment_method": "applepay",
    "payment_scheme": "Mastercard",
    "refunded_amount": null,
    "is_gcc_card": false,
    "card_issuer_country": null,
    "is_report_generated": false,
    "response_code": "10000",
    "error": null,
    "client": 77,
    "payment_channel": 49,
    "checkout_response_code": "10000",
    "payment_id": "pay_dq4njujikloejhsl3jobmhiu5q",
    "financial_action_response_data": null
}

pending = {
    "id": 46549,
    "created_on": "2023-10-12T13:18:15.528008+04:00",
    "modified_on": "2023-10-12T13:18:16.698586+04:00",
    "order_reference": "Invoice-7091|egg|22OG5YD9DD",
    "amount": "3078.7500",
    "currency": "AED",
    "customer_name": "Arun S Vatsan",
    "customer_email": "aruns+wick@yougotagift.com",
    "customer_ip_address": null,
    "idempotency_key": "6c2b7104-e1ce-4586-a1da-d100200c4467",
    "payment_reference": "Gift-Invoice-7091|egg|22OG5YD9DD|CWGZ2Y0ZZ8",
    "request_source": null,
    "api_request_data": {
        "3ds": {
            "enabled": true,
            "attempt_n3d": true
        },
        "amount": 307875,
        "source": {
            "id": "src_63olmpciw4su3l4x4ihgkxlnfy",
            "cvv": "100",
            "type": "id"
        },
        "capture": true,
        "currency": "AED",
        "customer": {
            "name": "",
            "email": "aruns+wick@yougotagift.com"
        },
        "metadata": {
            "udf1": null,
            "is_save_user_token": false
        },
        "reference": "Gift-Invoice-7091|egg|22OG5YD9DD|CWGZ2Y0ZZ8",
        "payment_ip": "152.58.219.39",
        "failure_url": "https://youpay.sandbox.yougotagift.com/en/payment-response/?id=gAAAAABlJ7nVeKV5G-g3eht5gYO0_pNZh9XSnZLG_6H0YPy2fBMogI9MTsJzVFLMfUKRJUPTT3DPG_kBq8Lg4ijAXVz4ewMvygFCHF9I_Do23oIyb8CkKiP5Tr7jA4UZQQGEhUBP43Uf&gty=PAYMTCPG&platform=app",
        "success_url": "https://youpay.sandbox.yougotagift.com/en/payment-response/?id=gAAAAABlJ7nVeKV5G-g3eht5gYO0_pNZh9XSnZLG_6H0YPy2fBMogI9MTsJzVFLMfUKRJUPTT3DPG_kBq8Lg4ijAXVz4ewMvygFCHF9I_Do23oIyb8CkKiP5Tr7jA4UZQQGEhUBP43Uf&gty=PAYMTCPG&platform=app"
    },
    "api_response_data": {
        "id": "pay_hsnjidgwn7ce3f34wkubs6ssei",
        "3ds": {
            "enrolled": "Y",
            "downgraded": false
        },
        "_links": {
            "self": {
                "href": "https://api.sandbox.checkout.com/payments/pay_hsnjidgwn7ce3f34wkubs6ssei"
            },
            "actions": {
                "href": "https://api.sandbox.checkout.com/payments/pay_hsnjidgwn7ce3f34wkubs6ssei/actions"
            },
            "redirect": {
                "href": "https://api.sandbox.checkout.com/sessions-interceptor/sid_mvm55igzvzxubnmk56zvaxitjy"
            }
        },
        "status": "Pending",
        "customer": {
            "id": "cus_lve5crat3vwebhiveyqu4673zq",
            "name": "Agsh",
            "email": "aruns+wick@yougotagift.com"
        },
        "reference": "Gift-Invoice-7091|egg|22OG5YD9DD|CWGZ2Y0ZZ8"
    },
    "is_notification": false,
    "approved": false,
    "status": "Pending",
    "auth_code": null,
    "response_summary": null,
    "is_fraud": false,
    "is_flagged": false,
    "card_bin": null,
    "card_last4": null,
    "payment_method": "savedcard",
    "payment_scheme": "null",
    "refunded_amount": null,
    "is_gcc_card": false,
    "card_issuer_country": null,
    "is_report_generated": false,
    "response_code": null,
    "error": null,
    "client": 77,
    "payment_channel": 49,
    "checkout_response_code": null,
    "payment_id": "pay_hsnjidgwn7ce3f34wkubs6ssei",
    "financial_action_response_data": null
}