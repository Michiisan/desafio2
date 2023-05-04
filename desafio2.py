txt = input("Ingresa un caracter ")
#esMinuscula = txt.islower()
#esMayuscula = txt.isupper()
#esNumero = txt.isdigit()
#esLetra = txt.isalpha()

#print("Es minuscula", esMinuscula)
#print("Es mayuscula", esMayuscula)
#print("Es numero", esNumero)
#print("Es letra", esLetra)
# ctrol + } 

if (txt.isalpha()):
    if(txt.islower()):
        print("Es minuscula")
    else:
        print("Es mayuscula")
elif(txt.isdigit()):
    print("Es numero")
else:
    print("caracter especial") 