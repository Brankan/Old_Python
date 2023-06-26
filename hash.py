import random

def hash(text):
    text=str(text)
    numbers=[]
    for letters in text:
        numbers.append(ord(letters))
    numbers=sum(numbers)
    numbers=numbers %100
    return numbers

hash('bruhbruh')


class Slownik:
    def __init__(self):
        self.tables =[[] for _ in range(100)]

    def add_values(self,key,value):
        if self.tables[hash(key)] is None:
            raise IndexError('error')
        else:
            self.tables[hash(key)].append([key,value])




    def get_value(self,key):
        print(self.tables[hash(key)])


moj_slownik=Slownik()
moj_slownik.add_values(10,10)

moj_slownik.get_value(10)


print(moj_slownik.tables)