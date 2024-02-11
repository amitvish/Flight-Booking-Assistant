import xml.etree.ElementTree as ET

def parse_flight_details_from_soap_response(soap_response):
    root = ET.fromstring(soap_response)
    
    flight_details = {}
    
    # Define namespace mapping
    ns = {'ns2': 'http://www.iata.org/IATA/EDIST/2017.2'}
    
    # Extracting flight details
    for offer in root.findall('.//ns2:Offer', ns):
        for offer_item in offer.findall('.//ns2:OfferItem', ns):
            passenger_refs = offer_item.find('.//ns2:PassengerRefs', ns).text
            price = offer_item.find('.//ns2:Price/ns2:BaseAmount', ns).text
            flight_segment_ref = offer_item.find('.//ns2:FareComponent/ns2:SegmentRefs', ns).text
            
            flight_segment = root.find(f'.//ns2:FlightSegment[@SegmentKey="{flight_segment_ref}"]', ns)
            departure_city = flight_segment.find('.//ns2:Departure/ns2:AirportCode', ns).text
            arrival_city = flight_segment.find('.//ns2:Arrival/ns2:AirportCode', ns).text
            departure_date = flight_segment.find('.//ns2:Departure/ns2:Date', ns).text
            departure_time = flight_segment.find('.//ns2:Departure/ns2:Time', ns).text
            arrival_date = flight_segment.find('.//ns2:Arrival/ns2:Date', ns).text
            arrival_time = flight_segment.find('.//ns2:Arrival/ns2:Time', ns).text
            
            flight_details[passenger_refs] = {
                "departure_city": departure_city,
                "arrival_city": arrival_city,
                "departure_date": departure_date,
                "departure_time": departure_time,
                "arrival_date": arrival_date,
                "arrival_time": arrival_time,
                "price": price
            }
    
    return flight_details

# Example usage
soap_response = """
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
    <!-- SOAP response content -->
</SOAP-ENV:Envelope>
"""
flight_details = parse_flight_details_from_soap_response(soap_response)
print(flight_details)
