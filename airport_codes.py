class AirportCodes:
    _codes = {
        "Sharjah": "SHJ",
        "Trivandrum": "TRV",
        "Delhi": "DEL",
        "Bangalore": "BLR",
        "Hyderabad": "HYD",
        "Colombo": "CMB",
        "Dhaka": "DAC",
        "Bahrain": "BAH",
        "Cairo": "CAI",
        "Chennai": "MAA",
        "Kochi": "COK",
        "Mumbai": "BOM",
        "Milan": "BGY",
        "Kuwait": "KWI",
        "Karachi": "KHI",
        "Jeddah": "JED",
        "Abu Dhabi": "AUH",
        "Coimbatore": "CJB",
        "Beirut": "BEY",
        "Alexandria": "HBE",
        # Add more mappings as needed
    }

    @classmethod
    def get_code(cls, city_name):
        """Retrieve airport code for a given city, handling variations and case sensitivity."""
        city_key = city_name.title()
        return cls._codes.get(city_key, "Unknown")

    @classmethod
    def add_city(cls, city_name, airport_code):
        """Add a new city and its airport code to the dictionary."""
        cls._codes[city_name.title()] = airport_code.upper()

# Example usage
if __name__ == "__main__":
    print(AirportCodes.get_code("Sharjah"))  # Should print "SHJ"
    AirportCodes.add_city("New City", "NCI")
    print(AirportCodes.get_code("New City"))  # Should print "NCI"
