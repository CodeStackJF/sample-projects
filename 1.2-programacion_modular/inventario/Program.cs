namespace inventario;

class Program
{
    static void Main(string[] args)
    {
        var productos = new List<Producto>()
        {
            new Producto(1, "TV", 500, 5),
            new Producto(2, "Radio", 200, 10),
            new Producto(3, "Laptop", 820, 7),
        };

        Inventario inventario = new Inventario(productos);
        inventario.MostrarInventario();
        Console.WriteLine("Realizando venta.");
        Venta venta = new Venta(inventario);
        venta.Vender(1, 3);
        venta.Vender(1, 6);
        inventario.MostrarInventario();

        Console.WriteLine("Agregando productos al inventario");

        inventario.AgregarProducto(new Producto(4, "Tablet", 250, 4));
        inventario.AgregarProducto(new Producto(1, 7));

        int indice_producto = productos.FindIndex(x=>x.id == 1);
        productos[indice_producto].CambiarNombre("Televisión");

        Console.WriteLine("Producto actualizado");
        inventario.MostrarInventario();

        inventario.RemoverProducto(1);

        Console.WriteLine("Producto removido");

        inventario.MostrarInventario();

    }
}

class Producto
{
    public int id {get; }
    public string nombre;
    public decimal precio;
    public int existencias;

    public Producto(int _id, string _nombre, decimal _precio, int _existencias)
    {
        id = _id;
        nombre = _nombre;
        precio = _precio;
        existencias = _existencias;
    }

    public Producto(int _id, int _existencias)
    {
        id = _id;
        existencias = _existencias;
        nombre = "";
    }

    public void CambiarNombre(string _nombre)
    {
        nombre = _nombre;
    }
}

class Inventario
{
    private List<Producto> productos;

    public Inventario(List<Producto> _productos)
    {
        productos = _productos;
    }

    public void MostrarInventario()
    {
        foreach(Producto producto in productos)
        {
            Console.WriteLine($"ID: {producto.id} Nombre: {producto.nombre} Precio: {producto.precio} Existencias: {producto.existencias}");
        }
    }

    public void DisminuirInventario(int idProducto, int cantidad)
    {
        if(TotalProducto(idProducto) < cantidad)
        {
            Console.WriteLine("No hay suficientes existencias del producto.");
            return;
        }
        int indice = productos.FindIndex(x=>x.id == idProducto);
        productos[indice].existencias -= cantidad;
    }

    public void AumentarInventario(int idProducto, int cantidad)
    {
        Producto producto = productos.Find(x=>x.id ==idProducto)!;
        producto.existencias += cantidad;
    }

    public int TotalProducto(int idProducto)
    {
        return productos.Find(x=>x.id ==idProducto)!.existencias;
    }

    public void AgregarProducto(Producto producto)
    {
        int indice = productos.FindIndex(x=>x.id == producto.id);
        if(indice == -1)
        {
            productos.Add(producto);
        }
        else
        {
            AumentarInventario(producto.id, producto.existencias);
        }
    }

    public void RemoverProducto(int idProducto)
    {
        int indice = productos.FindIndex(x=>x.id == idProducto);
        productos.RemoveAt(indice);
    }

    public int TotalProductosInventario()
    {
        return productos.Count;
    }
}

class Venta
{
    private readonly Inventario inventario;

    public Venta(Inventario _inventario)
    {
        inventario = _inventario;
    }

    public void Vender(int idProducto, int cantidad)
    {
        inventario.DisminuirInventario(idProducto, cantidad);
    }
}
//Productos
//Inventario
//Venta