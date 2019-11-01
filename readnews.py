import requests
import json
import time

def voice(text):
    from win32com.client import Dispatch
    test = Dispatch("SAPI.SpVoice")
    test.Speak(text)

url = "https://newsapi.org/v2/top-headlines?country=in&apiKey=16c450dcf999441696f03e943d8993f4"
news = requests.get(url).text
test = requests.get(url)
print(dir(test))
news_dict = json.loads(news)
article = news_dict['articles']
for j in article:
    print("Reading",j['title'])
    voice(j['title'])




