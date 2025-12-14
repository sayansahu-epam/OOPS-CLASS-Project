#HYUNDAI CARS COMPANY IMPLEMENTATION

from abc import ABC,abstractmethod #importing necessary abstract methods

class Company(ABC):
    
    def __init__(self,name,origin):
        self._name=name#i am using it protected so child classes can access
        self._origin=origin
    
    #ABSTRACT METHODS
     
    @abstractmethod
    def get_company_info(self):
        pass
    
    @abstractmethod
    def manufacture(self):
        pass
    

#We cannot instantiate Company class directly as its abstract

#Hyundai Class

#Properties

#name(inherited)
#origin(inherited)
#plant_loc
#est_year

#Methods

#get_company_info() inherited
#manufacture() inherited
#get_brand_det() 

class Hyundai(Company):
    
    def __init__(self, origin,plant_loc,est_year):
        super().__init__("Hyundai",origin)
        self.plant_loc=plant_loc
        self.est_year=est_year
        
    def get_company_info(self):
        return (
            f"Company {self._name} \n"
            f"Origin   {self._origin} \n"
            f"Establised in {self.est_year} \n"
            
        )
        
    def manufacture(self):
        return (f"Company-> {self._name} Manufactures Cars,Sedans,SUV's")
    
    def get_brand_det(self):
        return (f"Comapany {self._name} Plant is at {self.plant_loc}")
    

class SUV(Hyundai):
    def __init__(self, origin, plant_loc, est_year):
        super().__init__(origin, plant_loc, est_year)
        
        
    def cat_type(self):
        return f"SUV's From {self._name}"
    
    def manufacture(self):
        return f"{self._name}  Manufactures SUV's"
    
class Sedan(Hyundai):
    
    def __init__(self, origin, plant_loc, est_year):
        super().__init__(origin, plant_loc, est_year)
        
    
    def cat_type(self):
        return f"{self._name} Manufactures Sedans"
    
    def manufacture(self):
        return f"{self._name} Manufactures Sedans"
    

class Hatchback(Hyundai):
    def __init__(self, origin, plant_loc, est_year):
        super().__init__(origin, plant_loc, est_year)
        
    def cat_type(self):
        return f"{self._name} Manufactures Hatchbacks"
    
    def manufacture(self):
        return f"{self._name} Manufactures Hatchbacks"
    
    

#Small Testing I am doing

# suv=SUV("Korea","India",2016)
# sedan=Sedan("Korea","India",2018)
# Hb=Hatchback("Korea","India",2000)

# print(suv.cat_type())
# print(suv.est_year)
# print(suv.get_company_info())




class Creta(SUV):
    def __init__(self, origin, plant_loc, est_year,price):
        super().__init__(origin, plant_loc, est_year)
        self.__price=price
        self.engine_type="Petrol/Diesel"
        self.mileage="22.4 kmpl"
    
    def car_features(self):
        return f"Creta is a premium SUV from {self._name}"
    
    @property#accessing private properties not directly but using method
    def price(self):
        return self.__price
    
    def calc_price(self):
        return f"Price is {self.__price}"
    




class Verna(Sedan):
    def __init__(self, origin, plant_loc, est_year,price):
        super().__init__(origin, plant_loc, est_year)
        self.__price=price
        self.engine_type="Petrol/Diesel"
        self.mileage="18.6 kmpl"
    
    def car_features(self):
        return f"Verna is a premium Sedan from {self._name}"
    
    @property#accessing private properties not directly but using method
    def price(self):
        return self.__price
    
    def calc_price(self):
        return f"Price is {self.__price}"

    

class Grand_i_10(Hatchback):
    def __init__(self, origin, plant_loc, est_year,price):
        super().__init__(origin, plant_loc, est_year)
        self.__price=price
        self.engine_type="Petrol/Diesel"
        self.mileage="24.8 kmpl"
    
    def car_features(self):
        return f"Grand i110 is a Economy Hatchback from {self._name}"
    
    @property#accessing private properties not directly but using method
    def price(self):
        return self.__price
    
    def calc_price(self):
        return f"Price is {self.__price}"

        
        

creta=Creta("India","Karnataka",2018,1300000)
verna=Verna("India","Jaisalmer",2015,1000000)
grandi_10=Grand_i_10("India","Raipur",2017,800000)

cars_collection=[creta,verna,grandi_10]

print("_________________POLYMORPHISM_________")

for c in cars_collection:
    print(c.car_features())
    
print()
print("_____MANUFACTURING__INFO_______")

for c in cars_collection:
    print(c.manufacture())
    
    
print("_________ENCAPSULATION________")

for c in cars_collection:
    print(c.calc_price())
    

    

    

        
        

