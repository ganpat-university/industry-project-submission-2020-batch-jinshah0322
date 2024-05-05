my_list = [1, 2, 3, 4, 5]
my_set = set(my_list)
print("List converted to set:", my_set)

my_set = {1, 2, 3, 4, 5}
my_list = list(my_set)
print("Set converted to list:", my_list)

my_list = [('a', 1), ('b', 2), ('c', 3)]
my_dict = dict(my_list)
print("List converted to dictionary:", my_dict)

my_dict = {'a': 1, 'b': 2, 'c': 3}
my_list = list(my_dict.items())
print("Dictionary converted to list of tuples:", my_list)

my_string = "hello"
my_list = list(my_string)
print("String converted to list of characters:", my_list)

my_list = ['h', 'e', 'l', 'l', 'o']
my_string = ''.join(my_list)
print("List of characters converted to string:", my_string)