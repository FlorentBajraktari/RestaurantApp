from base_enum import Location
import order_calculators

class OrderCalculatorFactory:
    
    @staticmethod
    def get_order_calculator_by_location(location):
        match(location):
            case Location.KOSOVO:
                return order_calculators.OrderCalculatorKS()
            case Location.GERMANY:
                return order_calculators.OrderCalculatorGER()
            case _:
                print("Current location is invalid. OrderCalculator could not be determined. ")
                