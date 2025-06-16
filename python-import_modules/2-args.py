#!/usr/bin/python3
import sys
count = len(sys.argv[1:])
element = sys.argv[1:]
print(count, "arguments:")
for i,element in enumerate(element, start=1):
    print(f"{i}: { element}")
