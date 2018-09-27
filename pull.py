import requests
import re
# download for InstrumentModbusRegisters.xlsx
file_url = "http://windchillapp.pitnet.com/Windchill/servlet/AttachmentsDownloadDirectionServlet?oid=OR:wt.doc.WTDocument:162785177&oid=OR:wt.content.ApplicationData:162785247&role=PRIMARY"
# download for InstErrorCodeListwithAction.xlsx
#file_url = "http://windchillapp.pitnet.com/Windchill/servlet/AttachmentsDownloadDirectionServlet?oid=OR:wt.doc.WTDocument:162744106&oid=OR:wt.content.ApplicationData:162744124&role=PRIMARY"

user = null # implement user input code
pswd = null # implement user input code

authsite = requests.get(file_url, auth=(user, pswd)) 

m = re.search('(?<=downloadURL = ")(\S+)(?=")', authsite.text)

print m.group(0)

loc = m.group(0)

print "location obtained"
print "done"

r = requests.get(loc, stream = True)
with open(" InstrumentModbusRegisters.xlsx","wb") as excel: 
    excel.write(r.content) 
