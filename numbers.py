def sum_to_k(lst, k):
	i, j = 0, 1
	while j < len(lst):
		if lst[i] + lst[j] == k:
			return True
			break
		i += 1
		j += 1
	else:
		return False

##################################
# version 2 - might be bull shit #
##################################
def sum_to_k(lst, k):

	# find middle of list
	if len(lst) % 2 != 0:
		middle = int(len(lst)/2)
	else:
		middle = int(len(lst)/2-1)

	# if k < middle, start from lst[0], else start from middle
	if k < lst[middle] + lst[middle+1]:
		i, j = 0, 1
	else:
		i, j = middle, middle+1

	while j < len(lst):
		if lst[i] + lst[j] == k:
			return True
				break
		i += 1
		j += 1
	else:
		return False
