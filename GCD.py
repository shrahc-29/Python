print("Python Program for GCD using Recursive function.\n")

#Pyhton Program for finding GCD of two numbers using recursive function.
def gcd(A,B):
  if  B==0:
    return A
  else:
    return gcd(B,A%B)
A=int(input("Enter the first number:"))
B=int(input("Enter the second number:"))
print("\nThe GCD of {0} and {1} is: {2}" .format(A,B,gcd(A,B)))
