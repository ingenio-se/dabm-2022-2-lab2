# -*- coding: utf-8 -*-
'''
DAVID GUERRA
DABM -2022-2
'''



from classes.menu import *
from classes.equipo import *
from classes.prestamo import *

def main():
    menu = Menu("Escuela de Ingenieria")
    op=menu.ver()
    if op == "1":
        menu2 = MenuTecnicos()
        op2=menu2.ver()
        if op2 =="1":
            e=crearEquipo()
            e.save()
        elif op2 =="2":
            p=crearPrestamo()
            p.save()
        elif op2=="3":
            registroMantenimiento()
        elif op2=="4":
            registroEntrega()
        else:
            print("Opción inválida")
            main()
    
    elif op=="2":
        menu2=MenuEstudiantes()
        op2=menu2.ver()
        if op2=="1":
            verPrestamos()
        elif op2=="2":
            consultarEquipo()
    
    elif op=="3":
        exit()
            
    main()


if __name__=='__main__':
    
    main()
