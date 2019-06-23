#reddit challenge, find the number of revised julain calander leap years 

def leaps(year1, year2):
	leaps = 0
	if year2 < year1:
		raise Exception("Year 1 must be less than Year 2")
	else:
		dif = year2 - year1
		for nums in range(dif):
			year = year1 + nums
			if year%100 == 0:
				if (year%900 == 600) or (year%900 == 200):
					leaps = leaps + 1
			else:
				if year % 4 == 0:
					leaps = leaps + 1
		print(leaps)
				
leaps(123456,7891011)