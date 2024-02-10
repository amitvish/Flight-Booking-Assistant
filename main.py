import requests

def get_auth_token():
    auth_url = "https://aero-suite-stage4-airarabia.isaaviation.net/api/auth/authenticate"
    auth_payload = {
        "login": "admin@mail.com",
        "password": "Qwerty1!"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(auth_url, json=auth_payload, headers=headers)
    # Updated to extract accessToken from the tokenPair
    token_response = response.json()
    access_token = token_response.get('tokenPair', {}).get('accessToken')
    return access_token


def read_xml_request(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.read()

def send_soap_request(soap_request, soap_url, token):
    soap_headers = {
        'Content-Type': 'text/xml',
        'Authorization': f'Bearer {token}'
        
    }
    response = requests.post(soap_url, data=soap_request, headers=soap_headers)
    return response

# Step 1: Authenticate and get the token
token = get_auth_token()

# Step 2: Specify the SOAP endpoint URL
soap_url = 'https://aero-search-best-offer-soap-api-service-stage4-airarabia.isaaviation.net/best-offer/AirShopping/17.2/V1/'

# Step 3: Read the SOAP request from the 'request.xml' file
soap_request = read_xml_request('request.xml')

# Step 4: Send the SOAP request with the obtained token and get the response
response = send_soap_request(soap_request, soap_url, token)

# Step 5: Print the response text
print(response.text)
