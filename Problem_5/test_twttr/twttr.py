def main():
    #Storage the texting
    texting = input("Input: ")
    final_text = shorten(texting)
    print("Output: " + final_text)
def shorten(texting):
    without_vogal = ""
    #Does a loop for find a vogal in the textubg
    for c in texting:

        if not c in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            without_vogal += c

    return without_vogal

if __name__ == "__main__":
    main()
