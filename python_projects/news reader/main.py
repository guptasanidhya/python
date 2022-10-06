import json

import requests
url=('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey=dbe288c0219141d68ec3d535ef452155')
response=requests.get(url).text
response_info = json.loads(response)


# print(response_info)
# response_info[]


def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.Speak(str)


if __name__ == '__main__':
 for i in range(0,10):
    print(f"{i+1}.{response_info['articles'][i]['title']}")
    print(f"Description:{response_info['articles'][i]['description']}")
    speak(response_info['articles'][i]['title'])
    speak(response_info['articles'][i]['description'])


 #speak(response_info)