def sum_to_k(lst, k):
	i = 0
	j = 1
	while i < len(lst):
		if lst[i] + lst[j] == k:
			print(lst[i] + lst[j])
		i += 1
		j += 1
