#!/usr/bin/python3
import sys
count = len(sys.argv[1:])
element = sys.argv[1:]
if __name__ == "__main__":
    print(count, "argument:")
    for i,element in enumerate(element, start=1):
        print(f"{i}: { element}")
