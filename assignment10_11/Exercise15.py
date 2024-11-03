"""Exercise-15: Use filter and lambda to Remove Elements
Write a function "remove_elements(my_list: list, element) -> list" that uses filter and a lambda function to remove all instances of a specific element from a list.

Example:
remove_elements([1, 2, 3, 2, 4, 2, 5], 2) -> [1, 3, 4, 5]
"""

def remove_elements(my_list: list, element):
    #return list(filter(lambda x: x != element, my_list))
    filtered_list = []
    for x in my_list:
        if x != element:
            filtered_list.append(x)
    return filtered_list
print(remove_elements([1, 2, 3, 2, 4, 2, 5], 2))


