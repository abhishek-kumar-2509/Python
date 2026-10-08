# %%
# <Q1.1.> Write a variable 'age' and assign it the integer 25. Print its value and its type using type().
age = 25
print(age)
print(type(age))

# %%
"""Q1.2. Assign the string "10" to a variable called num, then reassign num to the integer 10. Print num and type(num) after each 
    assignment to show dynamic typing in action."""

num ="10"
print(num)
print(type(num))

num = 10
print(num)
print(type(num))

# %%
""" Q1.3. In C or Java, why would `int x = 3; x = 4.5;` fail to compile, but the equivalent code runs fine in Python?
Answer in 2-3 sentences.    """
""" Answer Below:
In C/Java, variables are statically typed: when we write `int x`, the
compiler reserves memory sized and interpreted specifically for an int,
and it checks at compile time that only int-compatible values are ever
assigned to x. Assigning a float (4.5) violates that contract, so it
fails to compile. Python is dynamically typed — a name like x is just a
label that can point to ANY object, and the type lives with the object,
not the variable. So reassigning x to a float just makes x point to a
new float object; there's no compile-time type contract to violate.     """

# %%
#  Q1.4. Predict the output (write your prediction, then run it):
x = 5
x = "five"
print(x)

# Prediction: "five" — x is just a label; it gets rebound to the string object.

