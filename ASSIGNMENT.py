
from enum import Enum
from abc import ABC, abstractmethod


# -------------------------------------------------
# 1. ENUMERATION FOR REGIONS
# -------------------------------------------------

class Region(Enum):
    R1 = "USA"
    R2 = "Europe"
    R3 = "Asia"
    R4 = "Africa"


# -------------------------------------------------
# 2. COUNTRY TO REGION MAPPING
# -------------------------------------------------

class CountryRegionMapper:

    def __init__(self):
        self.country_map = {
            "USA": Region.R1,
            "Germany": Region.R2,
            "France": Region.R2,
            "Italy": Region.R2,
            "India": Region.R3,
            "China": Region.R3,
            "Japan": Region.R3,
            "South Korea": Region.R3,
            "South Africa": Region.R4,
            "Egypt": Region.R4,
            "Nigeria": Region.R4
        }

    def get_region(self, country):

        country = country.strip().title()

        if country in self.country_map:
            return self.country_map[country]

        raise ValueError("Country not found in the system.")


# -------------------------------------------------
# 3. CAR CLASS
#    Demonstrates ENCAPSULATION
# -------------------------------------------------

class Car:

    def __init__(self, model, price, country):
        self.__model = model
        self.__price = price
        self.__country = country

    def get_model(self):
        return self.__model

    def get_price(self):
        return self.__price

    def get_country(self):
        return self.__country


# -------------------------------------------------
# 4. ABSTRACT TAX STRATEGY
#    Demonstrates ABSTRACTION
# -------------------------------------------------

class TaxStrategy(ABC):

    @abstractmethod
    def calculate_tax(self, price):
        pass

    @abstractmethod
    def get_tax_rate(self):
        pass


# -------------------------------------------------
# 5. TAX STRATEGIES
#    Demonstrates INHERITANCE & POLYMORPHISM
# -------------------------------------------------

class R1TaxStrategy(TaxStrategy):

    def get_tax_rate(self):
        return 0.10       # 10%

    def calculate_tax(self, price):
        return price * self.get_tax_rate()


class R2TaxStrategy(TaxStrategy):

    def get_tax_rate(self):
        return 0.20       # 20%

    def calculate_tax(self, price):
        return price * self.get_tax_rate()


class R3TaxStrategy(TaxStrategy):

    def get_tax_rate(self):
        return 0.15       # 15%

    def calculate_tax(self, price):
        return price * self.get_tax_rate()


class R4TaxStrategy(TaxStrategy):

    def get_tax_rate(self):
        return 0.12       # 12%

    def calculate_tax(self, price):
        return price * self.get_tax_rate()


# -------------------------------------------------
# 6. FACTORY PATTERN
# -------------------------------------------------

class TaxStrategyFactory:

    @staticmethod
    def get_strategy(region):

        if region == Region.R1:
            return R1TaxStrategy()

        elif region == Region.R2:
            return R2TaxStrategy()

        elif region == Region.R3:
            return R3TaxStrategy()

        elif region == Region.R4:
            return R4TaxStrategy()

        else:
            raise ValueError("Invalid region.")


# -------------------------------------------------
# 7. PRICING SERVICE
# -------------------------------------------------

class CarPricingService:

    def __init__(self, mapper):
        self.mapper = mapper

    def calculate_price(self, car):

        # Find region of the country
        region = self.mapper.get_region(
            car.get_country()
        )

        # Select appropriate tax strategy
        tax_strategy = TaxStrategyFactory.get_strategy(region)

        # Calculate tax
        tax = tax_strategy.calculate_tax(
            car.get_price()
        )

        # Calculate final price
        final_price = car.get_price() + tax

        # Display result
        print("\n----------------------------------------")
        print("       CAR PRICING DETAILS")
        print("----------------------------------------")

        print("Car Model    :", car.get_model())
        print("Country      :", car.get_country())
        print("Region       :", region.name)
        print("Continent    :", region.value)
        print("Base Price   : ₹", format(car.get_price(), ",.2f"))
        print("Tax Rate     :", tax_strategy.get_tax_rate() * 100, "%")
        print("Tax Amount   : ₹", format(tax, ",.2f"))
        print("Final Price  : ₹", format(final_price, ",.2f"))

        print("----------------------------------------")


# -------------------------------------------------
# 8. MAIN PROGRAM
# -------------------------------------------------

def main():

    print("========================================")
    print("   REGIONAL CAR PRICING SYSTEM")
    print("========================================")

    model = input("Enter car model: ")

    try:
        price = float(input("Enter car base price: ₹"))
    except ValueError:
        print("Invalid price!")
        return

    country = input("Enter country of origin: ")

    # Create Car object
    car = Car(model, price, country)

    # Create Country-Region Mapper
    mapper = CountryRegionMapper()

    # Create Pricing Service
    pricing_service = CarPricingService(mapper)

    try:
        pricing_service.calculate_price(car)

    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()




