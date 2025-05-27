#f=open("newtext.txt","x") used x to create a new file.
f=open("newtext.txt","a") #used a to append the text to the file
f.write("this is a new line")
f= open("newtext.txt","r")# used r to read the file after performing append action to it
print(f.read())
f.close()