# read mode
f = open('hi.txt', 'r')

# store the content in file_text variable
file_text = f.read()

# close hi.txt
f.close()

# display content
print(file_text)
