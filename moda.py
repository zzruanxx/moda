def preenche(valores)
    for ind in range(len(valores)):
        valores[ind] = int(input(f"Elemento[{ind}] = "))
        return None
        
def buscaModa(valores):
    auxiliar = [0] * len(valores)
    
for indice in range(len(valores)):
    auxiliar[indice] = 1
    for varre in range(indice + 1, len(valores)):
        if valores[varre] == valores[indice]:
            auxiliar[indice] += 1
            
ondeMOda = 0 
for i in range(1, len(auxiliar)):
    if auxiliar[i] > auxiliar[ondeModa]:
        ondeModa = i
        
return valores[ondeModa]        

numeros = [0] * 10
preenche(numeros)
moda = buscaModa(numeros)
print(f"A moda do vetor e: {moda}")