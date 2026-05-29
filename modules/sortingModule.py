def sortPrice(products):
    for i in range (len(products)):
        smallest = i
        for j in range (i+1, len(products)):
            if products[j].price < products[smallest].price:
                smallest = j
        
        products[i], products[smallest] = products[smallest], products[i]
    return products

def sortSales(products):
    for i in range (len(products)):
        smallest = i
        for j in range (i+1, len(products)):
            if products[j].sales < products[smallest].sales:
                smallest = j
        
        products[i], products[smallest] = products[smallest], products[i]
    return products

def showOutOfStock(products):
    outOfStock = list(filter(lambda x: x.stock == 0, products))
    return outOfStock


def sortName(products):
    for i in range (len(products)):
        smallest = i
        for j in range (i+1, len(products)):
            if products[j].name < products[smallest].name:
                smallest = j
        
        products[i], products[smallest] = products[smallest], products[i]
    return products

def searchName(products):
    target = (input("Ingrese el nombre del producto a buscar: ")).lower()
    for product in products:
        if (product.name).lower() == target:
            return product
    print("No hay resultados")
    return []

def searchCategory(originalProducts):
    target = (input("Ingrese la categoria del producto a buscar: ")).lower()
    products = sortName(originalProducts)
    def findFirst():
        low, high = 0, len(products) - 1
        first_idx = -1
        while low <= high:
            mid = (low + high) // 2
            if (products[mid].category).lower() == target:
                first_idx = mid
                high = mid - 1
            elif (products[mid].category).lower() < target:
                low = mid + 1
            else:
                high = mid - 1
        return first_idx

    def findLast():
        low, high = 0, len(products) - 1
        last_idx = -1
        while low <= high:
            mid = (low + high) // 2
            if (products[mid].category).lower() == target:
                last_idx = mid
                low = mid + 1
            elif (products[mid].category).lower() < target:
                low = mid + 1
            else:
                high = mid - 1
        return last_idx

    first = findFirst()
    if first == -1:
        print("No hay resultados")
        return []
    
    last = findLast()
    return products[first : last + 1]