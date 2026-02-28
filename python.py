sistemaActivo: bool = True
tienePermiso: bool = False
if sistemaActivo == True and tienePermiso == True:
    print ("Accion ejecutada")
elif sistemaActivo == True and tienePermiso == False:
    print ("Permiso denegado")    
else:
    print ("Sistema inactivo")