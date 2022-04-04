my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print my_list in the console
print("Input list is", my_list)

# Square all numbers in my_list
squared_list_lambda = list(map(lambda x: x ** 2, my_list))

# Print the result of the map function
print("The squared numbers are", squared_list_lambda)

my_list2 = [10, 21, 31, 40, 51, 60, 72, 80, 93, 101]
# Print my_list2 in the console
print("Input list is:", my_list2)

# Filter numbers divisible by 10
filtered_list = list(filter(lambda x: (x%10 == 0), my_list2))

# Print the numbers divisible by 10
print("Numbers divisible by 10 are:", filtered_list)