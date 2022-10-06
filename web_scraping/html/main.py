"""
if you want to scrape a website
1.use the API
2.HTML web scraping using some tool like bs4
"""
"""
step 0:Install all the requirements
pip install requests
pip install bs4
pip install html5lib
"""
import requests
from bs4 import BeautifulSoup
url="https://codewithharry.com"

#step 1: get the html
"""In order to work with the HTML, we will have to get the HTML as a string. We can easily get HTML data by using get() function in requests module. We first need to import this module by writing:"""
r=requests.get(url)# r variable has all the HTML code
htmlContent=r.content# r returns response so if we want the code we write r.content
# print(htmlContent)# printing the code

"""
r.text is the response in Unicode and r.content is the response in bytes.
Instead of “content” we can also use “text”:
htmlText = r.text
print(htmlText)"""

#step:2 Parse the Html
"""
BeautifulSoup (bs4):
Beautiful Soup is the perfect module to parse or transverse through HTML code. We can easily target any div, table, td, tr, class, id, etc. The basic template(boilerplate code) which is used everytime is:
"""
soup=BeautifulSoup(htmlContent,'html.parser')
"""We can also save an HTML file instead of getting data everytime, take that HTML file’s data in a variable and in the same way just write the variable in the function, both are same things."""
# print(soup)
print(soup.prettify)# to print html in tree structure

#step:3 tree traversal
#commonly used types of objects:
"""
title=soup.title
print(title)
print(type(title))# 1. Tag
print(title.string)
print(type(title.string))# 2.NavigableString
print(type(soup))#3.beautifulSoup
## 4. Comments
markup="<p><!-- this is a comment --></p>"
soup2=BeautifulSoup(markup,'html.parser')
print(type(soup2.p.string))
"""
###############################################################################################



#find()
"""It is used to get first element in the HTML page. It could be any element. For eg:"""

#print(soup.find('p'))

"""This line will get you first p tag of the page. If we want all paragraphs(all p tags) of the page then we can use find_all() function"""
#find_all():
paras=soup.findAll('p')
#print(paras)
"""Whatever tag you want to scrap, write that tag in the function as argument. Also when we print paras variable,  it will print it like a list. If we want every item one by one, we just put it through a for loop and iterate it, like this:"""
#for i in paras:
    #print(i)
#Getting class of an element:
"""Earlier we were getting text from the tag, this time we are getting class of the element. To get class of an element we need to write:"""
#print(soup.find('p')['class'])
"""Here we are using find() function to get p tag like before but we added [‘class’] in it. It’s like list slicing, tag has a class variable, we are getting that variable’s value. If we want other variables like id, style, role, type, we can get them all"""
#Finding elements through class name:
"""Most of the times we don’t want to find by tag name because it isn’t that accurate so we use class name there. Code to find elements by class name:"""
#print(soup.find_all('p', class_='mt-2'))
"""We can also avoid writing tag name if you are not sure about tag name. You can simply write like:"""
#print(soup.find_all(class_='text-sm'))
"""There is no find_all() function for id because id can be given to only one element."""




#Getting text from tags(text/get_text()):
"""When we write soup.find(‘element’) it returns the whole tag:"""
textdata=soup.find('p').text
textdata2=soup.find('p').get_text()
# print(textdata)
# print(textdata2)


#####################################################################################################

#Getting all the links:
anchors=soup.find_all('a')
"""This will get all the anchor tags but anchor tags have text in them. Links are in href and href is a variable written in the tag. What did I tell you about getting variables from tags? Slicing! It can be done like this:"""
# for i in anchors:
#     print(i['href'])
# for i in anchors:
#         print(i.get('href'))

all_links=set()
for link in anchors:
    if(link.get('href')!='#' and "https" not in link.get('href')):
            linktext="https://codewithharry.com" + link.get('href')
            all_links.add(linktext)
            print(linktext)
# print(all_links)

###########################################################################################################################################################
html = '''
<body>
    <ul>
        <li>This</li>
        <li><a>This</a>This</li>
        <li>This</li>
        <li>This</li>
        <li id="li">This</li>
        <li>    This is wow    </li>
    </ul>
</body>
'''
soup3 = BeautifulSoup(html, 'html.parser')
ul = soup3.find("ul")
# print(ul.contents)
#Children, parent, next_sibling and previous_siblings:
"""You can see HTML tree like a family tree. In a family tree there are parents, children, siblings, exactly like that in HTML tree we have children, parent and siblings. You can understand it like children means one step inside the tree, parent means one step outside the tree and siblings mean in the same step, other elements. Here is a simple code to understand it better:"""
"""Here body is parent to ul and ul is parent to li. li is children to ul and ul is children to body. All li tags are each others siblings, easy way to understand is their parent(ul) is same so siblings. Code for all three is:"""
#1.Children
# ul = soup3.find("ul")
# for i in ul.children:
#     print(i,end="")

#2.parent
# ul = soup3.find("ul")
# for i in ul.parent:
#     print(i,end="")

#for parent of parent
"""You just have to write “.parent”, to get parent of parent, write:"""
# ul = soup3.find("ul")
# for i in ul.parent.parent:
#     print(i,end="")
#3.next_sibling and previous_siblings:
"""Like parent we can go to next sibling and then next sibling like this:"""
# ul = soup3.find(id="li")
# for j in ul.next_siblings:
#     print(j)

# for i in ul.previous_siblings:
#     print(i)
"""Like next_sibling, we can also use previous_sibling() function and code is similar like earlier:"""

#Difference between content and Children
"""
Children and content are no different. The only difference is content returns a list but children gives a generator.
 If we print contents we can just see the list but if we print children we see:

<list_iterator object at 0x000002532ABDF190>
Copy
This is an object which is iterable so if we want to get values from it then we just have to iterate it by using a for loop.
 But why generator? When to use contents and when to use children? Contents simply takes whatever is there and store it in memory but
  generator doesn’t store it, it only processes when we ask for the value and it processes on the fly because of which there is no 
  storage happening which helps when we have to scrap big data. If we scrap big data with contents, it will store everything and fill
   up our memory because of which code may crash. So at that time we can use children. 
    """

"""# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator
"""
nav=soup.find(id="nav-content")
# print(nav)
# for elem in nav.contents:
#     print(elem)


# for elem in nav.children: #print the elements of nav
#     print(elem)


# for item in nav.strings:#get the string data from the elements
#     print(item)


# for item in nav.stripped_strings:
#     print(item)

# print(nav.parent)#give the parent of nav
# print(nav.parents)#give the generator


# for item in nav.parents: #extract  from current to the top parent from the generator
#     print(item.name)

print(nav.next_sibling)#it returns none because it doesnt have next sibling

#stripped Strings
"""stripped_strings does the same thing which in-built strip() function does. It takes away all the spaces."""
# ul=soup3.find(id="li")
#elem=ul.next_sibling   #it returns an empty string because a new line chracter is also treated as sibling
# elem=ul.next_sibling.next_sibling
# print(elem)
# for i in elem.stripped_strings:
#     print(i)

"""
exit():
exit() function is used to exit a program. It is helpful while finding errors or when we want to see code in pieces. If you have written a code of say 100 lines and on 71st line you have written exit() then it will not compile rest of the 29 lines, it will exit right there."""
#########################################################################################################################################################
#SAme as CSS Selectors we use in jQuery
elem=soup.select("#nav-content")#extracting data in a list
print(elem)