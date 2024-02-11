import re
from dateutil.parser import parse
from airport_codes import AirportCodes

def extract_travel_details(text):
    # Improved regex patterns for extracting cities and dates
    journey_pattern = re.compile(r"from\s(\w+)\sto\s(\w+)")
    dates = re.findall(r"\b(?:\d{1,2}\s\w{3,9}\s\d{4}|\d{4}-\d{2}-\d{2})\b", text)

    # Attempt to find journey details
    journey_matches = journey_pattern.search(text)
    if journey_matches:
        departure_city, arrival_city = journey_matches.groups()
        departure_code = AirportCodes.get_code(departure_city)
        arrival_code = AirportCodes.get_code(arrival_city)
    else:
        departure_code = arrival_code = "Unknown"

    # Convert extracted dates to standardized format
    formatted_dates = [parse(date).strftime('%Y-%m-%d') for date in dates]

    # Prepare travel details dictionary
    travel_details = {
        "departure_code": departure_code,
        "arrival_code": arrival_code,
        "departure_date": formatted_dates[0] if formatted_dates else None,
        "return_date": formatted_dates[1] if len(formatted_dates) > 1 else None,
    }

    return travel_details

# Example usage
if __name__ == "__main__":
    user_input = input("Please describe your travel plans: ")
    details = extract_travel_details(user_input)
    print(details)
