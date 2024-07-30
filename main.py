from bs4 import BeautifulSoup

linkInput = input("Enter Your Link: ")

with open(linkInput) as webLink:
    link = BeautifulSoup(webLink)
    print(link)
