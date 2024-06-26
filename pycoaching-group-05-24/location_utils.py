from base_enum import Location

class LocationManager:
    
    @staticmethod
    def get_location_from_string(location_as_string):
        for location in Location:
            if location.name == location_as_string:
                return location
        raise Exception("No location could be found for the given location parameters.")
    
    