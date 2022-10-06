from tensorflow import reduce_sum,constant
import numpy
wealth=constant([[11,50],[7,2],[4,60],[3,0],[25,10]])

#sum wealth over its rows
wealth_sum=reduce_sum(wealth,1)

#sum wealth over its columns
wealth_col=reduce_sum(wealth,0)

#convent result to numpy array
array=reduce_sum(wealth_col).numpy()

print(array)
"""
Summing over tensor dimensions
You've been given a matrix, wealth. This contains the value of bond and stock wealth for five individuals in thousands of dollars.

wealth = 
 
[115072460302510]

The first column corresponds to bonds and the second corresponds to stocks. Each row gives the bond and stock wealth for a single individual. Use wealth, reduce_sum(), and .numpy() to determine which statements are correct about wealth.

Instructions
35 XP
Possible Answers

The individual in the first row has the highest total wealth (i.e. stocks + bonds).

Combined, the 5 individuals hold $50,000 in stocks.

Combined, the 5 individuals hold $50,000 in bonds.

The individual in the second row has the lowest total wealth (i.e. stocks + bonds).

Submit Answer

Hint
reduce_sum(wealth,1) will sum wealth over its rows.
reduce_sum(wealth,0) will sum wealth over its columns.
Note bonds appear first and stocks appear second in reduce_sum(wealth,0).
You can append .numpy() to reduce_sum() to convert the results to a numpy array.
"""