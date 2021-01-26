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
        found=False
        for index,element in enumerate(self.array[hash]):
            if len(element)==2 and element[0]==key:
                
                self.array[hash][index]=(key,value)
                found=True
                break
             
        else:
            self.array[hash].append((key,value))
    def __getitem__(self,key):# insted of this get(self,key):
        hash=self.getHash(key)
        for index,elments in enumerate(self.array[hash]):
            if len(elments)==2 and elments[0]==key:
                return elments[1]
            else:
                return None

        
    def __delitem__(self,key):
        hash=self.getHash(key)
        for index,elments in enumerate(self.array[hash]):
            if len(elments)==2 and elments[0]==key:
                del self.array[hash][index]
                break
        else:
            self.array[hash]=None


hash=HashTable()
hash["Love"]="List"
hash["march 6"]=99 #instead of this hash.push("march 6",99)

hash["march 17"]="March 17"
hash['march 17']="Pundai"
del hash["march 17"]
print(hash["march 17"])




    