def int_numbers(int_list):

	int_data = {}
	num = 0

	for val in int_list:

		if val in int_data:
			int_data[val] += 1
		else: 
			int_data[val] = 1
			
		num +=1

	return int_data

def first_unique_int(int_list):

	int_data = int_numbers(int_list)

	for val in int_list:

		if int_data[val] == 1:
			return val

	return None		

a = [1, 2, 3, 4, 5, 0]

res = first_unique_int(a)
print res