from random import randint

def rand_word():
    words = ["tu vieja en cuatro", "duro dos horas", "claro p mascota", "hueles a poto"]
    rand_palabra = words[randint(0, len(words)) -1]
    return rand_palabra

def conv_palabra(rand):
    list_palabras = rand.split(" ")
    for i, palabra in enumerate(list_palabras):
        list_palabras[i] = "".join("_" for x in palabra)
    palabra_escondida = " ".join(list_palabras)
    return palabra_escondida

def linput(letras_antiguas):
    letra = input("ingresa la letra: ")
    
    if len(letra) > 1:
        print("solo una letra a la ves")
        linput(letras_antiguas)
    if letra in letras_antiguas:
        print(f"ya elegiste la letra {letra} intenta otra vez")
        linput(letras_antiguas)
    letras_antiguas.append(letra)
    return letra, letras_antiguas

def guion(palabra, guiones, letra_bus):
    indices = [indice for indice, x in enumerate(palabra) if x == letra_bus ]
    #print(f"{indices = }")
    guiones = list(guiones)
    guion = guiones[0]
    for x in indices:
        guiones[x] = letra_bus
    nuevo = "".join(guiones)     
    return nuevo

def main():
    turnos = 8
    solucionado = False
    rword = rand_word()
    letras_antiguas = []
    guiones = conv_palabra(rword)
    while (turnos != 0 and solucionado == False): 
        letras, letras_antiguas = linput(letras_antiguas)
        if letras in rword:
            guiones = guion(rword, guiones, letra_bus=letras)    
        else:
            turnos -= 1
        if guiones == rword:
            solucionado = True    
        print(guiones)
        print(f"te quedan {turnos} turnos")    
        print("---------------------")
    if solucionado:
        print("GANASTE!!!")
    else:
        print(f"la frase es: {rword}")
        print("PERDISTE!!!")

if __name__ == "__main__":
    main()

