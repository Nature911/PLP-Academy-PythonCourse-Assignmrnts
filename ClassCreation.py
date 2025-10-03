# Defining a class
class Phone:
    def __init__(self, brand, name):
        self.brand = brand   # Instance Variable
        self.name = name     # Instance Variable
        self.__ram = 64      # Encapsulation (private variable)

    # Getter method to access private __ram
    def get_ram(self):
        return self.__ram


# Creating objects
Phone1 = Phone("Samsung", "S23")
Phone2 = Phone("Tecno", "Spark8")

print(f"This brand is {Phone1.brand}, name {Phone1.name}")
print(f"This brand is {Phone2.brand}, name {Phone2.name}")


# Adding Inheritance
class Android(Phone):   # Correct spelling
    pass

android_phone = Android("Redmi", "Note 12")   # Pass both brand and name
print(android_phone.brand)


# Reviewing encapsulation
print(f"{Phone1.name} RAM is", Phone1.get_ram())
print(f"{android_phone.name} RAM is", android_phone.get_ram())
           