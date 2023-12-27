import shelve

db = shelve.open('persondb')

for key in sorted(db):
    print(key, '\t\t==>', db[key])

sue = db['Sue']
sue.giveRaise(.10)
db['Sue'] = sue
db.close()
