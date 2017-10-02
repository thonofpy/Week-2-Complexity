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
