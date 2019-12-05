f1 = open ("tester.txt", "r")
text= f1.read()
f1.close()
text.split(":")
for string in text:
    print (string)
