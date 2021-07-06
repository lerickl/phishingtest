import pickle  
#from Metodos.buscarMetadatosUrl import buscarMetadatosurl
#from Metodos.tools.remplazar import replace_acentos

#dat = buscarMetadatosurl("https://larepublica.pe/sociedad/2020/10/31/essalud-advierte-que-difteria-es-mas-mortal-que-covid-19/?fbclid=IwAR1nGhzeT7Ogm2_oGgg8PjApXkgGT1P_sSqt3RQw6IYWQak0fmmIbUqDTug")
#cadena = (dat.Obtener_TITLE())
phishing = ['yeniik.com.tr/wp-admin/js/login.alibaba.com/login.jsp.php']
loaded_model = pickle.load(open('Model_phishing.pkl', 'rb'))
result = loaded_model.predict(phishing)
print(result)
 