# Import the fuctions of emoji
import emoji
# Storage the input
emoji_user = input("Input: ")
# Convert the input for emoji
output = emoji.emojize(emoji_user, language='alias')
# print the input in emoji
print("Output:", output)
