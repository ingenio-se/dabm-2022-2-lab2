# -*- coding: utf-8 -*-

class Menu:
    def __init__(self,laboratorio):
        self.laboratorio = laboratorio
        
        
    def ver(self):
        print("BIENVENIDO AL SISTEMA".center(50,"*"))
        print("Laboratorio:"+self.laboratorio)
        print("1.Tecnicos")
        print("2.Estudiantes")
        print("3.Salir")
        op=input(">>>")
        
        return op
    
class MenuTecnicos:
    def ver(self):
        print("MENU TECNICOS DE LABORATORIO".center(20,"*"))
        print("1.Registrar equipos")
        print("2.Registrar prestamo")
        print("3.Registrar mantenimiento")
        print("4.Registrar entrega")
        op=input(">>>")
        
        return op

class MenuEstudiantes:
    def ver(self):
        print("MENU ESTUDIANTES".center(20,"*"))
        print("1.Mis prestamos")
        print("2.Consultar equipos")
        op=input(">>>")
        
        return op
    
if __name__=='__main__':
    m =Menu("xxxx")
    m.ver()