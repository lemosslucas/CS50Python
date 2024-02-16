#Storage the greeting
greeting = input("Greeting: ")
# Lower the string
greeting = greeting.lower()
# A array of conditions with the wanted worlds
if greeting in ["hello", "hello, newman", " hello "]:
    print("$0")
elif greeting in ["how you doing?", "hey", "how's it going"]:
    print("$20")
elif greeting in ["what's happening?", "what's up?"]:
    print("$100")