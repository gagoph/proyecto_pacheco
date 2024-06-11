import pickle

libros = []

def agregar_libro_bin(titulo, autor, isbn, categoria, estado):
    nuevo_libro = [titulo, autor, isbn, categoria, estado]
    libros.append(nuevo_libro)
    with open('datos.bin', 'wb') as file:
        pickle.dump(libros, file)

agregar_libro_bin("Cien años de soledad", "Gabriel García Márquez", "9780307474728", "Ficción", "Disponible")
agregar_libro_bin("El principito", "Antoine de Saint-Exupéry", "9780156013925", "Literatura infantil", "Disponible")
agregar_libro_bin("1984", "George Orwell", "9780451524935", "Ficción", "Disponible")
agregar_libro_bin("Orgullo y prejuicio", "Jane Austen", "9780141439518", "Clásicos", "Disponible")
agregar_libro_bin("Crónica de una muerte anunciada", "Gabriel García Márquez", "9781400034956", "Ficción", "Disponible")
agregar_libro_bin("El Gran Gatsby", "F. Scott Fitzgerald", "9780743273565", "Clásicos", "Disponible")
agregar_libro_bin("Don Quijote de la Mancha", "Miguel de Cervantes", "9788424118257", "Clásicos", "Disponible")
agregar_libro_bin("Harry Potter y la piedra filosofal", "J.K. Rowling", "9788478886556", "Fantasía", "Disponible")
agregar_libro_bin("Los miserables", "Victor Hugo", "9788491050062", "Clásicos", "Disponible")
agregar_libro_bin("La sombra del viento", "Carlos Ruiz Zafón", "9788408079545", "Misterio", "Disponible")


usuarios = []

def agregar_usuario_bin(usuario, ci, prestamos):
    nuevo_usuario = [usuario, ci, prestamos]
    usuarios.append(nuevo_usuario)
    with open('usuarios.bin', 'wb') as file:
        pickle.dump(usuarios, file)

agregar_usuario_bin("hgago.24", "31065384", [])
agregar_usuario_bin("crojas.24", "01234567", [])
agregar_usuario_bin("slibertella.24", "12345678", [])
agregar_usuario_bin("drodriguez.24", "23456789", [])
