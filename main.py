from ClaseEmail import Email
from Funcion4 import funcion4
#def test():
   # em = Email('mauri', 'gmail', 'com', 'maf')
    #print(em.retornaEmail())
    #m = Email.crearCuenta('mauri@gmail.com', 'nfnf')
    #print(m.retornaEmail())
if __name__ == '__main__':
    #test()
    nom = input("Ingrese su nombre:")
    p = Email(input ("Ingrese su ID:"),input ("Ingrese su dominio:"),input ("Ingrese su tipo de dominio:"),input ("Ingrese su contraseña:"))
    print("Estimado "+nom+" te enviaremos tus mensajes a la direccion "+p.retornarEmail())
    p.modifica_contra(input("Ingrese contraseña actual:"))
    corr = Email("","","","")
    corr.crearCuenta(input("Ingrese su correo:"))
    archivo = open ("Correos.csv")
    direcciones = archivo.read().split(",")
    funcion4(direcciones) 
    archivo.close()
    
  
    
    