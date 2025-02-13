import requests as req
import sys
url = "https://finance.naver.com/sise/sise_market_sum.naver"
web = req.get(url)
html = web.text

args = sys.argv
def kia(name):
    if __name__ == "__main__":
        if name == "삼성전자":
            f2 = html.find(name)
            return html[f2:f2+100][19:50].replace('<td class="number">',"").replace("</td>","").replace('\n',"")+"원"
        elif arg[1] == "기아":
            f1 = html.find(name)
            return html[f1:f1+100][17:50].replace('<td class="number">',"").replace("</td>","").replace('\n',"").replace('\t',"")+"원"
    