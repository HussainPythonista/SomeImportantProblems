class HashTable:
    def __init__(self):
        self.Max=10
        self.array=[[] for i in range(100)]

    def getHash(self,element):
        h=0#For adding the ordered value
        for i in element:
            h+=ord(i)#for calculating the ASCII Value
        place=h%self.Max #10 is size of memory location
        return place
    def __setitem__(self,key,value): # insted of this push(self,key,value)
        hash=self.getHash(key)
        self.array[hash].append((key,value))
    def __getitem__(self,key):# insted of this get(self,key):
        hash=self.getHash(key)
        return self.array[hash]
    def __delitem__(self,key):
        hash=self.getHash(key)
        self.array[hash]=0


hash=HashTable()
hash["march 6"]=99 #instead of this hash.push("march 6",99)

hash["march 17"]="March 17"
del hash["march 18"]
print(hash.array)


    