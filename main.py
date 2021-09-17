#importar base de datos 
from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches


#Iniciar sesion (solo se da acceso al usuario que aparezca en la lista de usuarios y ingrese la contraseña correcta). Solo te permite 3 intentos para introducir el usuario y una para la contraseña, si no se sale del programa.
#La lista de usuarios-contraseña esta formada por [el usuario, seguido de su contraseña] y es la siguiente.
lista_usuarios=[["administrador1","ingresar"],["administrador2","12345"],
["administrador3","contraseña"]]

print("Selecciona un opción: ")
print("(1) Iniciar sesión\n(2) Crear usuario")
registrar_usuario=input('Opción: ')
if registrar_usuario== "1": 
 usuario=input("Ingresa nombre de usuario: ")
 contraseña=input("Ingresa contraseña: ")
elif registrar_usuario=="2":
  print("Primero crea el usuario y contraseña, después inicia sesión")
  nuevo_usuario=input("Ingresa nombre de usuario: ")
  nueva_contraseña=input("Ingresa contraseña: ")
  lista_usuarios.append([nuevo_usuario,nueva_contraseña])
  print("Ahora inicia sesión")
  usuario=input("Ingresa nombre de usuario: ")
  contraseña=input("Ingresa contraseña: ")
  
else: #si no escribes las opciones correctas se saldra del proyecto
  print('Vuelve a intentarlo Escribe (1) si ya cuentas con un usuario o(2) si deseas registrar nuevo usuario')
  exit()

es_admi=0 #Es =0 Si son incorrectos los datos de usuario y contraseña. Es=1, si son correctos
intentos=0 # Número de intentos

while es_admi != 1 and intentos < 2:
  for admi in lista_usuarios:
    if admi[0]== usuario and admi[1]==contraseña:
      es_admi=1
  if es_admi==0:
    print("Datos incorrectos")
    usuario=input("Ingresa nombre de usuario: ")
    contraseña=input("Ingresa contraseña: ")
    intentos+=1

es_admi=1
if es_admi == 1: 
#Primer consigna: Productos 
  intentos=0
  opcion=0
  while opcion != 1 and opcion !=2 and opcion !=3 and intentos<3:
    print("Selecciona un opción: ")
    print("(1) 20 Productos más vendidos, 25 productos con más busquedas, productos ordenados con menores ventas y busquedas por categoria.\n(2) Lista de productos con mejores reseñas y lista con peores reseñas.\n(3) total de ingresos y ventas promedio mensuales, total anual y meses con más ventas al año")
    opcion=int(input("Opción: "))
    intentos+=1
    if intentos==3 and opcion !=1 and opcion !=2 and opcion !=3:
      print("Lo sentimos, vuelva a  intentarlo y elija una opcion correcta")
  if opcion==1:
    
    contador=0
    ventas_producto=[] #[id_producto,num_ventas]
    for producto in lifestore_products:
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[4]==0:
          contador+=1 #Suma 1 venta si se vendio y no se devolvio
        elif producto[0]==venta[1] and venta[4]==1:
          contador-=1 #Resta 1 venta si se vendio y se devolvio
        
      if contador !=0:
        ventas_producto.append([producto[0],producto[1],contador])
        contador=0
    

    #Ordenar lista de ventas de mayor a menor ventas
    productos_ordenados_mayor=[]
    while ventas_producto:
      maximo=ventas_producto[0][2]
      lista_max=ventas_producto[0]
      for totalventa in ventas_producto:
        if totalventa[2]>maximo:
          maximo=totalventa[2]
          lista_max=totalventa
      productos_ordenados_mayor.append(lista_max)
      ventas_producto.remove(lista_max)
    
    productos_ordenados_menor=[]
    tamaño=len(productos_ordenados_mayor)
    
    for i in range(1,tamaño+1):
      productos_ordenados_menor.append(productos_ordenados_mayor[tamaño-i])
    
    #20 productos más vendidos
    veint_productos_mas_vendidos=[]
    for j in range(0,20):
      veint_productos_mas_vendidos.append(productos_ordenados_mayor[j])
    print('Los 20 productos más vendidos son:["id_producto", "nombre_producto","#ventas" ')
    print(veint_productos_mas_vendidos)
   

   #productos con mayores busquedas
    contador=0
    busquedas_producto=[] #[id_producto,num_busquedas]
    for producto in lifestore_products:
      for busqueda in lifestore_searches:
        if producto[0]==busqueda[1]:
          contador+=1 #Suma 1 busqueda si se busco el producto
      if contador !=0:
          busquedas_producto.append([producto[0],producto[1],contador])
          contador=0
    
    #Ordenar lista de busquedas de mayor a menor 
    productos_busq_mayor=[]
    while busquedas_producto:
      maximo=busquedas_producto[0][2]
      lista_max=busquedas_producto[0]
      for totalbusqueda in busquedas_producto:
        if totalbusqueda[2]>maximo:
          maximo=totalbusqueda[2]
          lista_max=totalbusqueda
      productos_busq_mayor.append(lista_max)
      busquedas_producto.remove(lista_max)
    #print(len(productos_busq_mayor))=56
    #productos con menores busquedas ordenados de menor a mayor
    productos_busquedas_ordenados_menor=[]
    tamaño=len(productos_busq_mayor)
   
    for p in range(1,tamaño+1):
      productos_busquedas_ordenados_menor.append(productos_busq_mayor[tamaño-p])
    
    

      #25 productos más Busquedas
    veinticinco_productos_mas_buscados=[]
    for l in range(0,25):
      veinticinco_productos_mas_buscados.append(productos_busq_mayor[l])
    print('Los 25 productos más buscados son: ["id_producto", "nombre_producto","# busquedas"] ')
    print(veinticinco_productos_mas_buscados)
   
    #enlistar las categorias
    categorias=[]
    categoria1=''
    for producto in lifestore_products:
      if categoria1==producto[3]:
        continue
      else:
        categorias.append(producto[3])
        categoria1=producto[3]
    #print(categorias)# ['procesadores','tarjetas de video','tarjetas madre','discos duros','memorias usb','pantallas','bocinas','audifonos']

    #Se asigno a una lista ordenada de menor a mayor ventas igual a la lista de ventas de menor a mayor para agregar la categoria
    productos_ordenados_menor2=productos_ordenados_menor
    
    for elemento in lifestore_products:
      for producto in productos_ordenados_menor2:
        if producto[0]==elemento[0]:
          producto.append(elemento[3])
    lista_categorias_menores_ventas=[]
    
    for categoria in categorias:
      for ventas in productos_ordenados_menor2:
        if ventas[3]==categoria:
          lista_categorias_menores_ventas.append(ventas)
      print("La lista esta conformada por ['id_producto','nombre_del producto','# ventas, 'categoria']\nLos productos con menores ventas de la categoria", categoria, " son: ")
      print(lista_categorias_menores_ventas)
      lista_categorias_menores_ventas
      lista_categorias_menores_ventas=[]

    #Se asigno a una lista ordenada de menor a mayor busquedas igual a la lista de busquedas de menor a mayor para agregar la categoria
    productos_busq_ordenados_menor2=productos_busquedas_ordenados_menor
    #print(productos_busq_ordenados_menor2)
    for elemento in lifestore_products:
      for producto in productos_busq_ordenados_menor2:
        if producto[0]==elemento[0]:
          producto.append(elemento[3])
    lista_categorias_menores_busq=[]
    #print(productos_busq_ordenados_menor2)
    for categoria in categorias:
      for busqueda in productos_busq_ordenados_menor2:
        if busqueda[3]==categoria:
          lista_categorias_menores_busq.append(busqueda)

      print("La lista esta conformada por ['id_producto','nombre_del producto','# busquedas, 'categoria']\nLos productos con menores busquedas de la categoria", categoria, " son: ")

      print(lista_categorias_menores_busq)
      lista_categorias_menores_busq=[]
      
  if opcion==2:
    contador=0
    reseñas_producto=[] #[id_producto,nombre del producto,reseña]
    for producto in lifestore_products:
      for venta in lifestore_sales:
        if producto[0]==venta[1]:
          contador+=int(venta[2]) #Suma el valor de la reseña escrito en la venta o devolucion. 
      if contador !=0:
        reseñas_producto.append([producto[0],producto[1],contador])
        contador=0
    #print(reseñas_producto)
   
   #ordenar productos con mejores reseñas de mayor a menor
    productos_mayor_reseña=[]
    while reseñas_producto:
      maximo=reseñas_producto[0][2]
      lista_max=reseñas_producto[0]
      for totalreseñas in reseñas_producto:
        if totalreseñas[2]>maximo:
          maximo=totalreseñas[2]
          lista_max=totalreseñas
      productos_mayor_reseña.append(lista_max)
      reseñas_producto.remove(lista_max)
    #print(len(productos_mayor_reseña))#tiene 42 articulos vendidos
    #print(productos_mayor_reseña)
    
    #productos con menores reseñas ordenados de menor a mayor
    productos_peor_reseña=[]
    tamaño=len(productos_mayor_reseña)
    for t in range(1,tamaño+1):
      productos_peor_reseña.append(productos_mayor_reseña[tamaño-t])
    #print(productos_peor_reseña)


    #20 productos con mejor reseñas
    veinte_productos_mejor_reseña=[]
    for s in range(0,20):
      veinte_productos_mejor_reseña.append(productos_mayor_reseña[s])
    print('Los 20 productos con mejor reseña son: ["id_producto", "nombre_producto","reseñas"]')
    print(veinte_productos_mejor_reseña)

    #20 productos con peores reseñas
    veinte_productos_peor_reseña=[]
    for o in range(0,20):
      veinte_productos_peor_reseña.append(productos_peor_reseña[o])
    print('Los 20 productos con peor reseña son: ["id_producto", "nombre_producto","reseñas"]')
    print(veinte_productos_peor_reseña)
  
  #opción 3 total de ingresos y ventas promedio mensuales, total anual y meses con más ventas al año
  if opcion==3:
    
    
    #ingresos mensuales
    #enero
    contador=0
    sales1=0
    devoluciones1=0
    total_ingresos_mes1=0
    ventas_ingreso_producto_mes1=[] #[id_producto,nombre del producto,fecha_venta,ingresos]
    
    for producto in lifestore_products:
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[4]==0 and venta[3][3:5]=="01" and venta[3][6:10]=="2020":
          contador+=1 #Suma 1 venta si se vendio y no se devolvio
          sales1+=1
        elif producto[0]==venta[1] and venta[4]==1 and venta[3][3:5]=="01" and venta[3][6:10]=="2020":
          contador-=1 #Resta 1 venta si se vendio y se devolvio
          devoluciones1+=1
        
      if contador !=0:
        ventas_ingreso_producto_mes1.append([producto[0],producto[1],contador,int(producto[2])*contador])
        total_ingresos_mes1+=int(producto[2])*contador
        contador=0
    print("El total de ingresos para el mes 01 de 2020 es: $",total_ingresos_mes1, "de ", sales1," ventas",
    "y " , devoluciones1, " devoluciones")
    #frebrero
    contador=0
    sales2=0
    devoluciones2=0
    total_ingresos_mes2=0
    ventas_ingreso_producto_mes2=[] #[id_producto,nombre del producto,fecha_venta,ingresos]
    
    for producto in lifestore_products:
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[4]==0 and venta[3][3:5]=="02" and venta[3][6:10]=="2020":
          contador+=1 #Suma 1 venta si se vendio y no se devolvio
          sales2+=1
        elif producto[0]==venta[1] and venta[4]==1 and venta[3][3:5]=="02" and venta[3][6:10]=="2020":
          contador-=1 #Resta 1 venta si se vendio y se devolvio
          devoluciones2+=1
        
      if contador !=0:
        ventas_ingreso_producto_mes2.append([producto[0],producto[1],contador,int(producto[2])*contador])
        total_ingresos_mes2+=int(producto[2])*contador
        contador=0
    print("El total de ingresos para el mes 02 de 2020 es: $",total_ingresos_mes2, "de ", sales2, " ventas",
    "y " , devoluciones2, " devoluciones")

  #Marzo
    contador=0
    sales3=0
    devoluciones3=0
    total_ingresos_mes3=0
    ventas_ingreso_producto_mes3=[] #[id_producto,nombre del producto,fecha_venta,ingresos]
    
    for producto in lifestore_products:
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[4]==0 and venta[3][3:5]=="03" and venta[3][6:10]=="2020":
          contador+=1 #Suma 1 venta si se vendio y no se devolvio
          sales3+=1
        elif producto[0]==venta[1] and venta[4]==1 and venta[3][3:5]=="03" and venta[3][6:10]=="2020":
          contador-=1 #Resta 1 venta si se vendio y se devolvio
          devoluciones3+=1
        
      if contador !=0:
        ventas_ingreso_producto_mes3.append([producto[0],producto[1],contador,int(producto[2])*contador])
        total_ingresos_mes3+=int(producto[2])*contador
        contador=0
    print("El total de ingresos para el mes 03 de 2020 es: $",total_ingresos_mes3,"de ", sales3," ventas",
    "y " , devoluciones3, " devoluciones")

    #Abril
    contador=0
    sales4=0
    devoluciones4=0
    total_ingresos_mes4=0
    ventas_ingreso_producto_mes4=[] #[id_producto,nombre del producto,fecha_venta,ingresos]
    
    for producto in lifestore_products:
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[4]==0 and venta[3][3:5]=="04" and venta[3][6:10]=="2020":
          contador+=1 #Suma 1 venta si se vendio y no se devolvio
          sales4+=1
        elif producto[0]==venta[1] and venta[4]==1 and venta[3][3:5]=="04" and venta[3][6:10]=="2020":
          contador-=1 #Resta 1 venta si se vendio y se devolvio
          devoluciones4+=1
        
      if contador !=0:
        ventas_ingreso_producto_mes4.append([producto[0],producto[1],contador,int(producto[2])*contador])
        total_ingresos_mes4+=int(producto[2])*contador
        contador=0
    print("El total de ingresos para el mes 04 de 2020 es: $",total_ingresos_mes4,"de ", sales4," ventas",
    "y " , devoluciones4, " devoluciones")

    #Mayo
    contador=0
    sales5=0
    devoluciones5=0
    total_ingresos_mes5=0
    ventas_ingreso_producto_mes5=[] #[id_producto,nombre del producto,fecha_venta,ingresos]
    
    for producto in lifestore_products:
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[4]==0 and venta[3][3:5]=="05" and venta[3][6:10]=="2020":
          contador+=1 #Suma 1 venta si se vendio y no se devolvio
          sales5+=1
        elif producto[0]==venta[1] and venta[4]==1 and venta[3][3:5]=="05" and venta[3][6:10]=="2020":
          contador-=1 #Resta 1 venta si se vendio y se devolvio
          devoluciones5+=1
        
      if contador !=0:
        ventas_ingreso_producto_mes5.append([producto[0],producto[1],contador,int(producto[2])*contador])
        total_ingresos_mes5+=int(producto[2])*contador
        contador=0
    print("El total de ingresos para el mes 05 de 2020 es: $",total_ingresos_mes5,"de ", sales5," ventas",
    "y " , devoluciones5, " devoluciones")

    #Junio
    contador=0
    sales6=0
    devoluciones6=0
    total_ingresos_mes6=0
    ventas_ingreso_producto_mes6=[] #[id_producto,nombre del producto,fecha_venta,ingresos]
    
    for producto in lifestore_products:
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[4]==0 and venta[3][3:5]=="06" and venta[3][6:10]=="2020":
          contador+=1 #Suma 1 venta si se vendio y no se devolvio
          sales6+=1
        elif producto[0]==venta[1] and venta[4]==1 and venta[3][3:5]=="06" and venta[3][6:10]=="2020":
          contador-=1 #Resta 1 venta si se vendio y se devolvio
          devoluciones6+=1
        
      if contador !=0:
        ventas_ingreso_producto_mes6.append([producto[0],producto[1],contador,int(producto[2])*contador])
        total_ingresos_mes6+=int(producto[2])*contador
        contador=0
    print("El total de ingresos para el mes 06 de 2020 es: $",total_ingresos_mes6,"de ", sales6," ventas",
    "y " , devoluciones6, " devoluciones")

    #Juilo
    contador=0
    sales7=0
    devoluciones7=0
    total_ingresos_mes7=0
    ventas_ingreso_producto_mes7=[] #[id_producto,nombre del producto,fecha_venta,ingresos]
    
    for producto in lifestore_products:
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[4]==0 and venta[3][3:5]=="07" and venta[3][6:10]=="2020":
          contador+=1 #Suma 1 venta si se vendio y no se devolvio
          sales7+=1
        elif producto[0]==venta[1] and venta[4]==1 and venta[3][3:5]=="07" and venta[3][6:10]=="2020":
          contador-=1 #Resta 1 venta si se vendio y se devolvio
          devoluciones7+=1
        
      if contador !=0:
        ventas_ingreso_producto_mes7.append([producto[0],producto[1],contador,int(producto[2])*contador])
        total_ingresos_mes7+=int(producto[2])*contador
        contador=0
    print("El total de ingresos para el mes 07 de 2020 es: $",total_ingresos_mes7, "de ", sales7," ventas",
    "y " , devoluciones7, " devoluciones")

    #Agosto
    contador=0
    sales8=0
    devoluciones8=0
    total_ingresos_mes8=0
    ventas_ingreso_producto_mes8=[] #[id_producto,nombre del producto,fecha_venta,ingresos]
    
    for producto in lifestore_products:
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[4]==0 and venta[3][3:5]=="08" and venta[3][6:10]=="2020":
          contador+=1 #Suma 1 venta si se vendio y no se devolvio
          sales8+=1
        elif producto[0]==venta[1] and venta[4]==1 and venta[3][3:5]=="08" and venta[3][6:10]=="2020":
          contador-=1 #Resta 1 venta si se vendio y se devolvio
          devoluciones8+=1
        
      if contador !=0:
        ventas_ingreso_producto_mes8.append([producto[0],producto[1],contador,int(producto[2])*contador])
        total_ingresos_mes8+=int(producto[2])*contador
        contador=0
    print("El total de ingresos para el mes 08 de 2020 es: $",total_ingresos_mes8, "de ", sales8," ventas",
    "y " , devoluciones8, " devoluciones")
  
  #Septiembre
    contador=0
    sales9=0
    devoluciones9=0
    total_ingresos_mes9=0
    ventas_ingreso_producto_mes9=[] #[id_producto,nombre del producto,fecha_venta,ingresos]
    
    for producto in lifestore_products:
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[4]==0 and venta[3][3:5]=="09" and venta[3][6:10]=="2020":
          contador+=1 #Suma 1 venta si se vendio y no se devolvio
          sales9+=1
        elif producto[0]==venta[1] and venta[4]==1 and venta[3][3:5]=="09" and venta[3][6:10]=="2020":
          contador-=1 #Resta 1 venta si se vendio y se devolvio
          devoluciones9+=1
        
      if contador !=0:
        ventas_ingreso_producto_mes9.append([producto[0],producto[1],contador,int(producto[2])*contador])
        total_ingresos_mes9+=int(producto[2])*contador
        contador=0
    print("El total de ingresos para el mes 09 de 2020 es: $",total_ingresos_mes9, "de ", sales9," ventas",
    "y " , devoluciones9, " devolución")

    #Total de ingresos anuales 2020
    contador=0
    total_ingresos=0
    ventas_ingreso_producto=[] #[id_producto,nombre del producto,fecha_venta,ingresos]
    for producto in lifestore_products:
      for venta in lifestore_sales:
        if producto[0]==venta[1] and venta[4]==0 and venta[3][6:10]=="2020":
          contador+=1 #Suma 1 venta si se vendio y no se devolvio
        elif producto[0]==venta[1] and venta[4]==1 and venta[3][6:10]=="2020":
          contador-=1 #Resta 1 venta si se vendio y se devolvio
        
      if contador !=0:
        ventas_ingreso_producto.append([producto[0],producto[1],venta[3],int(producto[2])*contador])
        total_ingresos+=int(producto[2])*contador
        contador=0
    
        #total_ingresos+=ventas_ingreso_producto[3]
    #print(ventas_ingreso_producto)
    print("El total de ingresos para el año 2020 es: $",total_ingresos)

    #3 meses con mayores ventas
    lista_ventas_ingreso=[["Enero"],["Febrero"],["Marzo"],["Abril"],["Mayo"],["Junio"],["Julio"],["Agosto"],["Septiembre"]]
  
    #La lista lista_ventas_ingreso contiene [[enero,ventas,ingresos],[febrero,ventas,ingresos],[marzo,ventas,ingresos],[abril,ventas,ingresos],[mayo,ventas,ingresos],[junio,ventas,ingresos],[julio,ventas,ingresos],[agosto,ventas,ingresos],[septiembre,ventas,ingresos]]
    #mes1
    lista_ventas_ingreso[0].append(sales1-devoluciones1)
    lista_ventas_ingreso[0].append(total_ingresos_mes1)
    #mes2
    lista_ventas_ingreso[1].append(sales2-devoluciones2)
    lista_ventas_ingreso[1].append(total_ingresos_mes2)
    #mes3
    lista_ventas_ingreso[2].append(sales3-devoluciones3)
    lista_ventas_ingreso[2].append(total_ingresos_mes3)
    #mes4
    lista_ventas_ingreso[3].append(sales4-devoluciones4)
    lista_ventas_ingreso[3].append(total_ingresos_mes4)
    #mes2
    lista_ventas_ingreso[4].append(sales5-devoluciones5)
    lista_ventas_ingreso[4].append(total_ingresos_mes5)
    #mes6
    lista_ventas_ingreso[5].append(sales6-devoluciones6)
    lista_ventas_ingreso[5].append(total_ingresos_mes6)
    #mes7
    lista_ventas_ingreso[6].append(sales7-devoluciones7)
    lista_ventas_ingreso[6].append(total_ingresos_mes7)
    #mes8
    lista_ventas_ingreso[7].append(sales8-devoluciones8)
    lista_ventas_ingreso[7].append(total_ingresos_mes8)
    #mes9
    lista_ventas_ingreso[8].append(sales9-devoluciones9)
    lista_ventas_ingreso[8].append(total_ingresos_mes9)
    #ordenar lista de meses por mayor a menor venta
    #print(lista_ventas_ingreso)
    mayor_ventas_mes=[]
    while lista_ventas_ingreso:
      maximo=lista_ventas_ingreso[0][1]
      lista_max=lista_ventas_ingreso[0]
      for mes in lista_ventas_ingreso:
        if mes[1]>maximo:
          maximo=mes[1]
          lista_max=mes
      mayor_ventas_mes.append(lista_max)
      lista_ventas_ingreso.remove(lista_max)
    #lista 3 meses mejores ventas
    lista_tres_meses_mas_ventas=[]
    for e in range(0,3):
      lista_tres_meses_mas_ventas.append(mayor_ventas_mes[e][0:2])

    print("Los 3 meses con mayores ventas fueron [Mes,ventas]: ")
    print(lista_tres_meses_mas_ventas)
    




