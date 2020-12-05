# -*- coding: utf-8 -*-
"""TP_pilasColas_scriptPrueba.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ptQqES6N2kCj9ChTXYJVdOoog-RzCOS1
"""
from TPPilasYColas import * 
################################################################################
###########################SCRIPT DE PRUEBA#####################################
################################################################################

#############################IMPORTANTE!!!!!!###################################
#############COSAS PARA CONTROLAR ANTES DE EJECUTAR ESTA PRUEBA#################
#############################IMPORTANTE!!!!!!###################################

#Si usan Enums, los tienen que definir asi (respetar nombres y numeros asociados a cada uno):
#class ZonaAuxilio(int,Enum):
#  Sur = 0
#  Norte = 1
#  Este = 2
#  Oeste = 3
#  CABA = 4
#class TipoAuxilio(int,Enum):
#  Remolque = 0
#  Reparacion = 1
#class EstadoAuxilio(int,Enum):
#  Espera = 0
#  Aprobado = 1

#En la parte donde se cargan los datos de las oficinas: Comenten o descomenten los
#bloques de codigo indicados, segun usen o no usen Enums en sus implementaciones

#Orden de variables en constructores (__init__):
#TDA Auxilio: self, patente, zonaPartida, zonaDestino, tipo, estado
#TDA OficinaAtencion: self, nroInterno, cantCritica
#TDA EdificioEmpresa: self, cantPisos, cantHabitaculos

#Mantengan nombres de TDAs, operaciones y orden de parametros en las operaciones
#segun lo que esta definido en el enunciado

#Para ver mejor la salida pueden comentar la parte que imprime cuando la oficinaAtencion 
#llega a la cantidad critica en la operacion recibirPedido

########################Definicion de variables#################################
#################IMPORTANTE: NO MODIFICAR ESTAS VARIABLES!!!!!!!!!!!!!!!!!!!!!!!
nroPisos = 15
nroHabitaculos = 8
zonas = ["Sur","Norte","Este","Oeste","CABA"]
tipos = ["Remolque","Reparacion"]
estados = ["Espera","Aprobado"]
oficinasData = {}
primerosAuxiliosPorInterno = {}
primerosAuxiliosDesdeCABA = {}

################################################################################
##############Creacion de edificio y carga de oficinas##########################
################################################################################

####################Lectura de archivo con datos de auxilios####################
auxiliosFile = open('TP_pilasColas_datosPrueba.csv')
for auxilio in auxiliosFile:
  auxilioData = auxilio[:-1].split(',')
  interno = int(auxilioData[0])
  if interno in oficinasData:
    oficinasData[interno][1].append(auxilioData[4:])
  else:
    oficinasData[interno] = []
    oficinasData[interno].append(auxilioData[1:4])
    oficinasData[interno].append([auxilioData[4:]])
auxiliosFile.close() 
################################################################################

######################Creacion de edificio######################################
edificioDeEmpresa = EdificioEmpresa(nroPisos, nroHabitaculos)
################################################################################

######################Carga de oficinas#########################################
for interno in oficinasData:
  oficinaData = oficinasData[interno][0]
  cantCritica = int(oficinaData[0])
  nroPiso = int(oficinaData[1])
  nroHabitaculo = int(oficinaData[2])

  ############Creacion de oficina################
  oficina = OficinaAtencion(interno, cantCritica)
  
  ############Carga de auxilios a oficina########
  for auxilioData in oficinasData[interno][1]:
    patente = auxilioData[0]
    
    ###################Para uso con Enum########################################
    partida = ZonaAuxilio(zonas.index(auxilioData[2]))                          ###Comentar si usan strings 
    destino = ZonaAuxilio(zonas.index(auxilioData[3]))                          ###Comentar si usan strings
    tipo = TipoAuxilio(tipos.index(auxilioData[1]))                             ###Comentar si usan strings
    estado = EstadoAuxilio(estados.index(auxilioData[4]))                       ###Comentar si usan strings
    ############################################################################

    ###################Para uso con strings#####################################
    #partida = auxilioData[2]                                                   ###Comentar si usan Enums
    #destino = auxilioData[3]                                                   ###Comentar si usan Enums
    #tipo = auxilioData[1]                                                      ###Comentar si usan Enums
    #estado = auxilioData[4]                                                    ###Comentar si usan Enums
    ############################################################################

    ##############Creacion de auxilio#########################
    auxilio = Auxilio(patente, partida, destino, tipo, estado)
    ##############Envio de auxilio a oficina##################
    oficina.recibirAuxilio(auxilio)
  
  ################Ubicacion de oficina en edificio####################
  edificioDeEmpresa.establecerOficina(nroPiso, nroHabitaculo, oficina)

  ##############################################################################
  ##########Ejecucion de pruebas de operaciones de TDA OficinaAtencion##########
  ##############################################################################

  ##########################primerAuxilioAEnviar################################
  primerosAuxiliosPorInterno[interno] = oficina.primerAuxilioAEnviar()
  
  ##########################enviarAuxilio#######################################
  #####################Para uso con Enum########################################
  auxilioAEnviar = oficina.enviarAuxilio(ZonaAuxilio(zonas.index("CABA")))      ###Comentar si usan strings
  ##############################################################################

  #####################Para uso con strings#####################################
  #auxilioAEnviar = oficina.enviarAuxilio("CABA")                               ###Comentar si usan Enums
  ##############################################################################

  primerosAuxiliosDesdeCABA[interno] = auxilioAEnviar
  #print(auxilioAEnviar)
  oficina.recibirAuxilio(auxilioAEnviar)
################################################################################

#############################Impresion de edificio##############################
print("Edificio de empresa:\n")
print(edificioDeEmpresa)
print("-----------------------------------------------------------------------\n")

################################################################################
############Impresion de pruebas de operaciones de TDA OficinaAtencion##########
################################################################################

for interno in primerosAuxiliosPorInterno:
  ##########################primerAuxilioAEnviar################################
  print("Primer auxilio a enviar en oficina", interno, ":", primerosAuxiliosPorInterno[interno])
  
  ##########################enviarAuxilio#######################################
  print("Primer auxilio enviado desde CABA en oficina", interno, ":", primerosAuxiliosDesdeCABA[interno])

print("-----------------------------------------------------------------------\n")
  
################################################################################
################Prueba de operaciones de TDA EdificioEmpresa####################
################################################################################

#######################cantidadDeOficinasCriticas###############################
print("\n\nCantidades de oficinas criticas en cada piso:\n")
for nroPiso in range(nroPisos):
  print("Piso",nroPiso,":",edificioDeEmpresa.cantidadDeOficinasCriticas(nroPiso))  
print("-----------------------------------------------------------------------")

#########################oficinaMenosRecargada##################################
print("\n\nOficina menos recargada:\n")
print(edificioDeEmpresa.oficinaMenosRecargada())  
print("-----------------------------------------------------------------------")

#########################buscaOficina###########################################
print("\n\nUbicacion de cada oficina en el edificio:\n")
for interno in oficinasData:
  print("Interno",interno,":",edificioDeEmpresa.buscaOficina(interno))  
print("-----------------------------------------------------------------------")

#########################moverAuxilio###########################################
print("\n\nMovimiento de auxilios de oficina 118 (piso cero) a oficina 136 (piso dos):\n")
print("Cantidad de oficinas criticas en piso cero antes:",edificioDeEmpresa.cantidadDeOficinasCriticas(0))
print("Cantidad de oficinas criticas en piso dos antes:",edificioDeEmpresa.cantidadDeOficinasCriticas(2))

for auxilioData in oficinasData[118][1]:
  patente = auxilioData[0]
  edificioDeEmpresa.moverAuxilio(patente,118,136)
 
print("\nCantidad de oficinas criticas en piso cero despues:",edificioDeEmpresa.cantidadDeOficinasCriticas(0))
print("Cantidad de oficinas criticas en piso dos despues:",edificioDeEmpresa.cantidadDeOficinasCriticas(2))
print("-----------------------------------------------------------------------")