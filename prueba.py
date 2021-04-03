
with open("Database_Employees.txt","a+") as dbe:
    dbe.write(f"{empleado.nombre_completo}//{edad}//{genero}//{cedula}//{telefono}//{cargo}//{sueldo}\n")


try:
    with open("Database_Employees.txt") as dbe:
        datos = dbe.readlines()
            for dato in datos:
                empleado_l = dato[:-1].split("//")
                if empleado_l[0] == nombre_completo:
                    print("\nEmpleado ya registrado.")
                    empleado = Persona(empleado_l[0],empleado_l[1],empleado_l[2],empleado_l[3],empleado_l[4],empleado_l[5])
                    return empleado
                else:
                    return registro_empleado(nombre_completo)
except FileNotFoundError:
    print("\nTodavía no hay ningún empleado registrado.\n")
    return registro_empleado(nombre_completo)

try:
    with open("Database_Employees.txt") as dbe:
        datos = dbe.readlines()
        for dato in datos:
            empleado_l = dato[:-1].split("//")
            if empleado_l[0] == nombre_completo:
                print("\nEmpleado ya registrado.")
                empleado = Persona(empleado_l[0],empleado_l[1],empleado_l[2],empleado_l[3],empleado_l[4],empleado_l[5])
                return empleado
            else:
                return registro_empleado(nombre_completo)
except FileNotFoundError:
    print("\nTodavía no hay ningún empleado registrado.\n")
    return registro_empleado(nombre_completo)




    

# from Persona import Persona

# cargos = [("Gerente",10000),("Vendedor",6000),("Encargado de almacén",5500),("Personal de mantenimiento",2000)]



# def registro_empleado(nombre_completo):
#     """
#     Esta función toma por teclado los datos de un nuevo empleado para agregarlo a la base de datos de empleados de la tienda ('Database_Employees.txt').

#     Argumentos => nombre_completo: nombre de la persona ingresado por teclado.

#     Retorna => Registro del nuevo empleado en el archivo .txt, notifiación de registro exitoso y toda la información del empleado registrado.

#     """

#     edad = input("Ingrese su edad (entre 18 y 70): ")
#     while not edad.isnumeric() or int(edad) not in range(18,71):
#         edad = input("Ingreso inválido, ingrese su edad (entre 18 y 70): ")

#     genero = input("Ingrese su género ('F' para 'femenino', 'M' para 'masculino', 'O' para 'otro'): ")
#     while genero.upper() != "F" and genero.upper() != "M" and genero.upper() != "O":
#         genero = input("Ingreso inválido, ingrese su género ('F' para 'femenino', 'M' para 'masculino', 'O' para 'otro'): ")
#     genero = genero.upper()


#     cedula = input("Ingrese su número de cédula (sin caracteres especiales): ")
#     while not cedula.isnumeric() or int(cedula) < 1:
#         cedula = input("Ingreso inválido, intente otra vez: ")


#     telefono = input("Ingrese su número de teléfono (sin caracteres especiales): ")
#     while not telefono.isnumeric() or len(telefono) != 11:
#         telefono = input("Ingreso inválido, intente otra vez: ")

#     for i,c in enumerate(cargos):
#         print(f"{i+1}. {c[0]}")
#     cargo_sel = input("Ingrese el número correspondiente al cargo del empleado: ")
#     while not cargo_sel.isnumeric() or int(cargo_sel) not in range(1,5):
#         cargo_sel = input("Ingreso inválido, intente otra vez: ")
#     for i,c in enumerate(cargos):
#         if int(cargo_sel) == (i+1):
#             print("coinc")
#             cargo = c[0]
#             sueldo = c[1]


#     empleado = Persona(nombre_completo,edad,genero,cedula,telefono,cargo,sueldo)

#     with open("Database_Employees.txt","a+") as dbe:
#         dbe.write(f"{empleado.nombre_completo}//{edad}//{genero}//{cedula}//{telefono}//{cargo}//{sueldo}\n")

#     print("\nEmpleado registrado con éxito.")
#     return empleado





# def verificacion_empleado_existente():
#     """
#     Esta función toma por teclado el nombre de la persona a registrarse. Si se encuentra en la base de datos de empleados registrados, lo notifica. Si no está registrado, se ejecuta la función registro_empleado(nombre_completo). Si no hay ningún empleado registrado, lo notifica e igualmente ejecuta la función registro_empleado(nombre_completo).

#     Argumentos => n/a

#     Retorna =>
#     \tSi está en la lista: objeto 'Persona' con la información correspondiente al nombre ya existente.
#     \tSi no está en la lista: retorna el producto de la ejecución de la función 'registro_empleado(nombre_completo)'
#     \tSi el archivo .txt no existe (o sea, no hay nadie registrado): retorna el producto de la ejecución de la función 'registro_empleado(nombre_completo)' después de notificar la inexistencia de empleados registrados.

#     """

#     nombre_completo = input("Ingrese su nombre completo: ")
#     nc = nombre_completo.split()

#     while True:
#         if not ("".join(nc)).isalpha():
#             nombre_completo = input("Ingreso inválido, ingrese su nombre completo: ")
#             nc = nombre_completo.split()
#         elif ("".join(nc)).isalpha():
#             break
#     nombre_completo = nombre_completo.title()



#     try:
#         with open("Database_Employees.txt") as dbe:
#             datos = dbe.readlines()
#         for dato in datos:
#             empleado_l = dato[:-1].split("//")
#             if empleado_l[0] == nombre_completo:
#                 print("\nEmpleado ya registrado.")
#                 empleado = Persona(empleado_l[0],empleado_l[1],empleado_l[2],empleado_l[3],empleado_l[4],empleado_l[5])
#                 return empleado
#         else:
#             return registro_empleado(nombre_completo)
#     except FileNotFoundError:
#         print("\nTodavía no hay ningún empleado registrado.\n")
#         return registro_empleado(nombre_completo)




# def ver_empleados():
#     """
#     Esta función muestra la información de todos los empleaods previamente almacenada en la base de datos de empleados de la tienda.

#     Argumentos => n/a

#     Retorna => 
#     \tSi hay empleados registrados: imprime los empleados numerados por orden de registro.
#     \tSi el archivo .txt no existe (o sea, no hay nadie registrado): notifica que no existen empleados registrados.

#     """
#     empleados = []
#     try:
#         with open("Database_Employees.txt") as dbe:
#             datos = dbe.readlines()
#         if len(datos) == 0:
#             print("\nTodavía no hay ningún empleado registrado.\n")
#         else:
#             for dato in datos:
#                 empleado = dato[:-1].split("//")
#                 empleados.append(Persona(empleado[0],empleado[1],empleado[2],empleado[3],empleado[4],empleado[5],empleado[6]))

#             print("\n\t\tEMPLEADOS REGISTRADOS (por orden de registro)\n")
#             for i,empl in enumerate(empleados):
#                 print("-"*2,str(i+1),"-"*18)
#                 print(empl.mostrar_empleado())
#             return True

#     except FileNotFoundError:
#         print("\nTodavía no hay ningún empleado registrado.\n")
#         return False


# def modificar_empleado(ne):
#     """
#     Esta función permite modificar la información de los empleados previamente almacenada en la base de datos de empleados de la tienda ('Database_Employees.txt').

#     Argumentos => ne: número asignado previamente al empleado que se desea modificar.

#     Retorna => Modificación del archivo .txt, notificación de modificación exitosa y ejecución del método mostrar_empleado() sobre el objeto 'empleado'.

#     """
#     with open("Database_Employees.txt") as dbe:
#         datos = dbe.readlines()
#     for i,dato in enumerate(datos):
#         if i == (ne-1):
#             e = dato[:-1].split("//")
#             empleado = Persona(e[0],e[1],e[2],e[3],e[4],e[5],e[6])

#     print(f"1. Nombre completo: {empleado.nombre_completo}\n2. Edad: {empleado.edad}\n3. Género: {empleado.genero}\n4. Cédula: {empleado.cedula}\n5. Teléfono: {empleado.telefono}\n6. Cargo: {empleado.cargo}")
#     atributo = input("\nIngrese el número correspondiente al atributo que desea modificar: ")
#     while (not atributo.isnumeric()) or (int(atributo) not in range(1,7)):
#         atributo = input(f"Ingreso inválido, ingrese el número correspondiente al atributo que desea modificar: ")
    
    
#     print("\n")
    
#     if atributo == "1":
#         empleado.nombre_completo = input("Ingrese su nombre completo: ")
#         nc = (empleado.nombre_completo).split()

#         while True:
#             if not ("".join(nc)).isalpha():
#                 empleado.nombre_completo = input("Ingreso inválido, ingrese su nombre completo: ")
#                 nc = (empleado.nombre_completo).split()
#             elif ("".join(nc)).isalpha():
#                 break
        
#         empleado.nombre_completo = empleado.nombre_completo.title()
#         e[0] = empleado.nombre_completo



#     elif atributo == "2":
#         empleado.edad = input("Ingrese su edad (entre 18 y 70): ")
#         while not empleado.edad.isnumeric() or int(empleado.edad) not in range(18,71):
#             empleado.edad = input("Ingreso inválido, ingrese su edad (entre 18 y 70): ")
#         e[1] = empleado.edad

#     elif atributo == "3":
#         empleado.genero = input("Ingrese su género ('F' para 'femenino', 'M' para 'masculino', 'O' para 'otro'): ")
#         while empleado.genero.upper() != "F" and empleado.genero.upper() != "M" and empleado.genero.upper() != "O":
#             empleado.genero = input("Ingreso inválido, ingrese su género ('F' para 'femenino', 'M' para 'masculino', 'O' para 'otro'): ")
#         empleado.genero = empleado.genero.upper()
#         e[2] = empleado.genero

    
#     elif atributo == "4":
#         empleado.cedula = input("Ingrese su número de cédula (sin caracteres especiales): ")
#         while not empleado.cedula.isnumeric() or int(empleado.cedula) < 1:
#             empleado.cedula = input("Ingreso inválido, intente otra vez: ")
#         e[3] = empleado.cedula


#     elif atributo == "5":
#         empleado.telefono = input("Ingrese su número de teléfono (sin caracteres especiales): ")
#         while not empleado.telefono.isnumeric() or len(empleado.telefono) != 11:
#             empleado.telefono = input("Ingreso inválido, intente otra vez: ")
#         e[4] = empleado.telefono


#     else:
#         for i,c in enumerate(cargos):
#             print(f"{i+1}. {c[0]}")
#         cargo_sel = input("Ingrese el número correspondiente al cargo del empleado: ")
#         while not cargo_sel.isnumeric() or int(cargo_sel) not in range(1,5):
#             cargo_sel = input("Ingreso inválido, intente otra vez: ")
#         for i,c in enumerate(cargos):
#             if int(cargo_sel) == (i+1):
#                 empleado.cargo = c[0]
#                 empleado.sueldo = c[1]
#                 e[5] = empleado.cargo
#                 e[6] = empleado.sueldo




#     with open("Database_Employees.txt") as dbe:
#         datos = dbe.readlines()
#     for i in range(len(datos)):
#         if i == (ne-1):
#             datos[ne-1] = f"{e[0]}//{e[1]}//{e[2]}//{e[3]}//{e[4]}//{e[5]}//{e[6]}\n"
#     with open("Database_Employees.txt","w") as dbe:
#         dbe.writelines(datos)
    

#     print("\n\t\tEmpleado modificado con éxito.\n")
#     print(empleado.mostrar_empleado())


# def eliminar_empleado(ne):
#     """
#     Se recorre la base de datos de empleados registrados de la tienda ('Database_Employees.txt') y se elimina el deseado.

#     Argumentos => ne: número asignado previamente al empleado que se desea eliminar.

#     Retorna => Eliminación del empleado elegido del archivo .txt, notificación de que el empleado fue eliminado y ejecución de la función ver_empleados() después de eliminarlo.

#     """
#     with open("Database_Employees.txt") as dbe:
#         datos = dbe.readlines()
#         eliminar = datos[ne - 1]
#         empleado_eliminado = eliminar[:-1].split("//")
#     with open("Database_Employees.txt", "w") as dbe:
#         for dato in datos:
#             if dato != eliminar:
#                 dbe.write(dato)

    
#     print (f"\n\t\tEmpleado '{empleado_eliminado[0]}' eliminado de la base de datos.\n")
#     ver_empleados()









# def main():
#     seguir = True
#     while seguir:
#         print("Seleccione una opción:\n1. Registrar empleado\n2. Ver empleados registrados\n3. Modificar información de empelado registrado\n4. Eliminar empleado registrado\n")

#         seleccion = input("Ingrese el número correspondiente a su selección: ")
#         while (not seleccion.isnumeric()) or (int(seleccion) not in range(1,5)):
#             seleccion = input(f"Ingreso inválido, ingrese el número correspondiente a su selección: ")
#         seleccion = int(seleccion)

#         if seleccion == 1:
#             empleado = verificacion_empleado_existente()
#             print("\n")
#             print(empleado.mostrar_empleado())

#         elif seleccion == 2:
#             print("\n")
#             ver_empleados()


#         elif seleccion == 3:
#             print("\n")
#             if ver_empleados() == True:
#                 modificar = True
#                 while modificar:
#                     while True:
#                         np = input("\nIngrese el número correspondiente a la persona cuya información desea modificar: ")
#                         while not np.isnumeric():
#                             np = input("Ingreso inválido, ingrese el número correspondiente a la persona cuya información desea modificar: ")
#                         np = int(np)
#                         try:
#                             modificar_empleado(np)
#                             modificar_info = input("¿Desea modificar la información de otra persona? ('S' para 'sí', 'N' para 'no'): ")
#                             while modificar_info.upper() != "S" and modificar_info.upper() != "N":
#                                 modificar_info = input("Ingreso inválido, ¿desea modificar la información de otra persona? ('S' para 'sí', 'N' para 'no'): ")
#                             if modificar_info.upper() == "S":
#                                 continue
#                             elif modificar_info.upper() == "N":
#                                 modificar = False
#                             break
#                         except (IndexError, UnboundLocalError):
#                             print("El número ingresado no corresponde a ninguna persona, por favor intente otra vez.")


            

#         elif seleccion == 4:
#             print("\n")
#             if ver_empleados() == True:
#                 while True:
#                     np = input("\nIngrese el número correspondiente a la persona cuya información desea eliminar: ")
#                     while not np.isnumeric():
#                         np = input("Ingreso inválido, ingrese el número correspondiente a la persona cuya información desea eliminar: ")
#                     np = int(np)
#                     try:
#                         print("\n")
#                         eliminar_empleado(np)
#                         break
#                     except (IndexError, UnboundLocalError):
#                         print("El número ingresado no corresponde a ninguna persona, por favor intente otra vez.")



        

#         print("\n")
#         continuar = input("¿Desea realizar alguna otra operación? ('S' para 'sí', 'N' para 'no'): ")
#         while continuar.upper() != "S" and continuar.upper() != "N":
#             continuar = input("Ingreso inválido, ¿desea realizar alguna otra operación? ('S' para 'sí', 'N' para 'no'): ")
#         if continuar.upper() == "S":
#             print("\n")
#             continue
#         elif continuar.upper() == "N":
#             break

# main()