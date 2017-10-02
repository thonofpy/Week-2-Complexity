def sum_to_k(lst, k):
	i = 0
	j = 1
	while j < len(lst):
		if lst[i] + lst[j] == k:
			return True
		i += 1
		j += 1
	return False
