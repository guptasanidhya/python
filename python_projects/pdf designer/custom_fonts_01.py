from fpdf import FPDF
# create FPDF object
#Layout('P','L')
#Unit('mm','cm','in')
#format('A3','A4'(DEFAULT),'A5','Letter','Legal',(100,150))
pdf =FPDF('P','mm','Letter')
#same as part 1 except the hash block newly added
###############################################################################################3
pdf.add_font('Agency','','C:\Windows\Fonts\AGENCYR.ttf') #trueType font subset embedding

#google fonts
pdf.add_font('oswald','B',r"E:\study\Extra\python\python_projects\pdf designer\Oswald-Bold.ttf")
pdf.add_font('oswald','',r"E:\study\Extra\python\python_projects\pdf designer\Oswald-Regular.ttf")
#################################################################################################

#Add a page
pdf.add_page()

#specify font
# fonts ('times','courier','helvetica','symbol','zpfdingbats')
# 'B'(bold),'U'(underline),'I'(italics),''(regular),combination(i.e.,('BU'))
pdf.set_font('Agency','',16)
pdf.set_text_color(220,50,50)
#Add text
#w=width
# h=height
# txt=your text
# ln(0 FALSE;1 TRUE- move cursor down to next line)
# border(0 FALSE;1 TRUE-add border around cell)
pdf.cell(120,100,'Hello World!',ln=True,border=True)
pdf.set_font('oswald', 'B', 12)
pdf.cell(80, 10, 'Good Bye World!')

pdf.output('fonts_1.pdf')