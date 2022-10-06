from tensorflow import constant,ones_like,multiply,Variable
import tensorflow as tf
# Define tensors A1 and A23 as constants
A1 = constant([1, 2, 3, 4])
A23 = constant([[1, 2, 3], [1, 6, 4]])

# Define B1 and B23 to have the correct shape
B1 = ones_like(A1)
B23 = ones_like(A23)

# Perform element-wise multiplication
C1 = multiply(A1,B1)
C23 = multiply(A23,B23)

print(C1)
print(C23)

a1 = Variable([-1.0])
print(a1)
b=multiply(-1,-1)
print(b)
"""
Performing element-wise multiplication
Element-wise multiplication in TensorFlow is performed using two tensors with identical shapes. This is because the operation multiplies elements in corresponding positions in the two tensors. An example of an element-wise multiplication, denoted by the ⊙ symbol, is shown below:

  
  
 [1221]⊙[3125]=[3245]

In this exercise, you will perform element-wise multiplication, paying careful attention to the shape of the tensors you multiply. Note that multiply(), constant(), and ones_like() have been imported for you.

Instructions
70 XP
Define the tensors A1 and A23 as constants.
Set B1 to be a tensor of ones with the same shape as A1.
Set B23 to be a tensor of ones with the same shape as A23.
Set C1 and C23 equal to the element-wise products of A1 and B1, and A23 and B23, respectively.
"""