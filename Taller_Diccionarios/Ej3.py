c=0
usuarios = {
        "iperurena": {
            "nombre": "Iñaki",
            "apellido": "Perurena",
            "password": "123123"
    },
        "fmuguruza": {
            "nombre": "Fermín",
            "apellido": "Muguruza",
            "password": "654321"
    },
        "aolaizola": {
            "nombre": "Aimar",
            "apellido": "Olaizola",
            "password": "123456"
    }
}
while c<4:
    
    User = input("Escriba su usuario: ")
    Pass = input("Escriba su password: ")
    if User in usuarios and Pass == usuarios[User]['password']:
        print("Acceso concedido")
        print(f"{usuarios.get(User).get('nombre')} {usuarios.get(User).get('apellido')}")
        quit()
    else:
        print(f"Intente nuevamente ({(3-c)} intento/s restantes)")
    c=c+1