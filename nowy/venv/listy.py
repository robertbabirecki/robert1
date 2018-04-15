l1=[2,5,6,8,7,4,2,5,8]
l2=[2.3,2.5,2.8,5.8,8.8]
l3=['ble','bla','cos','ktos']
l4=['ble',1,2.3,'cos',1.2,4]
l5=['h']
print(l2)
print(l3)
print(l4)
l1.extend([2,100,50])
l1.sort()
l1.reverse()
l1.pop(2)
print(l1)

l2.extend([2.4,100.6,50.6])
l2.sort()
l2.reverse()
l2.pop(2)
print(l2)

l3.extend(['gdzies','tam','tu'])
l3.sort()
l3.reverse()
l3.pop(2)
print(l3)

l4.extend(['gdzies',5,'tu'])

l4.reverse()
l4.pop(2)
print(l4)