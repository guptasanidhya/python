# Import numpy as np
import numpy as np

# Set the seed
ludo=np.random.seed(123)
# ludo=np.random.rand()
ludo=np.random.randint(4,8)
# Generate and print random float
print(ludo)
ludo1=np.random.randint(4,8)
print(ludo1)

"""seed(): sets the random seed, so that your results are reproducible between simulations. As an argument, it takes an integer of your choosing. If you call the function, no output will be generated.
rand(): if you don't specify any arguments, it generates a random float between zero and one."""
