from bs4 import BeautifulSoup
import requests
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',}

url = "http://www.dyxia.com/Dongman/SS35851/"
file = open("jieguo","w")

web_data = requests.get(url,headers=headers)
soup = BeautifulSoup(web_data.text,"lxml")
downloads = soup.select('a[href^="thunder://"]')
for download in downloads:
    downloadurl = str(download).split('"',2)[1]
    file.write(downloadurl + "\n")
    print downloadurl

