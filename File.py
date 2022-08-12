# write #
fw = open("test.txt", 'w')
string = "1234\n5678\n9101112"
fw.write(string)
fw.close()


# append #
fa = open("test.txt", 'a')
fa.write("APPEND")
fa.close()

# read #
fr = open("test.txt", 'r')
while True :
    line = fr.readline() # read a line
    print(line)
    if not line:
        break
fr.close()

fr = open("test.txt", 'r')
strList = fr.readlines() # read lines separated by 'new line' and return a list
print(strList)
fr.close()

fr = open("test.txt", 'r')
File = fr.read() # Read all
print(File)
fr.close()


# with #
# 'using' in C# #

with open("test.txt", "w") as f :
    f.write("1234")



