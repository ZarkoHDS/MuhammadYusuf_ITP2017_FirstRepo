age=18
message="happy "+ str(age) +" years old Birthday"
print(message)

family=["mom","dad","sister","brother","me"]
print(family[0],'\n'+family[1])
family.append('older sister')
print(family)
family.insert(2, "new sister")
print(family)
del family[1]
print(family)
family.remove('older sister')
print(family)

people= ["adrian", "kirsa", "hely"]
for i in range(0, 3):
    message="hey "+ people[i].title() +" ,you have been invited"
    print(message)

data=['A', 'C', 'B', 'E', 'D']
print(len(data))
print(sorted(data))



