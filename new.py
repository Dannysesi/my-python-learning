import numpy as np
A = np.array([[2,1,1],[1,2,3],[1,0,0]])
B = np.array([4,5,6])
print("solutions:/n", np.linalg.solve(A, B))