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
        if self.array[hash]==[]:
            self.array[hash].append((key,value))
        else:
            for index,elements in enumerate(self.array):
                if len(elements)!=0:
                    hash=(hash+1)%10
                    if len(self.array[hash])==0:
                        self.array[hash].append((key,value))
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
hash["salmon"]=99
hash["tomato"]="tomato"
hash["march 17"]="march 17"
hash["march 6"]="march 6"
hash["darkblue"]=2
print(hash.array)