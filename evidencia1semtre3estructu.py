import tabulate 
#hola
diccionario1={}

def menu_principal():
    while True:
        print("*** MENU PRINCIPAL ***")
        print("ELIJA UNA OPCION")
        print("[1]. Agregar un nuevo registro")
        print("[2]. Consultar registros")
        print("[3]. Salir")
        respuesta = int(input("¿Cual es la opcion que desea?: "))
        if respuesta == 1:
            agregar_registro()
        elif respuesta == 2:
            sub_menu()
        elif respuesta == 3:
            print("Hasta luego")
            exit()
        else:
            print("Vuelva a escoger una opcion valida")

def agregar_registro():
    while True:
        continuar=input("¿desea agregar un nuevo ejemplar?[S/N]").upper()
        if continuar=="S":
            titulo=input("¿Ingrese el nombre del ejemplar?").upper()
            autor=input("cual el autor: ").upper()
            genero=input("Cual es el genero: ").upper()
            año=int(input("Cual es el año de publicacion: "))
            isbn=input("Cual es el isbn: ").upper()
            fecha_adquisicion=input("dime la fecha de adquisicion: ").upper() 


            if diccionario1:
                identificador=max(diccionario1) + 1
            else:
                identificador=1
                #diccionario principal donde se gurdaran los ejemplares que ingreso
                #el usuario
            diccionario1[identificador]={"titulo":titulo, "autor":autor, "genero":genero,"año":año, "isbn":isbn, "fecha":fecha_adquisicion}
            
        else:
            menu_principal()

def sub_menu():
    
    while True:
        print("*** MENU DE CONSULTAS ***")
        print("ELIJA UNA OPCION")
        print("[1]. Búsqueda de libro")
        print("[2]. Reporte")
        print("[3]. Volver al menu principal")
        respuesta = int(input("¿Cual es la opcion que desea?: "))
        if respuesta == 1:
            consultar_ejemplar()
        elif respuesta == 2:
            submenu_reporte()
        elif respuesta == 3:
            menu_principal()
        else:
            print("Opción inválida. Por favor, intente nuevamente")
                  

def consultar_ejemplar():
    print("Consultar los datos de un título")
    opcion = input("¿Cómo deseas buscar el título? (1. Título, 2. ISBN): ")
    if opcion == "1":
        reporte_total()
        titulo1 = input("Introduce el título: ")
        #lista para almacenar la busqueda
        # con la sentencia for recorre cada elemento del diccionario 'diccionario1
        #la variable "identificador" almacena la clave 
        #y "datos" se utiliza para almacenar el valor 
        #(es decir, el diccionario que contiene los datos del ejemplar).
        #La condición verifica si el valor del campo isbn del diccionario 
        #"datos" es igual al valor de la variable titulo1
        #si la condicion es verdadera se agrega el valor a la lista
        #y  al final esta lista se utiliza para imprimir los datos que el usuario busco
        encontrados = [identificador for identificador, datos in diccionario1.items() if datos['titulo'] == titulo1.upper()]
        if encontrados:
            print(f"Se encontraron {len(encontrados)} ejemplares con el título '{titulo1}':")
            for identificador in encontrados:
                datos = diccionario1[identificador]
                print(f"Identificador: {identificador}, título: {datos['titulo']}, autor: {datos['autor']}, genero: {datos['genero']}, año: {datos['año']}, isbn: {datos['isbn']}, fecha: {datos['fecha']}")
        else:
            print(f"No se encontraron ejemplares con el título '{titulo1}'")
            #print(diccionario1)
    elif opcion=="2":
        reporte_total()
        isbn1 = input("Introduce el isbn: ")
        #-----------------------
        #lista para almacenar la busqueda
        encontrados = [identificador for identificador, datos in diccionario1.items() if datos['isbn'] == isbn1.upper()]
        if encontrados:
            print(f"Se encontraron {len(encontrados)} ejemplares con el título '{isbn1}':")
            for identificador in encontrados:
                datos = diccionario1[identificador]
                print(f"Identificador: {identificador}, título: {datos['titulo']}, autor: {datos['autor']},genero: {datos['genero']}, año: {datos['año']}, isbn: {datos['isbn']}, fecha: {datos['fecha']}")
        else:
            print(f"No se encontraron ejemplares con el título '{isbn1}'")


def reporte():
    # Creamos una lista de autores únicos
    #
    autores = list(set([libro["autor"] for libro in diccionario1.values()]))

    # Imprimimos la lista de autores y pedimos que el usuario seleccione uno
    print("Autores disponibles:")
    for i, autor in enumerate(autores):
        print(f"{i+1}. {autor}")
    opcion_autor = int(input("Seleccione el número del autor: "))
    autor_seleccionado = autores[opcion_autor - 1]

    # Creamos la tabla de ejemplares del autor seleccionado
    tabla_ejemplares = []
    for identificador, libro in diccionario1.items():
        if libro["autor"] == autor_seleccionado:
            tabla_ejemplares.append([libro["titulo"], libro["genero"], libro["año"], libro["isbn"], libro["fecha"]])

    # IMPRIMIMOS la tabla de ejemplares
    longitudes_columnas = [max([len(str(ejemplar[i])) for ejemplar in tabla_ejemplares]+[len(header[i])]) for i, header in enumerate(["Título", "Género", "Año", "ISBN", "Fecha de adquisición"])]

    # IMPRIMIMOS la tabla de ejemplares
    print(f"Reporte para el autor '{autor_seleccionado}':")
    print("| Título" + " "*(longitudes_columnas[0]-6) + " | Género" + " "*(longitudes_columnas[1]-6) + " | Año" + " "*(longitudes_columnas[2]-4) + " | ISBN" + " "*(longitudes_columnas[3]-13) + " | Fecha de adquisición" + " "*(longitudes_columnas[4]-21) + " |")
    print("|" + "-"*(longitudes_columnas[0]+2) + "|" + "-"*(longitudes_columnas[1]+2) + "|" + "-"*(longitudes_columnas[2]+2) + "|" + "-"*(longitudes_columnas[3]+2) + "|" + "-"*(longitudes_columnas[4]+2) + "|")
    for ejemplar in tabla_ejemplares:
        print(f"| {ejemplar[0]:{longitudes_columnas[0]}} | {ejemplar[1]:{longitudes_columnas[1]}} | {ejemplar[2]:{longitudes_columnas[2]}} | {ejemplar[3]:{longitudes_columnas[3]}} | {ejemplar[4]:{longitudes_columnas[4]}} |")
        print("|" + "-"*(longitudes_columnas[0]+2) + "|" + "-"*(longitudes_columnas[1]+2) + "|" + "-"*(longitudes_columnas[2]+2) + "|" + "-"*(longitudes_columnas[3]+2) + "|" + "-"*(longitudes_columnas[4]+2) + "|")


def reporte_genero():
    # Creamos una lista de géneros únicos
    generos = list(set([libro["genero"] for libro in diccionario1.values()]))

    # Imprimimos la lista de géneros y pedimos que el usuario seleccione uno
    print("Géneros disponibles:")
    for i, genero in enumerate(generos):
        print(f"{i+1}. {genero}")
    opcion_genero = int(input("Seleccione el número del género: "))
    genero_seleccionado = generos[opcion_genero - 1]

    # Creamos la tabla de ejemplares del género seleccionado
    tabla_ejemplares = []
    for identificador, libro in diccionario1.items():
        if libro["genero"] == genero_seleccionado:
            tabla_ejemplares.append([libro["titulo"], libro["autor"], libro["año"], libro["isbn"], libro["fecha"]])

    # IMPRIMIMOS la tabla de ejemplares
    longitudes_columnas = [max([len(str(ejemplar[i])) for ejemplar in tabla_ejemplares]+[len(header[i])]) for i, header in enumerate(["Título", "Autor", "Año", "ISBN", "Fecha de adquisición"])]

    # IMPRIMIMOS la tabla de ejemplares
    print(f"Reporte para el género '{genero_seleccionado}':")
    print("| Título" + " "*(longitudes_columnas[0]-6) + " | Autor" + " "*(longitudes_columnas[1]-5) + " | Año" + " "*(longitudes_columnas[2]-4) + " | ISBN" + " "*(longitudes_columnas[3]-13) + " | Fecha de adquisición" + " "*(longitudes_columnas[4]-21) + " |")
    print("|" + "-"*(longitudes_columnas[0]+2) + "|" + "-"*(longitudes_columnas[1]+2) + "|" + "-"*(longitudes_columnas[2]+2) + "|" + "-"*(longitudes_columnas[3]+2) + "|" + "-"*(longitudes_columnas[4]+2) + "|")
    for ejemplar in tabla_ejemplares:
        print(f"| {ejemplar[0]:{longitudes_columnas[0]}} | {ejemplar[1]:{longitudes_columnas[1]}} | {ejemplar[2]:{longitudes_columnas[2]}} | {ejemplar[3]:{longitudes_columnas[3]}} | {ejemplar[4]:{longitudes_columnas[4]}} |")
        print("|" + "-"*(longitudes_columnas[0]+2) + "|" + "-"*(longitudes_columnas[1]+2) + "|" + "-"*(longitudes_columnas[2]+2) + "|" + "-"*(longitudes_columnas[3]+2) + "|" + "-"*(longitudes_columnas[4]+2) + "|")
            
def reporte_por_año():
    # Creamos una lista de años únicos
    años = list(set([libro["año"] for libro in diccionario1.values()]))

    # Imprimimos la lista de años y pedimos que el usuario seleccione uno
    print("Años disponibles:")
    for i, año in enumerate(años):
        print(f"{i+1}. {año}")
    opcion_año = int(input("Seleccione el número del año: "))
    año_seleccionado = años[opcion_año - 1]

    # Creamos la tabla de ejemplares del año seleccionado
    tabla_ejemplares = []
    for identificador, libro in diccionario1.items():
        if libro["año"] == año_seleccionado:
            tabla_ejemplares.append([libro["titulo"], libro["autor"], libro["genero"], libro["isbn"], libro["fecha"]])

    # IMPRIMIMOS la tabla de ejemplares
    longitudes_columnas = [max([len(str(ejemplar[i])) for ejemplar in tabla_ejemplares]+[len(header[i])]) for i, header in enumerate(["Título", "Autor", "Género", "ISBN", "Fecha de adquisición"])]

    # IMPRIMIMOS la tabla de ejemplares
    print(f"Reporte para el año '{año_seleccionado}':")
    print("| Título" + " "*(longitudes_columnas[0]-6) + " | Autor" + " "*(longitudes_columnas[1]-5) + " | Género" + " "*(longitudes_columnas[2]-6) + " | ISBN" + " "*(longitudes_columnas[3]-13) + " | Fecha de adquisición" + " "*(longitudes_columnas[4]-21) + " |")
    print("|" + "-"*(longitudes_columnas[0]+2) + "|" + "-"*(longitudes_columnas[1]+2) + "|" + "-"*(longitudes_columnas[2]+2) + "|" + "-"*(longitudes_columnas[3]+2) + "|" + "-"*(longitudes_columnas[4]+2) + "|")
    for ejemplar in tabla_ejemplares:
        print(f"| {ejemplar[0]:{longitudes_columnas[0]}} | {ejemplar[1]:{longitudes_columnas[1]}} | {ejemplar[2]:{longitudes_columnas[2]}} | {ejemplar[3]:{longitudes_columnas[3]}} | {ejemplar[4]:{longitudes_columnas[4]}} |")
        print("|" + "-"*(longitudes_columnas[0]+2) + "|" + "-"*(longitudes_columnas[1]+2) + "|" + "-"*(longitudes_columnas[2]+2) + "|" + "-"*(longitudes_columnas[3]+2) + "|" + "-"*(longitudes_columnas[4]+2) + "|")

def submenu_reporte():
    print("*** Menu de reportes ***")
    print("ELIJA UNA OPCION")
    print("[1]. Catalogo completo")
    print("[2]. Reporte por autor")
    print("[3]. Reporte por genero")
    print("[4]. Reporte por año de publicacion")
    print("[5]. Regresar al menu de consulta")
    respuesta = int(input("¿Cual es la opcion que desea?: "))
    if respuesta == 1:
        reporte_total()
    elif respuesta == 2:
        reporte()
    elif respuesta == 3:
        reporte_genero()
    elif respuesta == 4:
        reporte_por_año()
    elif respuesta == 5:
        sub_menu()
    else:
        print("Opción inválida. Por favor, intente nuevamente")

def reporte_total():
    # Crear una lista de listas a partir del diccionario
    data = [[key, value["titulo"], value["autor"], value["genero"], value["año"], value["isbn"], value["fecha"]] for key, value in diccionario1.items()]

# Mostrar la tabla utilizando tabulate
    headers = ["Identificador", "Título", "Autor", "Género", "Año", "ISBN", "Fecha de adquisición"]
    print(tabulate(data, headers=headers))


menu_principal()          
