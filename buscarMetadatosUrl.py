import requests, re
from bs4 import BeautifulSoup
 
class buscarMetadatosurl():
    def __init__(self, url):    
        self.url= url  
        self.HTML = requests.get(url)
        self.soup = BeautifulSoup(self.HTML.text, "html.parser")
    def obtener_Url(self):
        return self.url
    def Obtener_TITLE(self): 
        titulo = self.soup.find(property="og:title")
        cadena=titulo.get('content')
        dat = replace_acentos(cadena)
        
        return dat
    def Obtener_Descripcion(self):         
        description = self.soup.find(property="og:description")
        cadena=description.get('content')
        dat = replace_acentos(cadena)
        return dat
    def Obtener_Charset(self):
        encoding = self.soup.find(property="og:code")
        cadena=encoding.get('content')
        dat= replace_acentos(cadena)
        return dat
    def obtener_author(self):




def replace_acentos(cadena): 
    cadena= cadena.upper()
    cadena= cadena.replace('Á','A');
    cadena= cadena.replace('É','E');
    cadena= cadena.replace('Í','I');
    cadena= cadena.replace('Ó','O');
    cadena= cadena.replace('Ú','U');
    cadena= cadena.replace('Ñ','N');
    cadena= cadena.replace('Ä','A');
    cadena= cadena.replace('Ë','E');
    cadena= cadena.replace('Ï','I');
    cadena= cadena.replace('Ö','O');
    cadena= cadena.replace('Ü','U');
    cadena.lower()
    return cadena
 
                
    

   