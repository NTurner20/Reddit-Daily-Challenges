
def warm1(list):
	while 0 in list:
		list.remove(0)
	return list
def warm2(list):
	list.sort(reverse = True)
	return list
def warm3(list, N):
	if(N >= len(list)):
		return True
	else:
		return False
def warm4(list, N):
	for i in range(N):
		list[i] -= 1
	return list
	
def HH(list):
	warm1(list)
	if(len(list) == 0):
		return True		
	warm2(list)
	N =  list.pop(0)
	if (warm3(list, N) == True):
		return False
	warm4(list)
	return HH(list)
nums = [5, 3, 0, 2, 6, 2, 0, 7, 2, 5]
print(HH(nums))
		
	
