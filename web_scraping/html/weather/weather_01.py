from requests_html import HTMLSession

s =HTMLSession()
query='indore'
url=f'https://www.google.com/search?q=weather+in+{query}'
#in headers it is my user agent search it on google
r=s.get(url,headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36'})

temp=r.html.find('span#wob_tm',first=True).text
print(temp)
unit =r.html.find('div.vk_bk.wob-unit span.wob_t',first=True).text
print(unit)
desc=r.html.find('div.wob_dcp',first=True).find('span#wob_dc',first=True).text
print(desc)