
personas= []


def menu():
    while True:
        print("=================================================================")
        print("Menu de Opciones:")
        print("1. Grabar")
        print("2. Buscar por DNI")
        print("3. Imprimir certificados")
        print("4. Eliminar")
        print("5. Salir")

        opcion = input("Ingrese una opcion: ")
        

        if opcion == "1":
            opciones()
           
        elif opcion == "2":
            buscar_por_dni()
        elif opcion == "3":
            imprimir_certificados()
        elif opcion == "4":
            eliminar()
        elif opcion == "5":
            print("Programado por KEVIN ZAPATA DAVILA\nVersion 3.11.3")
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")


def opciones():
    while True:
        def verificar_rut(rut):
            rut = rut.replace("-","")
            rut, digito_verificador = rut[:-1], rut[-1]  
                    
            suma = 0
            mul = 2
            for i in reversed(rut):
                suma += int(i) * mul
                mul = (mul + 1) % 8 or 2

            resultado = (11 - suma % 11) % 11
            digito_verificador_calculado = "K" if resultado == 10 else str(resultado)

            return digito_verificador == digito_verificador_calculado

        print("=================BIENVENIDOS A RENAPER*===================")
        print("*VALIDAREMOS DNI*")
        print("=================================================================")


        rut = input("Ingrese el DNI: ")
        if verificar_rut(rut):
            print("DNI válido.")
            nombre = input("Ingrese el nombre: ")
            edad = str(input("Ingrese la edad: "))
            pais_nacimiento = input("Ingrese el país de nacimiento: ")
            ciudad_nacimiento = input("Ingrese la ciudad de nacimiento: ")
            print("=================================================================")
            persona = {
                "RUT": rut,
                "Nombre": nombre,
                "Edad": edad,
                "PN": pais_nacimiento,
                "CN": ciudad_nacimiento
            }
            personas.append(persona)
            print("Datos grabados correctamente.")
            break
                    
        else:
            print("DNI Invalido.")

def buscar_por_dni():
    rut_buscar = input("Ingrese el RUT a buscar: ")

    for persona in personas:
        if persona["RUT"] == rut_buscar:
            print("=================================================================")
            print("Información de la persona:")
            print("RUT:", persona["RUT"])
            print("Nombre:", persona["Nombre"])
            print("Edad:", persona["Edad"])
            print("Pais de nacimiento:", persona["PN"])
            print("Ciudad de nacimiento:", persona["CN"])

            if persona["PN"].lower() == "argentina":
                print("La persona pertenece al país de Argentina.")
            else:
                print("La persona no pertenece al país de Argentina.")

            return

    print("No se encontró ninguna persona con ese DNI.")

def imprimir_certificados():
    if len(personas) == 0:
        print("No hay personas registradas.")
        return

    estado_civil = input("Ingrese su Estado Civil: ")
    hijos = input("Cuantos Hijos tiene: ")

    rut_persona = input("Ingrese el DNI de la persona: ")

    for persona in personas:
        if persona["RUT"] == rut_persona:
            print("=================================================================")
            print("Certificado:")
            print("Estado Civil :", estado_civil)
            print("DNI de la persona:", persona["RUT"])
            print("Nombre de la persona:", persona["Nombre"])
            print("Edad:", persona["Edad"])
            print("Hijos:", hijos)


            return

    print("No se encontró ninguna persona con ese DNI.")

def eliminar():
    rut_eliminar = input("Ingrese el DNI de la persona a eliminar: ")

    for persona in personas:
        if persona["RUT"] == rut_eliminar:
            personas.remove(persona)
            print("Persona eliminada correctamente.")
            return

    print("No se encontró ninguna persona con ese DNI.")

menu()

