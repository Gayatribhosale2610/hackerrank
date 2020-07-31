class Test:
def __init__(self, name):
self.cards = []
self.name = name

def __str__(self):
return '{} holds ...'.format(self.name)
        
obj1 = Test('obj1')
print obj1

obj2 = Test('obj2')
print obj2
