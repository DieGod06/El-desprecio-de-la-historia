import random

#creación clases

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

class Cliente:
    def __init__(self, preciomin, preciomax):
        self.preciomin = preciomin
        self.preciomax = preciomax

#determinar los 20 productos

productos = [
    Producto("Violin", 300),
    Producto("Computador", 600),
    Producto("Reloj", 200),
    Producto("Cámara Polaroid", 400),
    Producto("Bicicleta", 250),
    Producto("Audífonos", 150),
    Producto("Smartphone", 500),
    Producto("Lentes", 100),
    Producto("Tablet", 300),
    Producto("Teclado", 100),
    Producto("Zapatos", 80),
    Producto("Libro", 30),
    Producto("Consola de juegos", 350),
    Producto("Balón de futbol", 70),
    Producto("Patineta", 150),
    Producto("Joyería", 1000),
    Producto("Micrófono", 180),
    Producto("Bolso de mano", 200),
    Producto("Cadena antigua", 900),
    Producto("Jarrón", 70),
]

#simulación de la tienda

def simulación_tienda():
    productos_disponibles = random.sample(productos, 5)
    print("Artículos disponibles en El desprecio de la Historia:")
    for producto in productos_disponibles:
        print (f"{producto.nombre}: ${producto.precio}")

    clientes = [Cliente(random.randint(50, 100), random.randint(400, 1000)) for _ in range (10)]

    for cliente in clientes:
        print("\nUn cliente entra en la casa de empeños 'El desprecio de la Historia'.")
        producto_comprar = random.choice(productos_disponibles)
        print(f"El cliente está interesado en {producto_comprar.nombre}.")
        oferta = int(input("Ingresa el precio establecido del objeto: "))
        while True:
            if oferta < cliente.preciomin:
                print("El cliente rechaza la oferta pero quiere regatear.")
                oferta = int(input(f"Ingresa otra oferta para {producto_comprar.nombre}: "))
            elif oferta > cliente.preciomax:
                print("El cliente sale corriendo de la tienda")
                break
            else:
                print("El cliente acepta la oferta y compra el objeto")
                break

simulación_tienda()
