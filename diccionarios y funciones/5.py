# Crear una función que reciba una cadena de texto y devuelva un diccionario 
# con la cantidad de veces que aparece cada letra en la cadena.

texto = '''
¿Te imaginas llegar a casa un día y encontrar una caja gigante delante de la puerta, con tu nombre bien visible? Eso fue lo que le pasó a Lucas. La caja que encontró era tan grande que no podía ver encima de ella.

Como sus papás no estaban, Lucas llamó a su abuela Susana para que le ayudara a abrir aquella caja.

—Abuela, ¿qué crees que haya dentro de esta caja? —preguntó Lucas emocionado.

—No lo sé, pero descubrirlo juntos será una aventura divertida —respondió la abuela Susana, con una gran sonrisa.

Juntos, abrieron la caja gigante y encontraron una caja más pequeña dentro de ella. Al abrirla, hallaron una llave dorada con un mensaje que decía: "La llave de la felicidad está en tu corazón".

—¡Wow! ¡Mira esto, abuela! ¿Qué crees que significa? —preguntó Lucas.

—Significa que la verdadera felicidad no está en las cosas materiales, sino en nuestro interior. Y esta llave es un recordatorio de eso —respondió Susana sabiamente.

Lucas y su abuela no sabían qué hacer con la llave, pero decidieron guardarla y esperar a que algo sucediera.

Un día, Lucas se sentía muy triste porque sus papás no podían asistir a su recital de música en la escuela. Susana le recordó que la llave de la felicidad está en su corazón y le sugirió que hiciera algo especial para sentirse mejor.

—¿Qué puedo hacer, abuela? —preguntó Lucas tristemente.

—Podrías escribir una canción y ensayarla conmigo. Cantar juntos siempre nos hace felices —sugirió Susana.

Lucas siguió el consejo de su abuela y escribió una canción sobre su amor por la música y su familia. Juntos, ensayaron la canción y la presentaron en el recital de música.

Fue todo un éxito, y Lucas se sintió muy feliz al escuchar los aplausos del público.

Otro día, la abuela Susana recibió una carta de una amiga muy querida que vivía en el extranjero. En la carta, su amiga le contó que estaba muy enferma y que le gustaría verla.

—Lucas, ¿me acompañarías a visitar a mi amiga Laura? Te encantará conocerla, es la persona más alegre que he conocido jamás —dijo Susana tristemente.

—Por supuesto, abuela —respondió Lucas—. Y me llevo la llave, por si acaso.

Juntos hicieron el viaje. Cuando llegaron, encontraron a Laura muy triste.

—No sé qué hacer para sentirme mejor —dijo Laura.

LEl secreto de la caja mágicaa abuela Susana no se lo podía creer. Su amiga Laura siempre había sido muy dicharachera y divertida.

—No te preocupes, Laura, tenemos la llave de la felicidad. Juntos podemos hacer algo especial para sentirnos mejor —dijo Lucas con una sonrisa.

Lucas les mostró la llave dorada y les explicó el mensaje que encontraron en la caja. Juntos, decidieron cantar la canción que Lucas escribió. La música y las risas llenaron la habitación y todos se sintieron más felices.

Después de su visita, Lucas y Susana regresaron a casa. Lucas se dio cuenta de que la llave dorada había desaparecido y se preocupó mucho. Sin embargo, su abuela le recordó que la llave de la felicidad está en su corazón y que siempre podrán hacer algo especial para sentirse mejor.

La llave mágica no desapareció nunca del corazón de Lucas. Y siempre que lo necesita, brilla para recordarle que, a pesar de todo, siempre hay algún motivo para ser feliz.
'''

lista_de_letras = set()
diccionario_de_salida = {}

def generar_lista_de_letras(texto, lista_de_letras, diccionario_de_salida):
    
    # genero la lista de letras
    for valor in texto:
        lista_de_letras.add(valor)
    
    
    lista_de_letras = list(lista_de_letras) 
    
        
    #itero la lista de letras y cuento cuantas veces aparece cada una en el texto    
    for i in range(len(lista_de_letras)):
        letra_actual = lista_de_letras[i]
        contador = 0
        
        for valor in texto:
            if letra_actual == valor:
                contador +=1
        diccionario_de_salida.update({ letra_actual : contador  })
    
    
          
        
    

generar_lista_de_letras(texto, lista_de_letras, diccionario_de_salida)
print(diccionario_de_salida)
