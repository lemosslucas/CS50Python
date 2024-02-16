# Storage the answer
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
# Lower the answer
answer = answer.lower()
# A array of codition
if answer in ["42", "forty-two", "forty two"]:
    print("Yes")
# If != 0 
else:
    print("No")