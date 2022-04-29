import time

# Create a function that reverses a string:
# "Hi My name is Andrei" should be:
# "ierdbA su eman yM iH"

name = "Hi My name is Andrei"

def reverse(letter):
    name_reverse = ""
    for i in letter[::-1]:
        name_reverse += i
    print(name_reverse)

def reverse_2(letter):
    name_reverse = letter[::-1]
    print(name_reverse)

start = time.time()
reverse(name)
print("Function using time: ", (time.time() - start)*1000000000)

start = time.time()
reverse_2(name)
print("Function using time: ", (time.time() - start)*1000000000)