import requests
from bs4 import BeautifulSoup as bs
from time import sleep
from random import getrandbits

def entries(amount):
    print("Welcome to @TBGSlay and @Silayman_Nagi's excelsiormilano raffle bot!")
    for i in range(0, amount):
        session = requests.session()
        url = "https://www.excelsiormilano.com/module/antcontactcustom/sendmail"
        email = 'slayadidas+{}@gmail.com'.format(getrandbits(40)) ## CHANGE ENTER_EMAIL_HERE to your EMAIL PRE FIX!!!
        data = {
                    "first_name": "ENTER_NAME_HERE", ## CHANGE ENTER_NAME_HERE to your first name
                    "last_name": "ENTER_NAME_HERE", ## CHANGE ENTER_NAME_HERE to your last name
                    "birth": "ENTER_BIRTH_HERE", ## CHANGE ENTER_BIRTH_HERE to your birthday
                    "mail": email,
                    "number": "ENTER PHONE HERE ", #ENTER PHONE HERE
                    "size": "10", # ENTER SIZE 3-12
                    "country": "United States", # ENTER COUNTRY
                    "state": "MI", #ENTER STATE (abreviated)
                    "city": "Detroit",  # ENTER CITY
                    "zip": "90210", # ENTER ZIP CODE
                    "street": "1234 MAINE ST", # ENTER STREET
                    "sizeKid": "20" # ENTER KIDS SIZE available: 20, 22, 23 1/2, 25, 26, 27
                }
        response = session.post(url, data)
        print('{} out of {} entered with email: {}.'.format(i, amount, email))
if __name__ == '__main__':
    entries(10000000000)
