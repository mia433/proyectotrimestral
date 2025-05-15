import sqlite3


def agregar_libro():
    
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    genero = input("Ingrese el género del libro: ")
    año_publicacion = int(input("Ingrese el año de publicación del libro: "))
    cursor.execute('''
        INSERT INTO libros (titulo, autor, genero, año_publicacion)
        VALUES (?, ?, ?, ?)
    ''', (titulo, autor, genero, año_publicacion))
    conn.commit()
    conn.close()
    print("Libro agregado correctamente.")
    def mostrar_libros():
       sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM libros")
    libros = cursor.fetchall()
    conn.close()
    if libros:
        print("Libros en la base de datos:")
        for libro in libros:
            print(f"ID: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}, Género: {libro[3]}, Año: {libro[4]}")
    else:
        print("No hay libros en la base de datos.")
        def eliminar_libro():
   
          sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    id_libro = int(input("Ingrese el ID del libro a eliminar: "))
    cursor.execute("DELETE FROM libros WHERE id = ?", (id_libro,))
    conn.commit()
    conn.close()
    print("Libro eliminado correctamente.")

def buscar_libro():
    """Busca un libro en la base de datos por su título."""
    conn = sqlite3.connect('biblioteca.db')
    cursor = conn.cursor()
    titulo = input("Ingrese el título del libro a buscar: ")
    cursor.execute("SELECT * FROM libros WHERE titulo LIKE ?", ('%' + titulo + '%',))
    libro = cursor.fetchone()
    conn.close()
    if libro:
        print(f"ID: {libro[0]}, Título: {libro[1]}, Autor: {libro[2]}, Género: {libro[3]}, Año: {libro[4]}")
    else:
        print("No se encontró el libro.")

def main():
    crear_base_de_datos() # type: ignore
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar un nuevo libro")
        print("2. Mostrar los libros existentes")
        print("3. Eliminar un libro")
        print("4. Buscar un libro")
        print("5. Salir")

        opcion = input("Ingrese una opción: ")

        match opcion:
            case "1":
                agregar_libro()
            case "2":
                mostrar_libros() # type: ignore
            case "3":
                eliminar_libro() # type: ignore
            case "4":
                buscar_libro()
            case "5":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción inválida.")

if __name__ == "_main_":
    main()