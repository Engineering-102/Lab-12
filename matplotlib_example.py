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
import matplotlib.pyplot as plt
# Part 1
x = np.linspace(-2, 2, 100)
y1 = x**2 / (4 * 2)
y2 = x**2 / (4 * 6)
plt.figure(1)
plt.plot(x, y1, color="blue", linewidth=2, label="f = 2")
plt.plot(x, y2, color="red", linewidth=6, label="f = 6")
plt.title("Parabolas with Different Focal Lengths")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
# Part 2
x = np.linspace(-4, 4, 25)
y = 2*x**3 + 3*x**2 - 11*x - 6
plt.figure(2)
plt.plot(x, y, "go-", label="Cubic Polynomial")
plt.title("Cubic Polynomial")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
#Part 3
x = np.linspace(-2*np.pi, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
plt.figure(3)
plt.subplot(2, 1, 1)
plt.plot(x, y1, color="blue", label="sin(x)")
plt.title("Sine Function")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.grid(True)
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(x, y2, color="red", label="cos(x)")
plt.title("Cosine Function")
plt.xlabel("x")
plt.ylabel("cos(x)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
