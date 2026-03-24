# Program to multiply two matrices using nested loops
import numpy as np
import time
import random
import matplotlib.pyplot as plt
import scipy



Ns = [10, 50, 100, 150, 200, 250, 300, 350, 400, 450, 500, 600, 700, 800]
speedups = []

for N in Ns:
    # NxN matrix
    X = [[random.randint(0, 100) for _ in range(N)] for _ in range(N)]
    
    # Nx(N+1) matrix
    Y = [[random.randint(0, 100) for _ in range(N+1)] for _ in range(N)]
    
    # result is Nx(N+1)
    result = [[0] * (N + 1) for _ in range(N)]

    # Nested loop multiplication (standard logic)
    start_nest = time.time()
    for i in range(N):
        for j in range(N + 1):
            for k in range(N):
                result[i][j] += X[i][k] * Y[k][j]
    elapsed_nest = time.time() - start_nest

    start_np = time.time()

    result_np = np.matmul(np.array(X), np.array(Y))
    elapsed_np = time.time() - start_np

    speedup = elapsed_nest / elapsed_np
    speedups.append(speedup)
    print(f"N = {N}: Nested = {elapsed_nest:.4f}s, Numpy = {elapsed_np:.4f}s, Speedup = {speedup:.2f}x")

# plotting speedup vs array size
plt.figure(figsize=(10, 6))
plt.plot(Ns, speedups, marker='o', linestyle='-', color='b')
plt.xlabel('Matrix Size (N)')
plt.ylabel('Speedup (Nested Loop / NumPy)')
plt.title('NumPy Speedup for Matrix Multiplication (N x N+1)')
plt.grid(True)
plt.show()
