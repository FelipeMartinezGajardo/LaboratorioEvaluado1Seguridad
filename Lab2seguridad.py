#Laboratorio 2 Evaluado Seguridad informatica
#Felipe Martinez Gajardo - Marcelo Villalba Lerdo de Tejada

Todo = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789|°¬!#$%&/()='?\¡¿´¨+*~[]{}^`@-_<>,.;: "

ABC = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"      #Abecedario para lograr el ROT 5 para 
abc = "abcdefghijklmnñopqrstuvwxyz"      #encriptar y para descifrar.
Numeros = "0123456789"
Caracteres = "|°¬!#$%&/()='?\¡¿´¨+*~[]{}^`@-_<>,.;:"

atbash1= "ABCDEFGHIJKLMNÑOPQRSTUVWXYZabcdefghijklmnñopqrstuvwxyz0123456789|°¬!#$%&/()='?\¡¿´¨+*~[]{}^`@-_<>,.;:"
atbash2 = ":;.,><_-@`^}{][~*+¨´¿¡\?'=)(/&%$#!¬°|9876543210zyxwvutsrqpoñnmlkjihgfedcbaZYXWVUTSRQPOÑNMLKJIHGFEDCBA"
#variables las cuales son el diccionario para cuando se quiera realizar el método
#ATBASH
Hash1 = 0
aux = " "
MensajeSeguro = []
MensajeDeco = []
import hashlib as hl

def encriptar(Mensaje):     #Función para encriptar el mensaje que será
    Seguro=[]               #ingresado por el usuario.
    
    for ix in Mensaje:      #For que recorre cada letra del mensaje ingresado
        if ix == ' ':       #En caso de que exista un espacio, agrega el espacio
            Seguro.append(" ")  #y continua con la siguiente letra.
        else:
            if ix in abc:   #Al encontrar una letra, aplica el método de ROT 5
                cambio = "".join([abc[(abc.find(ix)+5)%27]])
                Seguro.append(cambio)
            elif ix in ABC:
                cambio = "".join([ABC[(ABC.find(ix)+5)%27]])
                Seguro.append(cambio)
            elif ix in Numeros:
                cambio = "".join([Numeros[(Numeros.find(ix)+5)%10]])
                Seguro.append(cambio)
            elif ix in Caracteres:
                cambio = "".join([Caracteres[(Caracteres.find(ix)+5)%37]])
                Seguro.append(cambio)
                
    SeguroAux = "".join(Seguro) #Una vez terminado el método ROT, pasa a realizar 
    Seguro2 = []                #el método ATBASH
    
    for ix in SeguroAux:
        if ix == " ":           #Al igual que en ROT 5, si ve un espacio, lo agrega
            Seguro2.append(" ") #y sigue con la siguiente letra.
        else:
            if ix in atbash1:   #En caso de que la letra esté dentro del diccionario 
                Posicion = atbash1.find(ix) #de Atbash1, guarda la posición que este
                Letra = atbash2[Posicion]   #se encuentra, y finalmente lo reemplaza
                Seguro2.append(Letra)       #con el diccionario de Atbash2.
            else:
                pass
            
    Mseguro =''.join(Seguro2)
    MensajeSeguro.append(Mseguro)
    Salida = open("Mensajeseguro.txt","w")  #Comando para crear un .txt con el mensaje
    Mensaje_Seguro_Real = MensajeSeguro[0]  #ya asegurado.
    Salida.write(Mensaje_Seguro_Real)
    Salida.close()
    print("------------------")
    print("Mensaje codificado")
    
def descifrar(MensajeSeguro):       #Función para descifrar el mensaje que fue 
                                    #encriptado
    Seguro_aux = open("Mensajeseguro.txt", "r") #Esta función trabaja directamente   
    Deco = []                                   #con el archivo .txt del
    Deco2 = []                                  #mensaje cifrado, por lo que
    MensajeDeco = []                            #si se modifica el archivo .txt
    auxcito = Seguro_aux.readline().replace('\n','')    #el programa se dará cuenta.
    
    for ix in auxcito:              #For el cual empezará a realizar el Atbash primero,
        if ix == " ":               #ya que para encriptar, el Atbash fue lo último que se
            Deco.append(" ")        #realizó.
        else:
            if ix in atbash2:
                Posicion = atbash2.find(ix) #Sigue la misma lógica que el Atbash
                Letra = atbash1[Posicion]   #utilizado en la función de encriptar.
                Deco.append(Letra)
            else:
                pass
            
    DecoAux = "".join(Deco)
    
    for ix in DecoAux:                      #Una vez realizado esto, se procede 
        if ix == ' ':                       #a realizar ROT -5, para así, obtener 
            Deco2.append(" ")               #el mensaje original que ingresó el
        else:                               #usuario. 
            if ix in ABC:                   #El criterio de este ROT es igual al que se 
                cambio = "".join([ABC[(ABC.find(ix)-5)%27]]) #utilizó en la función 
                Deco2.append(cambio)        #encriptar, pero con la diferencia de que
            elif ix in abc:                 #se reemplaza por 5 letras anteriores.
                cambio = "".join([abc[(abc.find(ix)-5)%27]])
                Deco2.append(cambio)
            elif ix in Numeros:
                cambio = "".join([Numeros[(Numeros.find(ix)-5)%10]])
                Deco2.append(cambio)
            elif ix in Caracteres:
                cambio = "".join([Caracteres[(Caracteres.find(ix)-5)%37]])
                Deco2.append(cambio)
          
    Mensaje2 = ''.join(Deco2)
    MensajeDeco.append(Mensaje2)
    MensajeDecodificado = MensajeDeco[0]
    HashD = hl.sha1(MensajeDecodificado.encode())    #Una vez se descifra el mensaje, se
    Hash2 = HashD.hexdigest()                        #genera un Hash para comparar los resultados
                                                     #y analizar si fue modificado el mensaje seguro o no.    
    print("------------------")
    print("El mensaje seguro fue descifrado y el Hash de este es: ", Hash2)
    
    if Hash1 == Hash2:
        print("Su mensaje es seguro")
        print("------------------")
    else:
        print("Alerta, su mensaje fue alterado")
        print("------------------")
            

Boton = True
while Boton:    #While que estaría representando el Main del programa.
    Mensaje = input("Ingrese el mensaje que quiera codificar: (algunos carácteres especiales no se podrán utilizar, como por ejemplo el uso de tildes): ")
    contador = 0
    for ix in range(len(Mensaje)):  #For el cual analiza si los carácteres están permitidos.
    
        if Mensaje[ix] not in Todo:
            print("El caracter ", Mensaje[ix], "no está permitido.")
            contador = 1
            
    if contador == 1:
        Boton = True
    
    elif len(Mensaje) == 0:
        print("Debe ingresar un mensaje.")
        Boton = True
    
    else:
        Entrada = open("mensajedeentrada.txt",'w')
        Entrada.write(Mensaje)
        Entrada.close()
        Boton = False

Boton2 = True
while Boton2:   #While el cual representaría el menu de lo que se quiera realizar una vez
                #ingresado el mensaje de manera correcta.
    try:
        Pregunta = int(input("¿Qué desea hacer? \n(1) Codificar \n(2) Decodificar \n(3) Cerrar el programa \n Opción: "))
    except:
        print("Ingrese una opción válida")
        Pregunta = 0
    if Pregunta == 1:       #En caso de que quiere encriptar, se genera un Hash del mensaje
        HashE = hl.sha1(Mensaje.encode()) #ingresado. La idea de esto, es que al momento de descifrar el mensaje seguro
        Hash1 = HashE.hexdigest()   #este tiene que ser igual al mensaje original ingresado por el usuario. Esto
        encriptar(Mensaje)          #se debe a que cada palabra/oración/letra/etc, tienen un Hash único. Mediante
        print("El Hash del mensaje original es: ", Hash1)
        print("------------------")
        Boton2                      #este método, se podrá analizar si el mensaje fue alterado o no.
    elif Pregunta == 2:
        try:
            if Hash1 == 0:
                print("No existe un mensaje el cual decodificar")
                print("------------------")
                Boton2
            else:
                descifrar(MensajeSeguro)
                Boton2
        except:
            print("No existe un mensaje el cual decodificar")
            print("------------------")
            Boton2
    elif Pregunta == 3:
        print("Adiós")
        Boton2 = False
    else:
        Boton2