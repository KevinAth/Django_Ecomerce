from django.shortcuts import render, get_object_or_404
from .models import productos,Categoria
from .carrito import Cart
# Create your views here.

def index(request):
    listprod = productos.objects.all()
    liscat = Categoria.objects.all()
    data = {
        'productos': listprod,
        'categorias': liscat
    }
    return render(request,"index.html",data)

def  productosCategorias(request,categoria_id):
    objcategoria = Categoria.objects.get(pk=categoria_id)
    print(objcategoria)
    listprod = objcategoria.productos_set.all()
    print(listprod)
    
    listcat = Categoria.objects.all()
    
    data = {
        'productos': listprod,
        'categorias': listcat
    }
    
    return render(request, 'index.html',data)
    
def productosNombre(request):
    nombre = request.POST['nombre']
    
    listprod = productos.objects.filter(nombre__contains=nombre)
    print(listprod)
    listcat = Categoria.objects.all()
    
    data = {
        'categorias': listcat,
        'productos': listprod
    }
    
    return render(request,'index.html',data)

def productodetalles(request,producto_id):
    ##prod = productos.objects.get(pk=producto_id)
    prod = get_object_or_404(productos,pk=producto_id)
    data =  {
        'producto':prod
    }
    return render(request,'producto.html',data)
    
def carrito(request):
    return render(request,'carrito.html')
    
def addcarrito(request,producto_id):
    if request.method == 'POST':
        cantidad = int(request.POST['cantidad'])
    else:
        cantidad = 1
    
    objProducto = productos.objects.get(pk=producto_id)
    carritoProducto = Cart(request)
    carritoProducto.add(objProducto,cantidad)
    
    return render(request,'carrito.html')
    
def delprod(request,producto_id):
    objProducto = productos.objects.get(pk=producto_id)
    print(objProducto)
    carritoProducto = Cart(request)
    carritoProducto.delete(objProducto)
    
    return render(request,'carrito.html') 

def limpiarCarrito(request):
    carritoProductos = Cart(request)
    carritoProductos.clear()
    
    return render(request,'carrito.html')
    
    
    
    
    