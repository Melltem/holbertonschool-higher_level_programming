#!/usr/bin/python3
import sys
count = len(sys.argv[1:])
element = sys.argv[1:]
if count == 0:
    print("0 arguments.")
else:
    word = "argument:" if count == 1 else "arguments:"
    if __name__ == "__main__":
        print(count, word)
        for i,element in enumerate(element, start=1):
            print(f"{i}: { element}")
