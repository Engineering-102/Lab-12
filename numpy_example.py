# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who do."
# "I have not given or received any unauthorized aid on this assignment."
#
# Names:  Tyler Haidaczuk
# Jai Joshi
# Benjamin Sparks
# NA
# Section: 571
# Assignment: Lab Topic 11 Team
# Date: 12 November 2026
#
# As a team, we have gone through all required sections of the 
# tutorial, and each team member understands the material
import numpy as np
A = np.arange(12).reshape(3, 4)
B = np.arange(8).reshape(4, 2)
C = np.arange(6).reshape(2, 3)
print("A =", A)
print()
print("B =", B)
print()
print("C =", C)
print()
D = A @ B @ C
print("D =", D)
print()
print("D^T =", D.T)
print()
E = np.sqrt(D) / 2
print("E = ", E)
