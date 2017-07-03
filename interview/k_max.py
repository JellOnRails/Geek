def kmax(int_list, k):

	for i in range(1, k+1):
		for j in range(0, len(int_list) - i):
			if int_list[j] > int_list[j+1]:
				buff = int_list[j]
				int_list[j] = int_list[j+1]
				int_list[j+1] = buff

	kmax = int_list[-1*k:]

	return kmax


int_list = [2, 45, 67, 99, 3, 6, 99, 55, 23, 1]
k = 4

kmax = kmax(int_list, k)

print int_list
print '\n'
print kmax