x = np.arange(10)
x
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = x[1:3]  # creates a view
y
array([1, 2])
x[1:3] = [10, 11]
x
array([ 0, 10, 11,  3,  4,  5,  6,  7,  8,  9])
y
array([10, 11])
