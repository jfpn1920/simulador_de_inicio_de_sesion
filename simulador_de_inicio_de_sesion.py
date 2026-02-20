print("#-------------------------------------#")
print("#--| simulador de inicio de sesion |--#")
print("#-------------------------------------#")
usuario_correcto = "admin"
contrasena_correcta = "1234"
usuario = input("ingrese el usuario: ")
contrasena = input("ingrese la contraseña: ")
if usuario == usuario_correcto and contrasena == contrasena_correcta:
    print("acceso correcto, bienvenido.")
else:
    print("acceso incorrecto, usuario o contraseña inválidos.")