from bs4 import BeautifulSoup
import requests

URLInput = "https://www.newegg.ca/amd-ryzen-7-7800x3d-ryzen-7-7000-series/p/N82E16819113793"
#input("Enter Your Link: ")

result = requests.get(URLInput)

with open(result) as link:
    page = BeautifulSoup(link.text, "html.parser")
    print(page.prettify)
