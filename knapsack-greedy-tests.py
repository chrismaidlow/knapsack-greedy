
objects = [
	(5, 2)	
]
expected = [(5, 2)]
result = greedy(10, objects)
print(result)
assert expected == result

objects = [
	(6, 3),
	(5, 2),
]
# Note that although the first object is more valuable,
# it is also much heavier.
expected = [(5, 2), (6, 3)]
result = greedy(10, objects)
print(result)
assert expected == result

objects = [
	(6, 3),
	(15, 2),
	(11, 2.5),
	(6, 7),
	(2.5, 9),
	(5, 4),
]
expected = [(15, 2), (11, 2.5), (6, 3), (5, 4), (6, 7), (2.5, 9)]
result = greedy(100, objects)
print(result)
assert expected == result

objects = [
	(6, 3),
	(15, 2),
	(11, 2.5),
	(60, 7),
	(2.5, 9),
	(5, 4),
]
expected = [(60, 7), (15, 2)]
result = greedy(10, objects)
print(result)
assert expected == result

objects = [
	(6, 3),
	(15, 2),
	(11, 2.5),
	(6, 0.5),
	(2.5, 9),
	(5, 4),
]
expected = [(6, 0.5), (15, 2), (11, 2.5), (6, 3)]
result = greedy(10, objects)
print(result)
assert expected == result