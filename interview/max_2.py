def assign_max(val, max1, max2):

	if val > max1:
		max2 = max1
		max1 = val

	return [max1, max2]


def assign_first_max(int_list):

	max1 = int_list[0]
	max2 = None

	index = 1
	while (int_list[index] == max1) and (index < len(int_list)):
		index += 1
		max2 = int_list[index]

	if (not max2) or (max1 == max2):
		return [max1, None]	

	return [max1, max2]


def is_valid(int_list):

	if len(int_list) < 2:
	return -1


def kmax(int_list):

	elif len(int_list) == 2:

		max2 = int_list[0]
		if int_list[1] < max2:
			return max2
		elif int_list[1] == max2:
			return None 	

	max1 = int_list[0]
	max2 = None



	for val in int_list[1:]:

		if max1 < val:
			maxx = val

	return maxx		