class Juego:
    def __init__(self, nombre_jugador):
      
        self.nombre_jugador = nombre_jugador
        self.jugando = False

    def iniciar_juego(self):
        self.jugando = True
        print(f"\n¡Bienvenido al juego, {self.nombre_jugador}!")
        print("El juego ha comenzado..")
        self.jueguito()
        self.jueguito2()


        print("¡Gracias por jugar!\n")

    def salir(self):
        print(f"\nHasta luego, {self.nombre_jugador}. ¡Vuelve pronto!")


  
    
    def jueguito(self):
        lista=[] 
        for i in range (7):
            x=int(input("digite varios numeros ")) 
            lista.insert(i,x)
            i+=1
            print(lista)

        valor=True
        while valor:
            for index in range(len(lista)-1):
                
                if lista[index] > lista[index + 1]:
                    apartado=lista[index]
                    lista[index] = lista[index + 1] 
                    lista[index + 1] = apartado
            
                    print(lista)
                    break
            


    def jueguito2(self):
        mensaje = input("digite el mensaje ")
        mensaje = mensaje.lower()
        clave=1
        cifrado= ""
        letra=""
        abecederaio=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

        for index in mensaje:
          
            if index in abecederaio:
                #letra = abecederaio
                num = abecederaio.index(index)
                letra = letra + abecederaio[num+clave]
                cifrado = letra
                print(cifrado)

