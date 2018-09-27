import requests
import re
# download for InstrumentModbusRegisters.xlsx
file_url = "http://windchillapp.pitnet.com/Windchill/servlet/AttachmentsDownloadDirectionServlet?oid=OR:wt.doc.WTDocument:162785177&oid=OR:wt.content.ApplicationData:162785247&role=PRIMARY"

user = 'nsteward' # implement user input code
pswd = 'Leg0stew' # implement user input code

authsite = requests.get(file_url, auth=(user, pswd)) 
with open("temp.txt","wb") as txt: 
    txt.write(authsite.content)
