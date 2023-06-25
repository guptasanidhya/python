"""
Your first word cloud
We saw in the video that word clouds are very intuitive and a great and fast way to get a first impression on what a piece of text is talking about.

In this exercise, you will build your first word cloud. A string east_of_eden has been defined for you. It contains one of the first sentences of John Steinbeck's novel East of Eden. You can inspect its contents in the IPython Shell.

The matplotlib.pyplot package has been imported for you as plt.

Instructions 1/2
50 XP
Import the required package to build a word cloud.
Generate a word cloud using the east_of_eden string. The background color has been specified as white.

Instructions 2/2
50 XP
Create a figure from the word cloud object you generated in the previous step.
Display the image.
"""
east_of_eden='I remember my childhood names for grasses and secret flowers. I remember where a toad may live and what time the birds awaken in the summer—and what trees and seasons smelled like—how people looked and walked and smelled even. The memory of odors is very rich.'
from wordcloud import WordCloud

# Generate the word cloud from the east_of_eden string
cloud_east_of_eden = WordCloud(background_color="white").generate(east_of_eden)

import matplotlib.pyplot as plt

# Create a figure of the generated cloud
plt.imshow(cloud_east_of_eden, interpolation='bilinear')
plt.axis('off')
# Display the figure
plt.show()
