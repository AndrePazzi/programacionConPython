import os
from objects.product import Product
from modules import sortingModule

os.system('cls' if os.name == 'nt' else 'clear')

productLoop = True
userChoice = 0

products = []

tempProduct1 = Product("Girasol", "Plantas", 35.00, 12, 145)
tempProduct2 = Product("Taza de ceramica", "Vasos", 18.50, 45, 320)
tempProduct3 = Product("Latte de Vainilla", "Bebidas", 6.25, 0, 1450)
tempProduct4 = Product("Trebol", "Plantas", 65.00, 0, 52)
tempProduct5 = Product("Mezcla de Cafe", "Bebidas", 16.00, 28, 210)
tempProduct6 = Product("Hamaca", "Decoracion", 22.00, 15, 85)
tempProduct7 = Product("Envase de Matcha", "Vasos", 24.00, 0, 115)

products.append(tempProduct1)
products.append(tempProduct2)
products.append(tempProduct3)
products.append(tempProduct4)
products.append(tempProduct5)
products.append(tempProduct6)
products.append(tempProduct7)

def addProduct():
    name = input("Ingrese el nombre del producto: ")
    category = input("Ingrese la categoria del producto: ")
    price = float(input("Ingrese el precio del producto: "))
    stock = int(input("Ingrese la cantidad de inventario del producto: "))
    sales = int(input("Ingrese la cantidad de ventas del producto: "))
    newProduct = Product(name, category, price, stock, sales)
    products.append(newProduct)
    os.system('cls' if os.name == 'nt' else 'clear')
    print (f"{name} se ha registrado correctamente\n")

def showProducts(productList):
    for obj in productList:
        print (f"Producto: {obj.name}\tCategoria: {obj.category}\nPrecio: ${obj.price}\t\tInventario: {obj.stock}\nVentas: {obj.sales}\t\tValor total en inventario: {(obj.price * obj.stock)}\n")

def secondMenu():
    secondLoop = True
    secondChoice = 0

    while (secondLoop):
        print ("\nEscoger una opcion:\n")
        try:
            secondChoice = int(input("[1] - Ver productos\t[2] - Ordenar por precio\t[3] - Ordenar por ventas\n[4] - Mostrar productos agotados\t\t\t\t[9] - Salir\n"))
            os.system('cls' if os.name == 'nt' else 'clear')
            match secondChoice:
                case 1:
                    showProducts(products)
                case 2:
                    priceProducts = sortingModule.sortPrice(products)
                    showProducts(priceProducts)
                case 3:
                    salesProducts = sortingModule.sortSales(products)
                    showProducts(salesProducts)
                    print (f"{salesProducts[-1]} es el producto mas vendido")
                case 4:
                    outOfStockProducts = sortingModule.showOutOfStock(products)
                    showProducts(outOfStockProducts)
                case 9:
                    secondLoop = False
                case _:
                    print (f"\nEl numero {secondChoice} no esta disponible.\n")
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\nError: Favor de ingresar un numero.\n")

def thirdMenu():
    thirdLoop = True
    thirdChoice = 0

    while (thirdLoop):
        print ("\nEscoger una opcion:\n")
        try:
            thirdChoice = int(input("[1] - Buscar por nombre\t\t[2] - Buscar por categoria\t\t[9] - Salir\n"))
            os.system('cls' if os.name == 'nt' else 'clear')
            match thirdChoice:
                case 1:
                    foundObject = sortingModule.searchName(products)
                    print ("\n")
                    if foundObject:
                        print (f"Producto: {foundObject.name}\tCategoria: {foundObject.category}\nPrecio: ${foundObject.price}\t\tInventario: {foundObject.stock}\nVentas: {foundObject.sales}\t\tValor total en inventario: {(foundObject.price * foundObject.stock)}\n")
                case 2:
                    foundList = sortingModule.searchCategory(products)
                    print ("\n")
                    showProducts(foundList)
                case 9:
                    thirdLoop = False
                case _:
                    print (f"\nEl numero {thirdChoice} no esta disponible.\n")
        except ValueError:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"\nError: Favor de ingresar un numero.\n")

while (productLoop):
    print ("===Sistema Inteligente de Inventario===\nEscoger una opcion:\n")
    try:
        userChoice = int(input("[1] - Registrar producto\t[2] - Mostrar productos\t\t[3] - Busqueda\t\t[9] - Salir\n"))
        os.system('cls' if os.name == 'nt' else 'clear')
        match userChoice:
            case 1:
                addProduct()
            case 2:
                secondMenu()
            case 3:
                thirdMenu()
            case 9:
                productLoop = False
            case _:
                print (f"\nEl numero {userChoice} no esta disponible.\n")
    except ValueError:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"\nError: Favor de ingresar un numero.\n")