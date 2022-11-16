dicc = {'Mikel': 3, 'Ane': 8, 'Amaia': 12, 'Unai': 5, 'Jon': 8, 'Ainhoa': 7, 
'Maite': 5}
dicc2={}
lista=[]
for i,o in dicc.items():
    dicc2.update({o:o})
for u in dicc2:
    lista.append(dicc2[u])
print(lista)