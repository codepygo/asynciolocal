import xmltodict
from collections import OrderedDict
import pandas as pd
import codecs
# It doesn't work with Python 3! Read on for the solution!
def convert(xml_file, xml_attribs=True):
    with open(xml_file,) as f:
        d = xmltodict.parse(f, xml_attribs=xml_attribs, encoding='utf-8')
        return d



#res=convert("C:\\Users\\yogesh.k\\Downloads\\4bauer\\M_HJR=S_HBJ=V_2017-08-01=Datenbank_Mitarbeiter=C_HJR-XML.xml")
#import pdb;pdb.set_trace()

res=convert("/media/sf_ubuntu_data/virtual_celery_django_proj/django_department/Django/pro/24_release/M_HJR=S_HBJ=V_2017-10-01=Datenbank_Benutzer=C_HJR-XML.xml")
temp_data=[]
for dicts in res['redtext']['redtext-teil']['datenbank']['datenbank-text']['datensatz']:
    finaldict={}
    finaldict['UniqueNo']=dicts['@satzschluessel']
    for lists in dicts['datenfeld']:
        try:
            if type(lists['absatz'])==OrderedDict:
                finaldict[lists['@feldname']]=lists['absatz']['#text']
            else:
                finaldict[lists['@feldname']]=lists['absatz']
        except:
            finaldict[lists['@feldname']]="None"
    temp_data.append(finaldict)


#import pdb;pdb.set_trace()

final=pd.DataFrame(temp_data)

final.to_csv("/media/sf_ubuntu_data/virtual_celery_django_proj/django_department/Django/pro/24_release/user_data_29_jan.csv", encoding='utf-8-sig')
#final.to_csv("C:\\Users\\shinyj\\Desktop\\hbj_data_import_8_nov\\user_data.csv", encoding='utf-8-sig');