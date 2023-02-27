#conveert temprrature to fahrenheit
class Temperature:
    def __init__(self,celsius,farenheit):
        self.celsius=celsius
        self.farenheit=farenheit
        
    def convert_celsius(self):
        return((self.celsius*(9/5))+32)
    def  convert_farenheit(self):
        return(((self.farenheit-32)*5)/9)
    
stud= Temperature(20,20)
print(stud.convert_celsius())
print(stud.convert_ferenheit())

