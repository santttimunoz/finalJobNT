CREATE DATABASE AlmacenDB
USE AlmacenDB 

CREATE TABLE Productos (
    ProductoID INT PRIMARY KEY,
    Nombre NVARCHAR(255),
    Descripcion NVARCHAR(MAX),
    Precio DECIMAL(10, 2)
);


INSERT INTO Productos (ProductoID, Nombre, Descripcion, Precio)
VALUES
    (1, 'Laptop', 'Laptop de alta gama', 1200.00),
    (2, 'Teléfono móvil', 'Teléfono inteligente último modelo', 800.00),
    (3, 'Impresora', 'Impresora láser a color', 300.00),
    (4, 'Tablet', 'Tablet compacta y potente', 500.00),
    (5, 'Monitor', 'Monitor HD de 27 pulgadas', 250.00);


CREATE DATABASE AlmacenDB;


USE AlmacenDB;


CREATE TABLE Existencias (
    ExistenciaID INT PRIMARY KEY,
    ProductoID INT FOREIGN KEY REFERENCES Productos(ProductoID),
    Cantidad INT
);


INSERT INTO Existencias (ExistenciaID, ProductoID, Cantidad)
VALUES
    (1, 1, 20),
    (2, 2, 50),
    (3, 3, 10),
    (4, 4, 30),
    (5, 5, 15);

CREATE TABLE Proveedores (
    ProveedorID INT PRIMARY KEY,
    Nombre NVARCHAR(255),
    Direccion NVARCHAR(255),
    Telefono NVARCHAR(15)
);


INSERT INTO Proveedores (ProveedorID, Nombre, Direccion, Telefono)
VALUES
    (1, 'ProveedorElectronics', 'Calle Principal 123', '+123456789'),
    (2, 'ProveedorMóviles', 'Avenida Secundaria 456', '+987654321'),
    (3, 'ProveedorSuministros', 'Plaza Comercial 789', '+111222333'),
    (4, 'ProveedorComputadoras', 'Avenida Tecnológica 789', '+555666777'),
    (5, 'ProveedorAccesorios', 'Calle de Accesorios 123', '+999000111');
