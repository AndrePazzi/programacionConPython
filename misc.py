# 5. Corrige el siguiente programa: 
# numeros = [5,2,8,1 <--- Aqui hace falta cerrar el []
# ordenados = sorted(numeros) 

# Para corregir solo se tiene que cerrar correctamente
numerosSorted = [5,2,8,1]
ordenados = sorted(numerosSorted)

# 6. Completa Selection Sort. 
print ("\n===# 6. Completa Selection Sort.===")

numerosSelection = [7,4,2,9]

for i in range(len(numerosSelection)):
    smallest = i # Guarda la posicion actual
    for j in range(i+1, len(numerosSelection)):
        if numerosSelection[j] < numerosSelection[smallest]: # Revisa si el proximo numero es menor al guardado
            smallest = j # Guarda el proximo numero como el menor
    numerosSelection[i], numerosSelection[smallest] = numerosSelection[smallest], numerosSelection[i] # Intercambia el numero guardado con
                                                                                # la posicion actual en caso de haber encontrado uno menor

print(numerosSelection)

# 7. Crear una función usando *args que:
print ("\n===7. Crear una función usando *args que:===")

finalResult = []

def calcTotal(*itemsPurchased):
    itemSum = sum(itemsPurchased)
    itemTax = (itemSum * 0.16)
    itemTotal = (itemSum + itemTax)
    return itemSum, itemTax, itemTotal

finalResult = calcTotal(12.99, 15.99, 23.99)
print (f"Subtotal: ${finalResult[0]:.2f}\nImpuesto: ${finalResult[1]:.2f}\nTotal: ${finalResult[2]:.2f}")