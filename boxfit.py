#reddit challange, find the number of boxes that can fit in the larger box for 2D, 2D w rotation and 3D w rotation
x_tot = 0
y_tot = 0
z_tot = 0
tot = 0
def fit1(X,Y,x,y):
	for i in range(X+1):
		if i*x <= X:
			x_tot = i
	for i in range(Y+1):
		if i*y <= Y:
			y_tot = i
	tot = x_tot*y_tot
	return tot
def fit2(X,Y,x,y):
	if fit1(X,Y,y,x) > fit1(X,Y,x,y):
		return fit1(X,Y,y,x)
	else:
		return fit1(X,Y,x,y)
	
#print("Number of boxes:\n",fit2(5,100,6,1))
def fit3_1(X,Y,Z,x,y,z):
	for i in range(X + 1):
		if i*x <= X:
			x_tot = i
	for i in range(Y + 1):
		if i*y <= Y:
			y_tot = i
	for i in range(Z + 1):
		if i*z <= Z:
			z_tot = i
	tot = x_tot * y_tot * z_tot
	return tot
def fit3(X,Y,Z,x,y,z):
	list = [fit3_1(X,Y,Z,x,y,z),fit3_1(X,Y,Z,x,z,y),fit3_1(X,Y,Z,y,x,z),fit3_1(X,Y,Z,y,z,x),
	fit3_1(X,Y,Z,z,x,y),fit3_1(X,Y,Z,z,y,x)]
	return max(list)
print("Number of boxes:\n",fit3(123,456,789,10,11,12))
					
		
			
		

