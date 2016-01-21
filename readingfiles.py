
from sys import argv

script, filename = argv

txt = open(filename)

print ("Here is your file %r" % filename)
print txt.read()

print ("Type the filename again:")
file_again = input(">")

print ("Here is your file %r again" % file_again)
txt_again = open(file_again)

print (txt_again.read())

# in the terminal type python readingfiles bananas.txt

