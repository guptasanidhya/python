"""entities collection"""
"""

['Lina']
['Castillo']
['Teresa', 'Lozano', 'Long']
['Universidad', 'de', 'Texas']
['Austin']
['Austin', '.']
['Austin', '.', 'Ella']
['Gabriel', 'García', 'Márquez']
['Gabriel', 'García', 'Márquez']
['LIna']
['Castillo']
['colombiano']
['Colombia']
['Estados', 'Unidos']
['Castillo']
['Nation']
['Kenneth', 'Nebenzahl']
['Jr']
['Library']
['Society']
['Humboldt']
['América', 'Latina']
['.', 'García', 'Márquez']
['colombiano']
['Gabriel', 'García', 'Márquez']
['Gabo']
['Fidel', 'Castro']
['Gabo']
['Castro']
['colombianos']
['Gabo']
['colombiano']
['colombiano', 'Belisario', 'Betancur']
['Betancur']
['Fuerzas', 'Armadas', 'Revolucionarias', 'de', 'Colombia']
['FARC']
['Gabo']
['Cuba']
['Betancur']
['Gabo']
['Cuba']
['.', 'Betancur']
['Gabriel', 'García', 'Márquez']
['Gabo']
['San', 'Vicente', 'del', 'Caguán']
['Andrés', 'Patrana']
['FARC']
['Gabo']
['Pastrana']
['Ejército', 'de', 'Liberación', 'Nacional']
['ELN']
['García', 'Márquez']
['Mercedes', 'Barcha']
['ELN']
['La', 'Habana']
['Gabo']
['La', 'Habana']
['Gabo']
['Fidel', 'Castro']
['Gabriel', 'García', 'Márquez']
['Fidel', 'Castro']
['Gabriel', 'García', 'Márquez']
['Carmen', 'Balcells']
['La', 'Habana']
['Estados', 'Unidos']
['Colombia']
['.', 'Gabriel', 'García', 'Márquez']
['Gabo']
['Salman', 'Rushdie']
['Elena', 'Poniatowska']
['Gabo']
['Gabo']
['Gabriel', 'García', 'Márquez']
['García', 'Márquez']
['Macondo']
['colombiana']
['United', 'Fruit', 'Company']
['colombiano']
['Ciénaga']
['Santa']
['Santa', 'Marta']
['García', 'Márquez']
['York']
['Español']
['José', 'Arcadio', 'Segundo']
['García', 'Márquez']
['United', 'Fruit']
['Colombia']
['Macondo']
['Gabo']
['Gabo']
['Ciénaga']
['colombiana']
['José', 'Arcadio', 'Segundo']
['García', 'Márquez']
['Gabriel', 'García', 'Márquez']
['Harry', 'Ransom']
['Harry', 'Ransom', 'Center']
"""
"""
Spanish NER with polyglot
You'll continue your exploration of polyglot now with some Spanish annotation. This article is not written by a newspaper, so it is your first example of a more blog-like text. How do you think that might compare when finding entities?

The Text object has been created as txt, and each entity has been printed, as you can see in the IPython Shell.

Your specific task is to determine how many of the entities contain the words "Márquez" or "Gabo" - these refer to the same person in different ways!

Instructions
100 XP
Iterate over all of the entities of txt, using ent as your iterator variable.
Check whether the entity contains "Márquez" or "Gabo". If it does, increment count. Don't forget to include the accented á in "Márquez"!
Hit 'Submit Answer' to see what percentage of entities refer to Gabriel García Márquez (aka Gabo).

"""
# from polyglot import text
# # Create a new text object using Polyglot's Text class: txt
# txt = Text(article)
# here article is different

# # Initialize the count variable: count
# count = 0
#
# # Iterate over all the entities
# for ent in txt.entities:
#     # Check whether the entity contains 'Márquez' or 'Gabo'
#     if "Márquez" in ent or "Gabo" in ent:
#         # Increment count
#         count=count+1
#
# # Print count
# print(count)
#
# # Calculate the percentage of entities that refer to "Gabo": percentage
# percentage = count / len(txt.entities)
# print(percentage)


#output

"""
<script.py> output:
    29
    0.29591836734693877
"""