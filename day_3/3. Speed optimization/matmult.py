# Program to multiply two matrices using nested loops
import numpy as np
import time
import random
import matplotlib.pyplot as plt
import scipy

Ns = [40, 50, 100, 200, 300]#, 350, 400, 600, 700, 800]
speedup = np.zeros(len(Ns))
for n, N in enumerate(Ns):
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
    start_nest = time.time()
    # iterate through rows of X
    for i in range(int(len(X))):
        # iterate through columns of Y
        for j in range(int(len(Y))):
            # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][i]
    elapsed_nest = time.time() - start_nest

    start_np = time.time()
    #import ipdb; ipdb.set_trace()
    result_np = scipy.linalg.blas.sgemm(1.0, X, Y)
    elapsed_np = time.time() - start_np





    print(f"Nested loop took {elapsed_nest} seconds to execute.")
    print(f"Numpy  multiplication took {elapsed_np} seconds to execute.")
    print(f"Numpy is {elapsed_nest/elapsed_np} faster at N = {N}")
    speedup[n] = elapsed_nest/elapsed_np

plt.plot(Ns, speedup)
plt.ylabel("Speedup [s]")
plt.xlabel("N")
plt.show()
