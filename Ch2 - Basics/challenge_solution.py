# Solution to programming challenge for Learning Python course
# LinkedIn Learning Python course by Joe Marini
#

def is_palindrome(teststr):
    # use the slice trick to reverse the string
    return teststr == teststr[::-1]

run = True
while (run):
    teststr = input("Enter string to test for palindrome or 'exit':")

    # If the user types "exit" then quit the program
    if teststr == "exit":
        run = False
        break

    # convert the string to all lower case
    teststr = teststr.lower()

    # strip all the spaces and punctuation from the string
    newstr = "".join(x for x in teststr if x.isalnum())
    print("Palindrome test:", is_palindrome(newstr))
