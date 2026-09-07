import pyodbc

server = "127.0.0.1"
database = "usuarios"
usuario = 'sa'
password = '123456'
cadenaConexion = f'DRIVER={{SQL Server}}; SERVER={server}, DATABASE={database}, Trusted_Connection=yes, USERNAME= {usuario}, PASSWORD={password}'

conexion = pyodbc.connect(cadenaConexion)
cursor = conexion.cursor()
