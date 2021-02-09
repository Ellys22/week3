# name = "Elena Tudorache"

# greeting = f"Welcome, {name}!"

# print(greeting) # Prints: Welcome Elena Tudorache!

# import datetime

# appolo_11_launch = datetime.date(1959, 9, 13)

# print(type(appolo_11_launch))

# print(appolo_11_launch) 

# falcon_9_first_launch = datetime.date(2010, 6, 4)

# print(falcon_9_first_launch > appolo_11_launch) # prints: True

# import datetime

# current_datetime = datetime.date.today() # Returns datetime object of todays date

# print(current_datetime)

# class Animal:
#   def __init__(self, species_name, regions, common_name):
#     """A class to represent a generic animal
#     Attributes
#     ----------
#     species_name : (str) 
#         The technical species name of the animal
#     regions : (list[str]) 
#         A list of regions the animal is endemic to
#     common_name : (str) 
#         The colloquial name of the animal
#     """
#     self.species_name = species_name
#     self.regions = regions
#     self.common_name = common_name
#   def print_info(self):
#     """Prints information about animal instance"""
#     print(f"\nCommon Name: {self.common_name}\nSpecies: {self.species_name}\nRegions: {self.regions}")

# leopard_gecko = Animal("Eublepharis macularius", ["Afghanistan","Pakistan","India", "Iran"],"Common Leopard Gecko")

# leopard_gecko.print_info()

class CookieBaker:
  def __init__(self, number_of_cookies):
    """ Example class that is used to show off the __init__ method.
    The __init__ method calls the bake_cookie() method as many times as there are number_of_cookies.

    Attributes
    ----------
    number_of_cookies(int): How many cookies to bake
    """
    print(f"__init__ method called, creating {number_of_cookies} cookie(s):")
    self.number_of_cookies = number_of_cookies
    for cookie in range(number_of_cookies):
      self.bake_cookie()

  def bake_cookie(self):
    """Print's 'Cookie Baked!'."""
    print("Cookie Baked!")

    cookies = CookieBaker(10)
    cookies.bake_cookie()

