#Array Operations
import numpy as np
a1=np.arange(9,dtype=float).reshape(3,3)
print("First array: ")
print(a1)
print("  ")

a2=np.array([[3,6,9],[12,24,0],[6,4,14]])
print("Second Array: ")
print(a2)
print("  ")

print("Addition: ")
print(np.add(a1,a2))
print("  ")

print("Subraction: ")
print(np.subtract(a1,a2))
print("  ")

print("Multiplication: ")
print(np.multiply(a1,a2))
print("  ")

print("Division: ")
print(np.divide(a1,a2))
