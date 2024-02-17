import re
import sys

def main():
    # call and print the fuction return
    print(parse(input("HTML: ")))

def parse(s):
    # if matches is true return only the video name
    if matches := re.search(r"https?://(?:www\.)?youtube\.com/(\w+)/(\w+)", s, re.IGNORECASE):
        return (f"https://youtu.be/{matches.group(2)}")

if __name__ == "__main__":
    main()
