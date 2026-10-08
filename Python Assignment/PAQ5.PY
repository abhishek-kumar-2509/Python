# %%
# Q5.1. Write a for loop using range() that prints the numbers 1 through 10 (inclusive).
for i in range (1, 11):
    print(i)
   

# %%
# range(start, stop[, step])
for i in range(1, 11, 1):
    print(i, end =" ")


# %%
# Q5.2. Write a for loop that prints every 3rd number from 0 to 30 using the step argument of range().
i = 0
while i<30:
    print(i)
    i+=3



# %%
# Q5.3. Predict the output, then run it: for i in range(10, 0, -2): print(i)
for i in range(10, 0, -2): 
    print(i)        # 10 8 6 4 2


# %%
# Q5.4. Rewrite this for loop as a while loop that produces the same output:  for i in range(0, 20, 4):  print(i)
# 0 4 8 12 16
i = 0
while i < 20:
    print(i)
    i+=4

# %%
# Q5.5. How many times does the condition i < 10 get evaluated in the loop below? Explain your reasoning before  running it.  i = 0
# while i < 10:  print(i)  i += 1

i =0
while i < 10:
    print(i)
    i+=1

# The condition i < 10 is evaluated 11 times: once for each pass where it's
# True (i = 0,1,...,9 -> 10 True evaluations, printing 10 numbers) plus one
# final check when i = 10, which is False and ends the loop.

