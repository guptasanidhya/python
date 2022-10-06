from flask import Flask,request
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)
@app.route('/products',methods=['GET'])
def helloWorld():


    productName=request.args.get('q') #getting the query name i.e. shoes,mobile,etc.
    # print(productName)
    """here we fetch fata using query parameter
     http://127.0.0.1:5000/products?q=shoes
     """
    htmlSourceCode = getHtmlSourceCode(productName)#passing the product name in function and getting response
    # print(htmlSourceCode)
    soup = BeautifulSoup(htmlSourceCode, 'html.parser')#passing the htmlsource code in beautiful soup
    # print(soup)
    # a_tags=soup.findAll('a',{'class':'s1Q9rs'})

    urls=list()#creating a list for all the anchor tags fetched from page

    for a in soup.findAll('a',{'class':'s1Q9rs'}):
        urls.append('https://www.flipkart.com'+a['href'])#books class
    for a in soup.findAll('a',{'class':'_1fQZEK'}):
        urls.append('https://www.flipkart.com'+a['href'])#mobiles class
    for a in soup.findAll('a',{'class':'IRpwTa'}):
        urls.append('https://www.flipkart.com'+a['href'])#shoes class

    products=list()#list for adding individual dictionaries data dictionary include price,name,ratings
    for url in urls:
        product=dict()
        page_soup=BeautifulSoup(requests.get(url).text,'html.parser')
        name=page_soup.find('h1',{'class':'yhB1nd'})
        product['name']=name.text

        price = page_soup.find('div', {'class': '_30jeq3 _16Jk6d'})
        product['price'] = price.text
        # print(price.text)

        ratingsAndReviews=page_soup.find('span',{'class':'_2_R_DZ'})
        if ratingsAndReviews is None:
            product['ratingsAndReviews'] = '0 ratings & 0 reviews'
        else:
            product['ratingsAndReviews'] = ratingsAndReviews.text

        products.append(product)

    return {'products':products}


def getHtmlSourceCode(productName):


    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Language': 'en-US,en;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'T=TI165996010709700364085954513943055913428472190300284581859767548125; ab.storage.userId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%225244591%22%2C%22c%22%3A1659960106133%2C%22l%22%3A1659960106139%7D; ab.storage.deviceId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%22706a7d3f-99b7-d094-3ccb-6baa4360c3cc%22%2C%22c%22%3A1659960106142%2C%22l%22%3A1659960106142%7D; AMCVS_17EB401053DAF4840A490D4C%40AdobeOrg=1; AMCV_17EB401053DAF4840A490D4C%40AdobeOrg=-227196251%7CMCIDTS%7C19213%7CMCMID%7C31828613290668098712898697584855130332%7CMCAID%7CNONE%7CMCOPTOUT-1659967313s%7CNONE%7CMCAAMLH-1660564913%7C12%7CMCAAMB-1660564913%7Cj8Odv6LonN4r3an7LhD3WZrU1bUpAkFkkiY1ncBR96t2PTI; pxcts=e5e14923-1711-11ed-b13b-737174694c78; _pxvid=e5e13fa2-1711-11ed-b13b-737174694c78; Network-Type=4g; ab.storage.sessionId.7af503ae-0c84-478f-98b0-ecfff5d67750=%7B%22g%22%3A%22dde86504-cb3e-b4e3-4c28-1eb5a39fd249%22%2C%22e%22%3A2159960116650%2C%22c%22%3A1659960106137%2C%22l%22%3A1659960116650%7D; qH=7d8949bcbf85067f; S=d1t19NXc/P1o/fj95PxAuei0/P6Ot4Zq4g8v7qtlFm7reP/Ek/pBv42+1YkxLLuZP3UEuQ07L/L4mFGRXXBLKH8b4lw==; _px3=006baaddf61692dd4f88ef8a19a11cc25a13b70531e1fef757529a90ce303b54:nCUvM4WmZc7a0zwwP4zF7PWDRYSZmYagMt3F8KOXNUlFVp++lcKDHpylv6PecUg++Wl4T42zKHH/bJIZg8wHpw==:1000:SWPBudPB9+C4uyn4s6XIhXCqmzp2FJ7x+u1DjatcdnBQbPO+ajErZeZRKlGN6muQUaS6gVgyDJyL6WmJMv0RR5n/xugeveBXoy6S+iJypKtTsdmLkwYrHipl5UVK2PMTjKUB11g52KyhzFLG0gZ/K1lW2hbws08G6e30n2Hoz58vmNLRC4fUotOPKinuQxEg1miM9reZnUrIFoWZOZFHHg==; SN=VI4E4A2932ECBC40A28C5524A8EF1061D8.TOK6829C00141164C2A914452D28640A13D.1659960143.LO',
        'Referer': 'https://www.flipkart.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    params = {
        'q': productName,
        'otracker': 'search',
        'otracker1': 'search',
        'marketplace': 'FLIPKART',
        'as-show': 'off',
        'as': 'off',
    }

    response = requests.get('https://www.flipkart.com/search', params=params, headers=headers)
    return response.text

if __name__ == "__main__":
    app.run(debug=True)
