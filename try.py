import csv
import requests
import os, sys
import pyttsx
import pytesseract

from PIL import Image
from bs4 import BeautifulSoup
from datetime import datetime
import json
from httplib2 import FileCache

im=Image.open("wallpaper.jpg")
text=pytesseract.image_to_string(im,lang='eng')
print(text)

#reload(sys)
#sys.setdefaultencoding('UTF8')


html ="<string>"+text+"</string>"
# you can put any text that you want to convert 
diction = {'telugu' : 'te' , 'hindi' : 'hi','tamil' : 'ta','urdu' :'ur','malayalam' :'ml' ,'punjabi':'pa' ,'marathi':'mr','kannada':'kn','latin':'la','french':'fr',
'bengali':'bn','gujarati':'gu','japanese':'ja','italian':'it'}
lang=raw_input("Enter the Language that is to be translated into:")

try:
    
    soup=BeautifulSoup(html,"lxml")
    print(soup.find_all('string'))
    url='https://translation.googleapis.com/language/translate/v2/?key=AIzaSyD97Bja9raG9-LKJtVDpVtgv4bS0TdD2Tw'
    for string in soup.find_all('string'):
        print(string.text)
        payload = {
                "q": ""+string.text,
                "target": diction[lang],
                "source": "en",
                "format": "text"
            }
        headers = {'content-type': 'application/json'}
        try:
            response = requests.post(url, data=json.dumps(payload), headers=headers)
            #print(response)
            jsonValue= json.loads(response.text)
            rowValue=""
            print(jsonValue['data']['translations'][0]['translatedText'])
            #string.text=str(jsonValue['data']['translations'][0]['translatedText'])
            tag=string
            tag.string=jsonValue['data']['translations'][0]['translatedText']
            print(string)
            rowValue=""+str(string)
            f = open('helloworld9.txt','a')
            f.write('\n' + rowValue)
            f.close()
        except Exception as R:
            print(R)
            print("error in api hit")
    #print(soup)


except Exception as e:
    exc_type, exc_obj, exc_tb = sys.exc_info()
    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
    print(exc_type, fname, exc_tb.tb_lineno)
    # import pdb;pdb.set_trace()
    print(e)
    print("this is exception part")
engine=pyttsx.init()
engine.say(text)
engine.runAndWait()

