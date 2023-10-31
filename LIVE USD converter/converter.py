#importing requests library to get acces to api
import requests

class CurrencyConverter:
    def __init__(self, url):
        self.data = requests.get(url).json() # getting acces and formating to json for further usage
        self.currencies = self.data['rates'] #getting currencies data
        self.name_of_currencies = list(self.currencies.keys())[1:] # getting names of curencies and excluding 1st (usd)
        print("*** Welcome to Live USD converter.These is our currencies *** \n ", ", ".join((self.name_of_currencies)))

#Convert function which returns calculated amount of usd
    def convert(self, from_currency, to_currency, amount):
        if from_currency != "USD":
            amount = amount / self.currencies[from_currency]
        amount = round(amount * self.currencies[to_currency], 4)# rounding to only 4digits
        return amount

url = 'https://api.exchangerate-api.com/v4/latest/USD'
converter = CurrencyConverter(url)#creating variable which includes our url in class

user_currency = str(input("\nFrom USD To which currency do you want to convert? \nYour input(only 3 letter): ").upper())
user_amount = float(input("What amount: ")) 

result = converter.convert('USD', user_currency, user_amount)  #using variable to use in function
print(f"{user_amount}USD is  {result} {user_currency}")
