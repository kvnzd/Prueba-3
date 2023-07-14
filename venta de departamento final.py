
import time
pisos = ['A', 'B', 'C', 'D']
departamentos = {}
compradores = []

valorf2=3800
valorg2=3200
valorh2=2800
valori2=3500


v6=0
v7=0
v8=0
v9=0
v10=0
print("***INMOBILIARIA CASA FELIZ***")

def menu():
    global v1,v2,v3,v4,v5
    while True:
        
        print('--- Menú ---')
        print('1. Mostrar departamentos disponibles')
        print('2. Comprar departamento')
        print('3. Ver Lista de Compradores')
        print('4. Mostrar ganancias totales')
        print('5. Salir')
        opcion = input('Ingrese una opción: ')

        if opcion == '1':
            mostrar_departamentos()
        elif opcion == '2':
            comprar_departamento()
        elif opcion == '3':
            ver_compradores()
        elif opcion == '4':
            mostrar_ganancias()

        elif opcion == '5':
            
            print("Kevin_Zapata_PGY1121_004_V")
            print (time.strftime("%d/%m/%y"))
            break
        else:
            print('Opción no válida. Por favor, ingrese una opción válida.')


for piso in range(1, 10):
    for letra in pisos:
        departamento = f'{letra}{piso}'
        departamentos[departamento] = 'Disponible'
        

def mostrar_departamentos():
    
    for piso in range(1, 10):
        for letra in pisos:
            
            departamento = f'{letra}{piso}'
            
            estado = departamentos[departamento]
            print(f'{departamento}: {estado}')
        print()

def comprar_departamento():
    ca = input(" *1* Para Continuar Compra: ")
    ca = ca.upper()
    if ca == '1':
        print("Valores de Departamento en Comprar")
        print("Tipo A 3.800UF\nTipo B 3.200UF\nTipo C 2.800UF\nTipo D 3.500UF")
        
        departamento = input('Ingrese el departamento que desea Comprar (por ejemplo, A1): ')
        departamento=departamento.upper()
        global v6,v7,v8,v9,v10
        if departamento in ["A1","A2","A3","A4","A5","A6","A7","A8","A9"]:
            
            
            
            print("Este departamento tiene como valor de Venta de 3.800UF")
            if departamento in departamentos:
                if departamentos[departamento] == 'Disponible':
                    departamentos[departamento] = 'X'
                    v6+=valorf2
                    
                    rut = input("Ingrese el RUT: ")
                    nombre = input("Ingrese el nombre: ")                
                    comprador = {
                    "rut": rut,
                    "nombre": nombre,
                    "d": departamento + ":Comprado"
                }
                    compradores.append(comprador)
                    print(f'Departamento {departamento} Comprado exitosamente.')
                                
                else:
                    print(f'El departamento {departamento} ya no esta Disponible.')
            else:
                print('Departamento no valido.')


                    

        if departamento in ["B1","B2","B3","B4","B5","B6","B7","B8","B9"]:
            
            print("Este departamento tiene como valor de Venta de 3.200UF")
            if departamento in departamentos:
                if departamentos[departamento] == 'Disponible':
                    departamentos[departamento] = 'X'
                    v7+=valorg2
                    rut = input("Ingrese el RUT: ")
                    nombre = input("Ingrese el nombre: ")                
                    comprador = {
                    "rut": rut,
                    "nombre": nombre,
                    "d": departamento + ":Comprado"
                }
                    compradores.append(comprador)
                    print(f'Departamento {departamento} Comprado exitosamente.')
                                
                else:
                    print(f'El departamento {departamento} ya no esta Disponible.')
            else:
                print('Departamento no valido.')


        if departamento in ["C1","C2","C3","C4","C5","C6","C7","C8","C9"]:
            
            print("Este departamento tiene como valor de Venta de 2.800UF")
            if departamento in departamentos:
                if departamentos[departamento] == 'Disponible':
                    departamentos[departamento] = 'X'
                    v8+=valorh2
                    rut = input("Ingrese el RUT: ")
                    nombre = input("Ingrese el nombre: ")                
                    comprador = {
                    "rut": rut,
                    "nombre": nombre,
                    "d": departamento + ":Comprado"
                }
                    compradores.append(comprador)
                    print(f'Departamento {departamento} Comprado exitosamente.')
                                
                else:
                    print(f'El departamento {departamento} ya no esta Disponible.')
            else:
                print('Departamento no valido.')


        if departamento in ["D1","D2","D3","D4","D5","D6","D7","D8","D9"]:
            
            print("Este departamento tiene como valor de Venta de 3.500UF")
            if departamento in departamentos:
                if departamentos[departamento] == 'Disponible':
                    departamentos[departamento] = 'X'
                    v9+=valori2
                    rut = input("Ingrese el RUT: ")
                    nombre = input("Ingrese el nombre: ")                
                    comprador = {
                    "rut": rut,
                    "nombre": nombre,
                    "d": departamento + ":Comprado"
                }
                    compradores.append(comprador)
                    print(f'Departamento {departamento} Comprado exitosamente.')
                                
                else:
                    print(f'El departamento {departamento} ya no esta Disponible.')
            else:
                print('Departamento no valido.')


        



def ver_compradores():
    for comprador in compradores:
        
            print("rut:", comprador["rut"])
            print("nombre:", comprador["nombre"])
            print(comprador["d"])

def mostrar_ganancias():
    


    tipos_departamento = {
        'A': 'Tipo A 3.800 UF',
        'B': 'Tipo B 3.000 UF',
        'C': 'Tipo C 2.800 UF',
        'D': 'Tipo D 3.500 UF'
    }
    
    total_por_tipo = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    

    for comprador in compradores:
        departamento = comprador['d'].split(':')[0]
        tipo_departamento = tipos_departamento[departamento[0]]
        total_por_tipo[departamento[0]] += 1
    
    print('--- Detalle de Compras ---')
    print('Tipo de Departamento\t\tCantidad\tTotal')
    total_compra=v6+v7+v8+v9+v10
    
    for tipo, cantidad in total_por_tipo.items():
        total = 0
        if tipo == 'A':
            total = cantidad * valorf2
        elif tipo == 'B':
            total = cantidad * valorg2
        elif tipo == 'C':
            total = cantidad * valorh2
        elif tipo == 'D':
            total = cantidad * valori2
        
        print(f'{tipos_departamento[tipo]}\t\t\t{cantidad}\t\t{total} UF')
    total_cantidad = sum(total_por_tipo.values())
    total_general = (total_por_tipo['A'] * valorf2) + (total_por_tipo['B'] * valorg2) + (total_por_tipo['C'] * valorh2) + (total_por_tipo['D'] * valori2)
    print(f'Total\t\t\t\t{total_cantidad}\t\t{total_general} UF')
    

            
            
menu()
