import requests

def create_request(request):
    # create sample request
    PAY_SESSION_KEY="youpay-session-id"
    session_id = "123123"
    request.session[PAY_SESSION_KEY] = session_id
    
    

