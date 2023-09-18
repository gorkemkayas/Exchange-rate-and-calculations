
import requests
from bs4 import BeautifulSoup


class Doviz(BeautifulSoup):
    def __init__(self):
        super().__init__()
        self.take_infos()
    def take_infos(self):

        web_address = "https://www.doviz.com"
        response = requests.get(web_address)
        html_content = response.content



        while True:
            # [0] = GRAM ALTIN
            # [1] = DOLAR
            # [2] = EURO
            # [3] = STERLİN
            # [4] =  BIST 100
            # [5] = BITCOIN
            # [6] = GRAM GUMUS
            self.summary_table = []
            self.summary_string = ""
            self.currency_names = []
            self.currency_values = []
            self.currency_calculatible_values = []
            self.currency_changes = []
            soup = BeautifulSoup(html_content,"html.parser")
            for names in soup.find_all("span",{"class":"name"}):
                self.currency_names.append(names.text.lstrip())
            for values in soup.find_all("span",{"class":"value"}):
                self.currency_values.append(values.text)
                self.currency_calculatible_values.append(value_calculator(values.text))
            for change in soup.find_all("div",class_=["change-rate status up","change-rate status down","change-rate status"]):                                #for change in soup.find_all("div",{"class":"change-rate status up"}):
                self.currency_changes.append((change.text.strip()))               #self.currency_changes.append(change.text.strip())
            for i in range(0,7):
                self.summary_table.append("".join("{} : {}   {}\n".format(self.currency_names[i],self.currency_values[i],self.currency_changes[i])))
            for j in self.summary_table:
                self.summary_string += j

            return self.summary_string

def value_calculator(girilen_Sayi):
    # Örneğin girilen sayı 1.652,78 olsun. ilk olarak '.' yı kaldıralım
    formed = str(girilen_Sayi).replace(".","")
    formed = float((formed.replace(",",".")).lstrip("$"))
    return formed

value_calculator("1.652,78")




