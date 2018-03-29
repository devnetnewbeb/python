

Skip to content
This repository
Search
Pull requests
Issues
Marketplace
Explore
 @devnetnewbeb
Sign out
0
0 0 devnetnewbeb/python
 Code  Issues 0  Pull requests 0  Projects 0  Wiki  Insights  Settings
python/ex16.py
9671a54  39 minutes ago
@devnetnewbeb devnetnewbeb Create ex16.py
     
36 lines (23 sloc)  667 Bytes

from sys import argv

script, filename = argv

print (f"We're going to erase {filename}.")
print (f"If you don't want that, hit CTRL-C (^C).")
print ("If you do want that, hit RETURN.")

input("?")

print ("Opening the file...")
target = open(filename, 'w')

print ("Truncating the file. Goodbye!")
target.truncate()


print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()
© 2018 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
API
Training
Shop
Blog
About
Press h to open a hovercard with more details.
