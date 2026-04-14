import numpy as np

# Example points
p1 = np.array([5.1,3.5,1.4,0.2])
p2 = np.array([4.9,3.0,1.4,0.2])

distance = np.linalg.norm(p1 - p2)

print("Euclidean Distance:", distance)
