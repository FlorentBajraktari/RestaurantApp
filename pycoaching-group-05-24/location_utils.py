from base_enum import Location

class LocationManager:
    
    @staticmethod
    def get_location_from_id(location_id):
        for location in Location:
            if location.value == location_id:
                return location
        raise Exception("No location could be found for the given location parameters.")
    
    
    