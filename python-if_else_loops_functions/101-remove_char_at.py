#!/usr/bin/python3
print("%s" % "".join(
    chr(97 + 25 - i) if i % 2 == 0 else chr(65 + 25 - i)
    for i in range(26)), end="")
