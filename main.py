import requests
from extract_code import extract_travel_details

# user_input = input("Please describe your travel plans: ")

def get_auth_token():
    auth_url = "https://aero-suite-stage4-airarabia.isaaviation.net/api/auth/authenticate"
    auth_payload = {
        "login": "admin@mail.com",
        "password": "Qwerty1!"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(auth_url, json=auth_payload, headers=headers)
    token_response = response.json()
    access_token = token_response.get('tokenPair', {}).get('accessToken')
    return access_token


def generate_soap_request(journey_type, departure, arrival, departure_date, return_date):
    # Dynamically generate the SOAP request
    # Adjust this template as needed to fit your actual SOAP request format
    soap_request = f"""
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:get="http://www.iata.org/IATA/EDIST/2017.2">
    <soapenv:Header/>
    <soapenv:Body>
        <AirShoppingRQ Version="17.2" PrimaryLangID="EN" AltLangID="EN" xmlns="http://www.iata.org/IATA/EDIST/2017.2">
            <CoreQuery>
                <OriginDestinations>
                    <OriginDestination>
                        <Departure>
                            <AirportCode>{departure}</AirportCode>
                            <Date>{departure_date}</Date>
                        </Departure>
                        <Arrival>
                            <AirportCode>{arrival}</AirportCode>
                        </Arrival>
                        <CalendarDates DaysBefore="0" DaysAfter="0"/>
                    </OriginDestination>
                    {'' if journey_type == 'one-way' else f'''
                    <OriginDestination>
                        <Departure>
                            <AirportCode>{arrival}</AirportCode>
                            <Date>{return_date}</Date>
                        </Departure>
                        <Arrival>
                            <AirportCode>{departure}</AirportCode>
                        </Arrival>
                        <CalendarDates DaysBefore="0" DaysAfter="0"/>
                    </OriginDestination>'''}
                </OriginDestinations>
            </CoreQuery>
        </AirShoppingRQ>
    </soapenv:Body>
</soapenv:Envelope>
    """
    return soap_request.strip()

def send_soap_request(soap_request, soap_url, token):
    soap_headers = {
        'Content-Type': 'text/xml',
        'Authorization': f'Bearer {token}'
    }
    response = requests.post(soap_url, data=soap_request, headers=soap_headers)
    return response


def get_travel_plan_details(user_input):
# Main execution starts here
    token = get_auth_token()

    extracted_details = extract_travel_details(user_input)

    journey_type = 'one-way' if extracted_details.get('return_date') is None else 'round-trip'
    departure_code = extracted_details['departure_code']
    arrival_code = extracted_details['arrival_code']
    departure_date = extracted_details['departure_date']
    return_date = extracted_details.get('return_date')  # This may be None for one-way trips


    soap_request = generate_soap_request(journey_type, departure_code, arrival_code, departure_date, return_date)

    soap_url = 'https://aero-search-best-offer-soap-api-service-stage4-airarabia.isaaviation.net/best-offer/AirShopping/17.2/V1/'

    print("SOAP Request Body:", soap_request)

    response = send_soap_request(soap_request, soap_url, token)

    # Output the response for further handling or debugging
    print("Response Status Code:", response.status_code)
    print("Response Body:", response.text)

    return response.text  # Return the SOAP response text for further processing
