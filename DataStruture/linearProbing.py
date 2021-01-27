class HashTable:
    def __init__(self):
        self.Max=10
        self.array=[[] for i in range(10)]

    def getHash(self,element):
        h=0#For adding the ordered value
        for i in element:
            h+=ord(i)#for calculating the ASCII Value
        place=h%self.Max #10 is size of memory location
        return place
    def __setitem__(self,key,value): # insted of this push(self,key,value)
        hash=self.getHash(key)
        count=0
        
        self.array[hash].append((key,value))
        if len(self.array[hash])>1:
            for index,elements in enumerate(self.array):
                if len(elements)>1:
                    newPlace=(hash+1)%10
                    self.array[newPlace].append((key,value))
                    self.array[hash].pop()
                    break
    
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
hash["march 17"]=99
hash["march 6"]=97
hash["march 2"]=927
hash["march"]="latest"
hash["maa"]=975
hash["ma"]="Dummy"
print(hash["ma"])
print(hash.array)