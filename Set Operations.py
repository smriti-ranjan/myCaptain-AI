#Write a program to illustrate different Set Operations
#define two set variables and perform different set operations : union, intersection, difference and symmetric difference

E = { 0, 2, 4, 6, 8 }
N = { 1, 2, 3, 4, 5 }

print(f"Union of E and N is {E | N}")
print(f"Intersection of E and N is {E & N}")
print(f"Difference of E and N is {E - N}")
print(f"Symmetric difference of E and N is {E ^ N}")
