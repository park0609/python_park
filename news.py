

import os
import sys
import urllib.request
from dotenv import load_dotenv
load_dotenv()
MKEY = os.getenv("MYKEY")
PASS = os.getenv("PASSWORD")
client_id = MKEY #"MY_ID"
client_secret = PASS #"MY_SECRET"
encText = urllib.parse.quote("연예")
url = "https://openapi.naver.com/v1/search/news.json?query=" + encText 
 # JSON 결과
# url = "https://openapi.naver.com/v1/search/blog.xml?query=" + encText # XML 결과
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()
if(rescode==200):
    response_body = response.read()
    print(response_body.decode('utf-8'))
else:
    print("Error Code:" + rescode)
