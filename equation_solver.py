import math
print("I can solve quadratic equations, you just need to put the values of each variables and I solve this in 0.05 seconds!")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
if a == 0:
	print("This is not a quadratic equation, because a = 0!")
else:
	d = b**2 - 4*a*c
	if d < 0:
		print("There is no real roots")
	elif d == 0:
		print("The solution is x =", -b/(2*a))
	else:
		print("The solutions is x1 =", (-b + math.sqrt(d))/(2*a), ", and the second one is x2 =", (-b - math.sqrt(d))/(2*a))

