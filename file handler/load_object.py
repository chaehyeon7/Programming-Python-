import pickle
# 객체 하나 불러오자
with open('object.bin', 'rb')as f:
    p1 = pickle.load(f)
print(p1)
print(p1.name)
print(p1.color)
    
# 객체 여러 개 불러오자
with open('objects.bin', 'rb') as f:
    people = pickle.load(f)
# print(people)     #[<person.Person object at 0x000024B9
# print(people[0])
# print(people[1])
for person in people:
    print(person)