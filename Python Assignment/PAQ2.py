# %%
# Q2.1. Create one variable of each type: int, float, string, bool, and list. Print each variable along with its type().
age = 25
mark=78.5
name = "Abhishek"
happy = True
a = [2,5,8,]
print(age)
print(type(age))
print(mark)
print(type(mark))
print(name)
print((type(name)))
print(happy)
print(type(happy))
print(a)
print(type(a))

# %%
""" Q2.2. What is the difference between a list and a tuple? Write one line of code that creates each, and one line
    that shows a list can be changed after creation while a tuple cannot.  """

# A list is mutable (can be changed after creation: items added, removed,
# or modified in place) and uses square brackets []. A tuple is immutable
# (once created, its contents cannot change) and uses parentheses ().
my_list = [1, 2, 3]
my_tuple = (1, 2, 3)
my_list[0] = 99          # works fine — lists can be changed
print(my_list)

# my_tuple[0] = 99        # would raise: TypeError: 'tuple' object does not support item assignment

# %%
# Q2.3. Given price = 499.99 and in_stock = True, write an if statement that prints "Available" only when in_stock is True
price = 499.99
in_stock = True
if in_stock:
    print("Available")
# %%
