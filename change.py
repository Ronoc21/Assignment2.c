# Author: Conor Smith
# Date: 04/07/21
# Description: Converts a number less than 100 into appropriate change (USD)
Q = 25
D = 10
N = 5
P = 1
print("Please enter an amount in cents less than a dollar.")
num_1 = int(input())
print("Your change will be:")
print("Q:", num_1 // Q)
print("D:", num_1 % Q // D)
print("N:", num_1 % Q % D // N)
print("P:", num_1 % Q % D % N // P)
