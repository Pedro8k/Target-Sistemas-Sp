def inverte_string(palavra):
    # Forma 1:
    print(palavra, " invertido é: ", palavra[::-1])
    # return palavra[::-1]

    # Forma 2:
    resultado = []
    for letra in palavra:
        resultado.insert(0, letra )
    palavra_invertida = ''.join(resultado)
    print(palavra_invertida)
    return palavra_invertida

inverte_string("azul")
inverte_string("Pedro")
inverte_string("amora")