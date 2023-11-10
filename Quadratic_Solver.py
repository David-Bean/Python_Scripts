#	Instructions

# 	Quadratic equation:	0 = a*x^2 + b*x + c

#	Step 1: Enter values of a, b, and c

a = -1
b = 2
c = 3

#	Step 2: Press command+b to solve for x



x1 = (-b + pow ((b**2-4*a*c),0.5))/(2*a)
x2 = (-b - pow ((b**2-4*a*c),0.5))/(2*a)

print ("x =", x1, "or", x2)