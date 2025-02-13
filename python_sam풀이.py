import requests as req
import sys
url = "https://finance.naver.com/sise/sise_market_sum.naver"
web = req.get(url)
html = web.text

args = sys.argv

def sam(jong):
    f2 = html.find(jong)
    return (f"{jong}"+html[f2:f2+100][19:50].replace('<td class="number">',"").replace("</td>","").replace('\n',"")+"원")

if __name__ == "__main__":
    print(sam(jong[1]))