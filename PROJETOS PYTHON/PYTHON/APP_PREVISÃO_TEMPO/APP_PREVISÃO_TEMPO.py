from tkinter import*
import requests
import json
from datetime import datetime


#backend
#Tela de inicialização
root = Tk()
root.geometry("400x400")#Tamanho da tela
root.resizable(0,0)#Tamanho fixo da tela
root.title("Projeto-RML")#Titulo da Janela




city_value = StringVar()

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
 

def showWeather():
    
    #Colocar api do site de OPENWHEATERMAP 
    api_key = "43fff193b51bfbeec0a67b01e73f7136"
    
    #Nome da cidade 
    city_name=city_value.get()
    
    #site da api
    wheater_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name +api_key
    
    
    #respota do site da api
    response = requests.get(wheater_url)
    
    #escolhendo resposta de json para python
    wheater_info = response.json()
    
    tfield.delete("1.0", "end") # Limpar caixa de texto para nova escrita
    
    if wheater_info['cod'] == 200:#Valor da data do código da api
       kelvin = 273 #Valores em Kelvin
       
       #Valores de temperaturas da cidade
       temp = int(wheater_info['main']['temp'] - kelvin)
       feels_like_temp = int(wheater_info['main']['feels_like'] - kelvin)
       pressure = wheater_info['main']['pressure']
       humidity = wheater_info['main']['humidty']
       wind_speed = wheater_info['wind']['speed'] * 3.6
       sunrise = wheater_info['sys']['sunrise']
       sunset = wheater_info['sys']['sunset']
       timezone = wheater_info['timezone']
       cloudy = wheater_info['clouds']['all']
       description = wheater_info['wheater'][0]['description']
       
       sunrise_time = time_format_for_location|(sunrise+timezone)
       sunset_time = time_format_for_location(sunset + timezone)
       
       #displays variaveis para apresentar
       
       weather = f"\nWeather of: {city_name}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nInfo: {description}"
    else:
        weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
 
 
 
 #Enviar valores de acordo com texto
    tfield.insert(INSERT, weather)


#front_end do código

city_head = Label(root, text = 'Coloque o nome de sua cidade', font = 'Arial 12 bold').pack(pady=10)#para gerar o label para colocar o nome da cidade
inp_city = Entry(root, textvariable = city_value, width=24, font='Arial 14 bold').pack()#entrada de texto

Button(root, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=5, pady=5 ).pack(pady= 20)

wheater_now = Label(root, text = "A Temperatura vai ser", font = 'Arial 12 bold').pack(pady=10)
tfield = Text(root, width=46, height=10)
tfield.pack()

