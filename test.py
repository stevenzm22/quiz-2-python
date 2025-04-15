"""
lista = [ 1, 3, 2, 4 ]

temp = lista[1]
lista[1] = lista[2]
lista[2] = temp
print(lista)

"""

"""
lista=[] 
for i in range (7):
    x=int(input("dijite varios numeros ")) 
    lista.insert(i,x)
    i+=1
print(lista)


 #lista=[10,9,44,3,12,20]

valor=True
while valor:
    for index in range(len(lista)-1):
        
        if lista[index] > lista[index + 1]:
            apartado=lista[index]
            lista[index] = lista[index + 1] 
            lista[index + 1] = apartado
       
            print(lista)
 """   
        





mensaje = input("digite el mensaje ")
mensaje = mensaje.lower()
clave=1
cifrado= ""
letra=""
abecederaio=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

for index in mensaje:
    print(index)
    if index in abecederaio:
        #letra = abecederaio
        num = abecederaio.index(index)
        letra = letra + abecederaio[num+clave]
        cifrado = letra
        print(cifrado)
      
  
        
        




























    """
    mensaje = input("Digite el mensaje: ")
clave = 1
abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

cifrado = ""
valor=True
while valor:
    for letra in mensaje.lower():
        if letra in abecedario:
            indice = abecedario.index(letra)
            nueva_pos = (indice + clave) % len(abecedario)
            cifrado += abecedario[nueva_pos]
        else:
            cifrado += letra
    valor =False
    print("Mensaje cifrado:", cifrado)
    """