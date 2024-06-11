import pickle
import numpy as np

with open('datos.bin', 'rb') as file:
    libros = pickle.load(file)

with open('usuarios.bin', 'rb') as file: 
    usuarios = pickle.load(file)

def agregar_libro(titulo, autor, isbn, categoria, estado):
    nuevo_libro = [titulo, autor, isbn, categoria, estado]
    libros.append(nuevo_libro)


def mostrar_libros():
    for libro in libros: 
        print(f"Nombre: {libro[0]}, Autor: {libro[1]}, ISBN: {libro[2]}, Categoria: {libro[3]}, Estado: {libro[4]}")
        print()


def prestamo(isbn, ci):
    usuario_encontrado = False
    libro_encontrado = False
    for usuario in usuarios: 
        if usuario[1] == ci: 
            usuario_encontrado = True
            for libro in libros: 
                if libro[2] == isbn:
                    if libro[4] == "Disponible": 
                        libro[4] = f"Prestado a {usuario[0]}"
                        usuario[2].append(libro[0])
                        libro_encontrado = True
                    else: 
                        print(f"El libro ya esta en prestamo.")
                else: 
                    continue          
    if usuario_encontrado: 
        if libro_encontrado: 
            print()
            print("Libro prestado exitosamente.")
        else: 
            print()
            print("El libro ingresado no existe.")
    else: 
        print("El usuario ingresado no existe.")

def devolucion(ci): 
    for usuario in usuarios:
        if usuario[1] == ci: 
            libros_prestados = usuario[2]
            print("Libros en prestamo: ")
            for libro_prestado in libros_prestados: 
                print(libro_prestado)
            print()
            libro_devolucion = input("Indique el titulo del libro que quiere devolver: ")
            for libro_prestado in libros_prestados:
                if libro_devolucion == libro_prestado: 
                    usuario[2].remove(libro_devolucion)
                    for libro in libros: 
                        if libro[0] == libro_devolucion:
                            libro[4] = "Disponible"
                    print("Libro devuelto exitosamente.")

def eliminar_libro(titulo):
    i = 0 
    libro_encontrado = False
    for libro in libros: 
        if libro[0] == titulo: 
            libros.pop(i)
            libro_encontrado = True
            for usuario in usuarios:
                prestamos = usuario[2]
                if titulo in prestamos: 
                    prestamos.remove(titulo)
        else: 
            i += 1
            continue
    if libro_encontrado: 
        print("Libro eliminado exitosamente.")
    else: 
        print("El libro ingresado no existe.")

def mostrar_usuarios(): 
    for usuario in usuarios: 
        print(f"Nombre: {usuario[0]}, Cedula: {usuario[1]}, Prestamos: {usuario[2]}")
        print()

def agregar_usuario(usuario, ci): 
    nuevo_usuario = [usuario, ci, []]
    usuarios.append(nuevo_usuario)

def eliminar_usuario(nombre): 
    i = 0 
    usuario_encontrado = False
    for usuario in usuarios: 
        if usuario[0] == nombre: 
            if usuario[2]: 
                for prestamo in usuario[2]:
                    for libro in libros: 
                        if libro[0] == prestamo: 
                            libro[4] = "Disponible"
            usuarios.pop(i)
            usuario_encontrado = True
        else: 
            i += 1
            continue
    if usuario_encontrado: 
        print("Usuario eliminado exitosamente.")
    else: 
        print("El usuario ingresado no existe.")


while True:
        print("**Menú principal**")
        print("1. Mostrar libros")
        print("2. Agregar libro nuevo")
        print("3. Dar libro en prestamo")
        print("4. Devolver libro en prestamo")  
        print("5. Buscar libro")
        print("6. Eliminar libro")
        print("7. Gestionar usuarios")
        print("8. Guardar cambios y salir")

        opcion = int(input("Ingrese la opción deseada: "))

        if opcion == 1:
            mostrar_libros()
        elif opcion == 2:
            titulo = input("Indique el titulo del libro que desea agregar: ")
            autor = input("Indique el autor del libro que desea agregar: ")
            isbn = input("Ingrese el ISBN del libro que desea agregar (Numero de 13 digitos): ")
            if isbn.isnumeric() and len(isbn)==13: 
                categoria = input("Ingrese la categoria del libro que desea agregar: ")
                estado = "Disponible"
                agregar_libro(titulo, autor, isbn, categoria, estado)
            else: 
                print("El ISBN debe ser un numero de 13 cifras.")
        elif opcion == 3:
            ci = input("Ingrese su cedula de identidad: ")
            if ci.isnumeric(): 
                mostrar_libros()
                isbn = input("Ingrese el ISBN del libro que desea prestar: ")
                if isbn.isnumeric() and len(isbn) == 13: 
                    prestamo(isbn, ci)
                else: 
                    print("El ISBN ingresado no es correcto.")
            else: 
                print("La cedula ingresada debe ser numerica.")
        elif opcion == 4:
            ci = input("Ingrese su cedula de identidad: ")
            if ci.isnumeric(): 
                devolucion(ci)
        elif opcion == 5:
            print("Opcion 5")
        elif opcion == 6:
            titulo = input("Ingrese el titulo del libro a eliminar: ")
            eliminar_libro(titulo)
        elif opcion == 7:
            while True: 
                print("1. Mostrar usuarios")
                print("2. Agregar usuario")
                print("3. Eliminar usuario")
                print("4. Regresar al menu principal")

                opcion = int(input("Ingrese la opcion deseada: "))
                if opcion == 1: 
                    mostrar_usuarios()
                elif opcion == 2: 
                    usuario = input("Ingrese el usuario del nuevo usuario: ")
                    ci = input("Ingrese cedula de identidad: ")
                    if  ci.isnumeric(): 
                        agregar_usuario(usuario, ci)
                    else: 
                        print("La cedula ingresada debe ser numerica.")
                elif opcion == 3: 
                    nombre = input("Indique el usuario que desea eliminar: ")
                    eliminar_usuario(nombre)
                elif opcion == 4: 
                    break
                else: 
                    print("Opcion no valida")

        elif opcion == 8: 
            with open('usuarios.bin', 'wb') as file: 
                pickle.dump(usuarios, file)
            with open('datos.bin', 'wb') as file:
                pickle.dump(libros, file)
            break
        else:
            print("Opción no válida")