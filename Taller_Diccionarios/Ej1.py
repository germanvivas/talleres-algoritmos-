lista=[12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64,23] 
dicc={}
for i in lista:
    dicc.update({i:0})
for o in lista:
    dicc.update({o:dicc.get(o)+1})
print(dicc)