# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'bonn',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw',
          'australia':'vienna' }

# Update capital of germany

europe['germany']='berlin'
# Remove australia
europe.pop('australia')

# Print europe
print(europe)
"""The capital of Germany is not 'bonn'; it's 'berlin'. Update its value.
Australia is not in Europe, Austria is! Remove the key 'australia' from europe.
Print out europe to see if your cleaning work paid off."""