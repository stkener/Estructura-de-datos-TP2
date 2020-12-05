##################################################################
######################## UNAHUR - 2020 ###########################
##################################################################

##################################################################
#################### ESTRUCTURAS DE DATOS ########################
##################################################################

##################################################################
##################### KENER SEBASTIAN ############################
##################################################################

##################################################################
##################### TP 2 PILAS Y COLAS #########################
##################################################################

##################################################################
###################### FUNCIONES AUXILIARES ######################
##################################################################



##################################################################
###################### VALIDACION DE PATENTE #####################
##################################################################

def validarPatente(patente):
  if len(patente) != 6:                                                             #Comprueba que el tamanio de la patente sea 6
    raise Exception("Ingrese las 3 letras y 3 numeros de la Patente sin espacios")     
  if patente[0:3].isalpha() and patente[3:6].isdigit():                             #Se fija que las primeras 3 sean letras y las ultimas 3 numeros
    return patente.upper()                                                          #El upper pone en mayuscula las letras
  else:
    raise Exception("Patente mal ingresada")

##################################################################
############# DECLARACION DE LOS TIPOS DE DATOS ENUM #############
##################################################################

from enum import Enum

class ZonaAuxilio(int, Enum):
  Sur = 0
  Norte = 1
  Este = 2
  Oeste = 3
  CABA = 4

class TipoAuxilio(int, Enum):
  Remolque = 0
  Reparacion = 1

class EstadoAuxilio(int, Enum):
  Espera = 0
  Aprobado = 1

##################################################################
################### FUNCIONES DEL ORDENAMIENTO ###################
##################################################################

def ordenamientoRapido(unaLista):
  ordenamientoRapidoAuxiliar(unaLista,0,len(unaLista)-1)
  

def ordenamientoRapidoAuxiliar(unaLista,primero,ultimo):
   if primero<ultimo:
      puntoDivision = particion(unaLista,primero,ultimo)
      ordenamientoRapidoAuxiliar(unaLista,primero,puntoDivision-1)
      ordenamientoRapidoAuxiliar(unaLista,puntoDivision+1,ultimo)


def particion(unaLista,primero,ultimo):
   valorPivote = unaLista[primero]
   marcaIzq = primero+1
   marcaDer = ultimo
   hecho = False

   while not hecho:
       while marcaIzq <= marcaDer and unaLista[marcaIzq] <= valorPivote:
           marcaIzq = marcaIzq + 1

       while unaLista[marcaDer] >= valorPivote and marcaDer >= marcaIzq:
           marcaDer = marcaDer -1

       if marcaDer < marcaIzq:
           hecho = True
       else:
           temp = unaLista[marcaIzq]
           unaLista[marcaIzq] = unaLista[marcaDer]
           unaLista[marcaDer] = temp

   temp = unaLista[primero]
   unaLista[primero] = unaLista[marcaDer]
   unaLista[marcaDer] = temp
   return marcaDer