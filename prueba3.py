import csv
import json
lista_datos=[]
def procesar_estudiantes():
    with open("ListaCurso5B.csv", "r", newline= "") as archivo:
        datos_estudiantes= csv.DictReader(archivo)
        lista_datos= list(datos_estudiantes)
        for i in lista_datos:
            print(i)
        print(datos_estudiantes)

#procesar_estudiantes()

def registrar_estudiante():
    try:
        rut= int(input("Ingresa su numero de rut: \n"))
        nombre= input("Ingresa tu nombre: \n")
        nota1= float(input("Ingresa la nota 1: "))
        nota2= float(input("Ingresa la nota 2: "))
        datos = { "Rut": rut, "Nombre": nombre, "Nota 1":nota1, "Nota 2": nota2 }
        lista_datos.append(datos)
        if datos in lista_datos:
            print("Ha ingresado los datos correctamente")
        else:
            print("Tiene un error en los datos")
        print(lista_datos)

    except Exception as ex:
        print (f"Tienes un error de tipo {ex}")

def modificar_nota():
    rut= int(input("Para modificar nota ingresa su numero de rut: \n"))
    if rut in lista_datos:
        op= int(input("Que nota desea cambiar:1-Nota 1\n2-Nota 2\n3-No deseo modificar\n"))
        if op==1:
            nnota1= float(input("Ingrese la nueva nota por nota 1"))
            if nnota1==i:
                for i in lista_datos:
                    if i["Nota 1"] == nnota1:
                     print(nnota1)
                    else:
                        print("Ingrese un valor valido")
        if op==2:
            nnota2= float(input("Ingrese la nueva nota por nota 1"))
            for i in lista_datos:
                    if i["Nota 2"] == nnota2:
                     print(f"Su nueva nota es:{nnota2}")
                    else:
                        print("Ingrese un valor valido")
        if op==3:
            pass
def eliminar_estudiante():
    rut= int(input("Ingrese el rut del estudiante que desea eliminar \n"))
    if rut in  lista_datos:
        pass
    for i in lista_datos:
        if rut == i['Rut']:
            nombre = i['Nombre']
        print(f"Esta seguro de eliminar a {nombre}")
        
        
        
def generar_promedio_notas():
    pass
def generar_acta():
    with open("Acta_cierre_5B.csv","w", newline= " ")as file:
        actacierre = csv.DictWriter(file)  
        actacierre.writerow(lista_datos)
        
def salir():
    print("Saliendo del programa ")

while True:
    try:
        opcion= int(input("""Seleccione la accion que desea realizar:
                            1-Procesar lista de estudiantes.
                            2-Registrar estudiante.
                            3-Modificar nota
                            4-Eliminar estudiante.
                            5-Generar promedio de notas.
                            6-Generar acta de cierre de curso.
                            7-Salir\n"""))
        if opcion==1:
            procesar_estudiantes()
        elif opcion==2:
            registrar_estudiante()
        elif opcion==3:
            modificar_nota()
        elif opcion==4:
            eliminar_estudiante()
        elif opcion==5:
            pass
        elif opcion==6:
            pass
        elif opcion==7:
            salir()
            break
        else:
            print("Ingrese una opcion valida")
    
    

    except:
        print("Ingrese una opcion valida")