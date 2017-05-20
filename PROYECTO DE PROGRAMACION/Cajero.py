#!/usr/bin/env python2
# -*- coding: utf-8 -*-


def logIn():           #linea 1
    suma = 3
    valido = False
    while suma > 0:
        archivo = open("clientes.txt", "r")
        cuenta = raw_input("Ingrese su numero de cuenta: ")
        nip = raw_input("Ingrese su NIP: ")
        #linea=archivo.readline()
        for linea in archivo:
            #print linea
            lista = linea.split(" ")
            if cuenta == lista[0] and nip==lista[3]:
                lista2=list(lista)
                valido=True
            
        archivo.close()
        if valido:
            return lista2
        else:
            suma=suma-1
            print "El numero de cuenta o el NIP son incorrectos"
            print "Por favor vuelva a intentarlo"    #linea 20
            print "Intentos restantes", suma
            
def consultaSaldo(saldo, nombre, apellido, cuenta):
    print "\nSu saldo es de:", saldo
    while True:
        print "\nDesea imprimir su saldo"
        print "1 Si"
        print "2 No\n"
        op=input("Escriba el numero de opcion: ")
        if op==1:           #linea 30
            archivo2=open("saldo.txt", "w")
            archivo2.write("************ Banco IME ***********\n")
            archivo2.write("\nNunero de cuenta: "+cuenta+"\n")
            archivo2.write("Usuario: "+nombre+" "+apellido+"\n")
            archivo2.write("Su saldo es de: $"+saldo+"\n")
            archivo2.write("Gracias por su preferencia\n")
            archivo2.write("\n**********************************")
            archivo2.close()
            print "\nImprimiendo..."
            print "Impreso"               #linea 40
            break
        elif op==2:
            print "\nRegresando al menu..."
            break
        else:
            print "No es una opcion valida"


def deposita(saldo, nombre, apellido, cuenta):
    nsaldo = int(saldo)+input("Que cantidad desea depositar?: ")
    dep = nsaldo-int(saldo)
    strDomain = ""
    domain = []

    file = open("clientes.txt", "r")
    for l in file: domain.append(l.strip('\n\r').split(" "))
    file.close()

    for i in domain:
        if i[0] == cuenta:
            #print "QQQQQQQQQQQQQQQ" + cuenta
            i[4] = str(nsaldo)
        strDomain+= " ".join(i) + "\n"

    file = open("clientes.txt", "w")
    file.write(strDomain);
    file.close()
    
    print "Su nuevo saldo es de %d" % nsaldo

    if(raw_input("Desea imprimir el recibo? (si/no) ")== "si" or "Si"):
        toWrt = """************ Banco IME ***************
Numero de cuenta: %s
Usuario: %s
Su deposito fue de %s
Su saldo actual es de %s
Gracias por su preferencia
**********************************
""" % (cuenta, nombre, dep, nsaldo)
        print "Impreso"
    file=open("deposito.txt","w")
    file.write(toWrt)
    file.close()
    return nsaldo

def retiro(saldo, nombre, apellido, cuenta):
    nsaldo = int(saldo)-input("Que cantidad desea retirar?: ")
    ret=int(saldo)-nsaldo
    if nsaldo<0:
        print("No hay saldo suficiente")
        return
    else:
        strDomain = ""
        domain = []

        file = open("clientes.txt", "r")
        for l in file: domain.append(l.strip('\n\r').split(" "))
        file.close()

        for i in domain:
            if i[0] == cuenta:
                #print "QQQQQQQQQQQQQQQ" + cuenta
                i[4] = str(nsaldo)
            strDomain+= " ".join(i) + "\n"

        file = open("clientes.txt", "w")
        file.write(strDomain);
        file.close()
        
        print "Su nuevo saldo es de %d" % nsaldo

        if(raw_input("Desea imprimir el recibo? si/no")== "si" or "Si"):
            toWrt = """************ Banco IME ***************
Numero de cuenta: %s
Usuario: %s
Su retiro fue de %s
Su saldo actual es de %s
Gracias por su preferencia
**********************************
""" % (cuenta, nombre, ret, nsaldo)
            print "Impreso"
        file=open("retiro.txt","w")
        file.write(toWrt)
        file.close()
        return nsaldo


def nip(cuenta):   
    strDomain = ""
    domain = []

    newNip = raw_input("Inserte su nuevo nip: ")

    file = open("clientes.txt", "r")
    for l in file: domain.append(l.strip('\n\r').split(" "))
    file.close()

    for i in domain:
        if i[0] == cuenta:
            i[3] = newNip
            
        strDomain+= " ".join(i) + "\n"

    file = open("clientes.txt", "w")
    file.write(strDomain);
    file.close()
    print "Su NIP ha sido cambiado"

def gasolina(saldo, nombre, apellido, cuenta):
    print "Su saldo es canjeable por: "
    saldo = int(saldo)
    diesel = int(17.37)
    magna = int(16.50)
    premium = int(18.24)
    print "Diesel", diesel,"$ \nMagna",magna, "$ \nPremium",premium, "$" 
    
    ndiesel = saldo/diesel
    nmagna = saldo/magna
    npremium = saldo/premium
    
    print "litros de diesel con el saldo actual es ",str(ndiesel), "litros."
    print "litros de gasolina magna disponible con el saldo actual es ",str(nmagna), "litros."
    print "litros de gasolina Premium disponible con el saldp actual es ", str(npremium), "litros."

    print "¿Desea comprar gasolina (si/no)?"
    gas = raw_input().lower()
    if gas == "si":
        compra = raw_input("\n¿Cual es la gasolina quiere comprar?(Magna, Premium o diesel)\n").lower()
        if compra == "diesel":
            litros= int(input("\n¿Cuantos litros desea?\n"))
            c=litros*diesel
            print "Total de",c,"$"
            
            nsaldo = int(saldo)-c
            ret=int(saldo)-nsaldo
            if nsaldo<0:
                print("No hay saldo suficiente")
                return
            else:
                strDomain = ""
                domain = []

                file = open("clientes.txt", "r")
                for l in file: domain.append(l.strip('\n\r').split(" "))
                file.close()

                for i in domain:
                    if i[0] == cuenta:
                        #print "QQQQQQQQQQQQQQQ" + cuenta
                        i[4] = str(nsaldo)
                    strDomain+= " ".join(i) + "\n"
                    strDomain.rstrip()

                file = open("clientes.txt", "w")
                file.write(strDomain);
                file.close()
        
                print "Su nuevo saldo es de: %d " % nsaldo

                if(raw_input("Desea imprimir el recibo? si/no \n") == "si" or "Si"):
                    toWrt = """************ Banco IME ***************
                    Numero de cuenta: %s
                    Usuario: %s
                    Su retiro fue de %s
                    Su saldo actual es de %s
                    Gracias por su preferencia
                    **********************************
                    """ % (cuenta, nombre, ret, nsaldo)
                
                print "Impreso"
                file=open("retiro.txt","w")
                file.write(toWrt)
                file.close()
                return nsaldo
 ###############################################################################           
           
        elif compra == "premium":
            litros= int(input("\n¿Cuantos litros desea?\n"))
            x=litros*premium
            print "Total de",x,"$"
            
            nsaldo = int(saldo)-x
            ret=int(saldo)-nsaldo
            if nsaldo<0:
                print("No hay saldo suficiente")
                return
            else:
                strDomain = ""
                domain = []

                file = open("clientes.txt", "r")
                for l in file: domain.append(l.strip('\n\r').split(" "))
                file.close()

                for i in domain:
                    if i[0] == cuenta:
                        #print "QQQQQQQQQQQQQQQ" + cuenta
                        i[4] = str(nsaldo)
                    strDomain+= " ".join(i) + "\n"
                    strDomain.rstrip()

                file = open("clientes.txt", "w")
                file.write(strDomain);
                file.close()
        
                print "Su nuevo saldo es de: %d " % nsaldo

                if(raw_input("Desea imprimir el recibo? si/no \n") == "si" or "Si"):
                    toWrt = """************ Banco IME ***************
                    Numero de cuenta: %s
                    Usuario: %s
                    Su retiro fue de %s
                    Su saldo actual es de %s
                    Gracias por su preferencia
                    **********************************
                    """ % (cuenta, nombre, ret, nsaldo)
                
                print "Impreso"
                file=open("retiro.txt","w")
                file.write(toWrt)
                file.close()
                return nsaldo
            
            
        elif compra == "magna":
            litros= int(input("\n¿Cuantos litros desea?\n"))
            y=litros*magna
            print "Total de",y,"$"
            
            nsaldo = int(saldo)-y
            ret=int(saldo)-nsaldo
            if nsaldo<0:
                print("No hay saldo suficiente")
                return
            else:
                strDomain = ""
                domain = []

                file = open("clientes.txt", "r")
                for l in file: domain.append(l.strip('\n\r').split(" "))
                file.close()

                for i in domain:
                    if i[0] == cuenta:
                        #print "QQQQQQQQQQQQQQQ" + cuenta
                        i[4] = str((nsaldo))
                    strDomain+= " ".join(i) + "\n"
                    strDomain.rstrip()

                file = open("clientes.txt", "w")
                file.write(strDomain);
                file.close()
        
                print "Su nuevo saldo es de: %d " % nsaldo

                if(raw_input("Desea imprimir el recibo? si/no \n") == "si" or "Si"):
                    toWrt = """************ Banco IME ***************
                    Numero de cuenta: %s
                    Usuario: %s
                    Su retiro fue de %s
                    Su saldo actual es de %s
                    Gracias por su preferencia
                    **********************************
                    """ % (cuenta, nombre, ret, nsaldo)
                
                print "Impreso"
                file=open("retiro.txt","w")
                file.write(toWrt)
                file.close()
                return nsaldo
            
        elif gas == "no":
            print "Regrese pronto."
        else:
            print "Error"
    

def menu():
    print "Bienvenido"
    datos=logIn()
    if datos != None:
        while True:
            print "\n************ Banco IME ***********"
            print "Cliente:", datos[1], datos[2]
            print "\n1 Consulta saldo"       #linea 80
            print "2 Deposito"
            print "3 Retiro"
            print "4 Cambio de NIP"
            print "5 Costo de gasolina"
            print "6 Salir\n"
            op=input("Elige una opcion: ")
            if op==1:
                consultaSaldo(datos[-1], datos[1], datos[2], datos[0])
            elif op==2:
                datos[-1]=deposita(datos[-1], datos[1], datos[2], datos[0])
            elif op==3:
                datos[-1]=retiro(datos[-1], datos[1], datos[2], datos[0])   
            elif op==4:
                nip(datos[0])
                
            elif op == 5:
                gasolina(datos[-1], datos[1], datos[2], datos[0])
                
            elif op==6:
                print "Hasta luego"
                return
            else:
                print "Seleccione una opcion válida"
        
          #linea 100

menu()