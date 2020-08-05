# Python for Data Science and Machine Learning - Part1 Excercises

# ** What is 7 to the power of 4?**

num = 7**4
print(num)

#** Split this string:** s = "Hi there Sam!" *into a list. *

s = 'Hi there Sam!'
new_s = list(s.split())
print(new_s)

# ** Given the variables:**
# planet = "Earth"
# diameter = 12742
# ** Use .format() to print the following string: **
# The diameter of Earth is 12742 kilometers.

planet = 'Earth'
diam = 12742
print(f"The diameter of {planet} is {diam} km.")

# ** Given this nested list, use indexing to grab the word "hello" **

lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
hi = lst[3][1][2][0]
print(hi)

#** Given this nested dictionary grab the word "hello". Be prepared, this will be annoying/tricky **

d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
hi2 = d['k1'][3]['tricky'][3]['target'][3]
print(hi2)

#** Create a basic function that returns True if the word 'dog' is contained in the input string.
# Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **

def findDog(sentence):
    if 'dog' in sentence:
        print("You've found a doggo!")
        return True

findDog("Hello, Mr dog!")


#** Create a function that counts the number of times the word "dog" occurs in a string. Again ignore edge cases. **

def howManyDoggos(sentence):
    counter = 0
    sentence = sentence.lower()
    doggolist = list(sentence.split())
    for word in doggolist:
        if word == 'dog':
            counter += 1
        else:
            pass
    print
    print (f"You've got {counter} doggos!")
    return counter

howManyDoggos('dog had a dog and ate a hot dog Dog dog dog dog')

#** Use lambda expressions and the filter() function to filter out words from a list that don't start with the letter 's'. For example:**
# seq = ['soup','dog','salad','cat','great']
# should be filtered down to:
# ['soup','salad']

seq = ['soup','dog','salad','cat','great']
new_list = list(filter(lambda word: word[0]=='s',seq))
print(new_list)

# Final Problem
# *You are driving a little too fast, and a police officer stops you.
# Write a function to return one of 3 possible results: "No ticket", "Small ticket", or "Big Ticket".
# If your speed is 60 or less, the result is "No Ticket".
# If speed is between 61 and 80 inclusive, the result is "Small Ticket".
# If speed is 81 or more, the result is "Big Ticket".
# Unless it is your birthday (encoded as a boolean value in the parameters of the function) --
# on your birthday, your speed can be 5 higher in all cases. *

def whatTicket(speed, is_birthday):
    if is_birthday == True:
        velocity = speed - 5
    else:
        velocity = speed

    if velocity <= 60:
        print("No ticket")
    elif velocity >80:
        print("Big ticket")
    else:
        print('Small ticket')

whatTicket(30, False)



