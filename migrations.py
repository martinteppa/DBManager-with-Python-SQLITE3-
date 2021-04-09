from models import Producto
 

productos = Producto()
productos.createTable()

productos.agregar(Nombre="zapatilla",Cantidad=200, Precio=23.33)
productos.agregar(Nombre="camisa",Cantidad=300, Precio=40.99)
""" productos.eliminar(2) """
productos.actualizar(1,Nombre="pantalon",Cantidad=5)

 