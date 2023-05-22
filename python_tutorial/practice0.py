import re
mystr='''Tata Limited
Dr. David Landsman, executive director
18, Grosvenor Place
London SW1X 7HSc
Phone: +44 (20) 7235 8281
Fax: +44 (20) 7235 8727
Email: tata@tata.co.uk
Website: www.europe.tata.com
Directions: View map

Tata Sons, North America
1700 North Moore St, Suite 1520
Arlington, VA 22209-1911
USA
Phone: +1 (703) 243 9787
Fax: +1 (703) 243 9791
66-66
455-4545
Email: northamerica@tata.com 
Website: www.northamerica.tata.com
Directions: View map fass
sanidhya is a good boy
+91 9876 543210
+91 9876 012345
hiiii
hihihi
9993337474
guptasanidhya6@gmail.com
'''

# patt = re.compile(r'\+91 \d{4}\s\d{6}')
# patt = re.compile(r'\w@\w\.\w')
# patt = re.compile(r'[\w]+@[\w]+\.[\w]+')


# patt=re.compile(r'sanidhya')
# patt=re.compile(r'.anidhya')
# patt=re.compile(r'^Tata')
# patt=re.compile(r'boy$')
# patt=re.compile(r'hi{2}')
# patt=re.compile(r'(hi){1}')
# patt=re.compile(r'hi{1}|boy')
#special sequences
# patt = re.compile(r'\bFax')
# patt = re.compile(r'Fax\b')
# patt = re.compile(r'\d{5}-\d{4}')
patt = re.compile(r'[a-z A-Z 0-9 _.\-]+@[\w]+\.[\w]+')

matches=patt.finditer(mystr)
for match in matches:
    print(match)