def getHash(element):
        h=0#For adding the ordered value
        for i in element:
            h+=ord(i)#for calculating the ASCII Value
        place=h%10 #10 is size of memory location
        return place
value=getHash("march")
print(value)