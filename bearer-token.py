
from urllib.parse import quote
import base64
import requests
consumer_key='9DylZjpQIUOuRDVev7BRlShUS'
consumer_secret='WvDaTcYz3c70xgsadKBdi9BrfjpQEiymiOrPsg2KNVnZppnQo6'
access_token='1063915931066261504-FwDnh5XsrB0Hb0dVzsbfW0omgyMrKS'
access_token_secret='BrNAzfPwQGzb1rAuJCBC2EiC6HvFEXpVFBh9AZEWrpoTy'

def get_bearer_token(consumer_key, consumer_secret):
    
    OAUTH2_TOKEN= 'https://api.twitter.com/oauth2/token'
    
    consumer_key = quote(consumer_key)
    consumer_secret = quote(consumer_secret)
    bearer_token = consumer_key+ ":"+ consumer_secret
    encoded_bearer_token = base64.b64encode(bearer_token.encode('utf-8'))

    headers = {
        "Authorization": "Basic " + encoded_bearer_token.decode('utf-8') + "",
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8",
        "Content-Length": "29"}

    response = requests.post(OAUTH2_TOKEN, headers=headers, data={"grant_type":"client_credentials"})
    response_json = response.json()

    return(response_json["access_token"])
    
get_bearer_token(consumer_key,consumer_secret)

def send_req_with_bearer_token()