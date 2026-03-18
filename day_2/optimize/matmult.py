# Program to multiply two matrices using nested loops
import random
import time
import numpy as np

N = 300

# NxN matrix
X = []
for i in range(N):
    X.append([random.randint(0,100) for r in range(N)])

# Nx(N+1) matrix
Y = []
for i in range(N):
    Y.append([random.randint(0,100) for r in range(N+1)])

# result is Nx(N+1)
result = []
for i in range(N):
    result.append([0] * (N+1))

start = time.time()
# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]
elapsed = time.time() - start
result = np.array(result)

result_opt = []
for i in range(N):
    result_opt.append([0] * (N+1))
result_opt = np.array(result_opt)


start = time.time()
# iterate through rows of X
cY = list(zip(*Y)) # Take transpose of Y, then cast into a list object
for i in range(len(X)):
    rX = X[i] # Save row of X
    # iterate through columns of Y
    for j in range(len(Y[0])):
        cYj = cY[j] # column j of Y
        result_opt[i][j] = sum(a * b for a, b in zip(rX, cYj)) # replace the last loop by this sum
elapsed_opt = time.time() - start  




if np.array_equal(np.array(result) - np.array(result_opt),np.zeros(result.shape)):
    print("Multiplication correct") # check so multiplication is correct, should print array of zeros
    print(f"elapsed time unoptimized: {elapsed} s")
    print(f"elapsed time optimized: {elapsed_opt} s")
else:
    print(f"multiplication incorrect, difference: {result - result_opt}")