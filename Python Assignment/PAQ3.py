# %%
""" Q3.1. Explain in your own words the difference between `is` and `==` in Python."""
# `==` checks whether two variables have the same VALUE (they are equal in
# content). `is` checks whether two variables point to the exact same
# OBJECT in memory (same identity). Two different objects can hold equal
# values (== True) while still being different objects (is False).


# %%
# Q3.2. Predict the output, then verify by running it:
a = [1, 2, 3]
b = [1, 2, 3]
print(a == a)       #True   -> same contents
print(a is b)       #fase   -> two separate list objects in memory



# %%
# Q3.3. Create two variables x = 100 and y = 100. Check x is y and x == y. Now create p = 1000 and q = 1000 and
# check the same. Look up (or discuss) why small integers may behave differently from large ones.
x = 100
y = 100
print(x is y, x == y)

p = 1000
q = 1000
print(p is q, p==q)     # 'is' result is not guaranteed here; often False in a plain script,
                         # sometimes True in an interactive shell. CPython pre-caches and
                         # reuses integer objects from -5 to 256; numbers outside that range
                         # aren't guaranteed to be cached, so two separately created 1000s
                         # may or may not be the same object. `==` is always True regardless

# %%
""" Q3.4. Everything in Python is an object. Using type(5), type("hi"), and type([1,2]), show that even numbers and
 strings are objects with a type.  """

# %%
print(type(5), type("Hi"), type([1,2]))
# This shows every value in Python — even simple ints and strings — is an
# object that has a type, not a "primitive" in the C/Java sense.
