import requests
from bs4 import BeautifulSoup
from win10toast import ToastNotifier

n = ToastNotifier()
#Funcção para obter dados de URL
def getdata(url):
    r = requests.get(url)
    return r.text
#Função para poder analisar página da web
htmldata = getdata("https://weather.com/en-IN/weather/today/l/25.59,85.14?par=google&temp=c/")

soup = BeautifulSoup(htmldata, 'html.parser')

print(soup.prettify())

#Separação de conteudos interessantes para notificação
current_temp = soup.find_all("span",  
                             class_=" _-_-components-src-organism-CurrentConditions-CurrentConditions--tempValue--MHmYY") 
chances_rain = soup.find_all("div",  
                             class_= "_-_-components-src-organism-CurrentConditions-CurrentConditions--precipValue--2aJSf") 
  
temp = (str(current_temp))    
temp_rain = str(chances_rain) 
 
 
 #Faz aparecer a  notificação na area de trabalho sobre a temperatura 
result = "current_temp " + temp[128:-9] + "  in patna bihar" + "\n" +temp_rain[131:-14] 