# %%
# Q4.1. Create a string name = "pYTHOn". Print name.upper(), name.lower(), and name.title().
name = "pYTHOn"
print(name.upper())
print(name.lower())
print(name.title())


# %%
# Q4.2. Predict the output, then run it:s = "Hello"  s.lower()  print(s)
s = "Hello"
s.lower()
print(s)        #Hello -> strings are immutable


# %%
# Q4.3. Now try: s = "Hello"  s = s.lower() print(s),  Explain why the output differs from the previous question.
s = "Hello"
s = s.lower()
print(s)        #hello

# Prediction: "hello" — this time the returned lowercase string was
# reassigned back to s, so s now refers to the new lowercase string object.


# %%
""" Q4.4. Given sentence = " Learning Python is fun ", use string methods to: (a) remove the leading/trailing spaces, 
 (b) count how many times the letter 'n' appears, (c) split the sentence into a list of words. """

sentence = "      Learning Python is fun   "
cleared = sentence.strip()
n_count  =sentence.count("n")
word = cleared.split()

print(cleared)
print(n_count)
print(word)
