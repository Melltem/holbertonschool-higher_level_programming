#!/usr/bin/python3
import sys
if __name__ == "__main__":
    total = 0
    for num in sys.argv[1:]:
        total = total + int(num)
    print(total)
