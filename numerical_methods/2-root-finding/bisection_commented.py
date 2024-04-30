from sympy import symbols, Eq, sympify

def my_bisection(f,a,b,tol):
	R=[]
	E=[]
	while True:
		midpoint=(a+b)/2
		R.append(float(str(midpoint).rstrip('0')))
		fx=f.subs(x,midpoint)

		if fx<0:
			a=midpoint 
		elif fx>0:
			b=midpoint
		else:
			return [R,E]

		fx=abs(fx)
		E.append(float(str(fx).rstrip('0')))

		if fx<tol:
			return [R,E]

x=symbols('x')
print(my_bisection(sympify(input()),int(input()),int(input()),float(input())))