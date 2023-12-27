import shelve
from person import Person, Manager

bob = Person('Bob Gilbert')
sue = Person('Sue', 'dev', 10000)
tom = Manager('Tom Jones', pay=10000)

db = shelve.open('persondb')

for obj in (bob, sue, tom):
    db[obj.name] = obj

db.close()
