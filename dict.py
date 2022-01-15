#in python 3.6 or earlier dictories are unordered,in latest ordered
#duplicates not allow
person = {
    "name": "ghazi",
    "age" :22,
    "country" : "pakistan",
    "age":22
}
#print(person)
#print(len(person))
#print(type(person))
#x=person["name"]
#print(x)
#x= person.get("name")
#print(x)
#x=person.keys()
#print(x) 
#x=person.values()
#print(x)
#x=person.items()
#print(x)
#if "name" in person:
#    print("Yes, It's completed")
#person["age"]=40 #value change ki he
#print(person)
#person.update({"age":40})
#print(person)
#person.update({"id":21})
#print(person)
#person["id"]=21 #value add ki he
#print(person)
#person.update({"id":21,"number":50})
#print(person)
#person.pop("age")
#print(person)
#person.popitem()#popitem removes last item
#print(person)
#del person["age"]
#print(person)
#del person
#print(person)
person.clear()
print(person)