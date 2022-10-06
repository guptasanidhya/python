# Build histogram with 5 bins
import matplotlib.pyplot as plt
life_exp=[1,1,2,3,4,5,6,7,8,9,10,10,10,10,11,11,11,11,11,11]
plt.hist(life_exp,bins=5)

# Show and clean up plot
plt.show()
plt.clf()

# Build histogram with 20 bins
plt.hist(life_exp,bins=20)

# Show and clean up again
plt.show()
plt.clf()