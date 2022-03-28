import webbrowser
import requests
import re
from bs4 import BeautifulSoup
import tkinter as tk
import time

#getting the price of desired ticker
def getPrice():
    site = ("https://www.google.com/finance/quote/ETH-USD")
    html = requests.get(site)
    soup = BeautifulSoup(html.text, 'html.parser')
    price = soup.find('div', class_="YMlKec fxKbKc").text
    output = re.findall("\d", price)
    number = ""
    for i in output:
        number = number + i
    number = int(number)
    number = number/100
    number = ('%.2f' % number)
    return number

 


menu = tk.Tk()
menu.title("ETH")
menu.geometry("400x100")
menu.configure(bg = 'black')
fontTuple = ("Terminal", 50, "underline")
text = tk.Label(menu, text = "$" + getPrice(), bg = 'black', fg = '#20C20E', font = fontTuple)
text.grid()

def task():
    menu.after(2000, task)

menu.after(2000, task)
menu.mainloop()   
