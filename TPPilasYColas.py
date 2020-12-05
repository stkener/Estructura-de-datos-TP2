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

from tdaPilasColas import * 
from funcionesAuxiliares import * 

##################################################################
######################## TDA AUXILIO #############################
##################################################################

class Auxilio:
  def __init__(self, patente, zonaPartida, zonaDestino, tipo, estado):
    self.patente = validarPatente(patente)
    self.zonaPartida = ZonaAuxilio(zonaPartida)
    self.zonaDestino = ZonaAuxilio(zonaDestino)
    self.tipo = TipoAuxilio(tipo)
    self.estado = EstadoAuxilio(estado)
    
  def __repr__(self):
    cadenaPrint = "Patente:" + str(self.patente) + " Partida:" + self.zonaPartida.name + " Destino:" + self.zonaDestino.name + " Tipo:" + self.tipo.name + " Estado:" + self.estado.name
    return cadenaPrint        

##################################################################
################## TDA OFICINA DE ATENCION #######################
##################################################################

class OficinaAtencion:
  def __init__(self, nroInterno, cantCritica):
    if nroInterno in range(1, 999):
      self.nroInterno = nroInterno
    self.cantCritica = cantCritica  
    self.colaRemolques = Queue()
    self.colaReparacion = Queue()

  '''recibirAuxilio(auxilio): Agrega el auxilio que recibe por parámetro a la cola que corresponde
  a su tipo. Si se excede la cantidad crítica en alguna cola, se almacena el auxilio, pero
  se debe informar por pantalla la situación.'''

  def recibirAuxilio(self, auxilio):
    if auxilio.tipo == TipoAuxilio(TipoAuxilio.Remolque).value:                                     
      self.colaRemolques.enqueue(auxilio)
      if self.colaRemolques.tamanioCola() > self.cantCritica:
        print("Cantidad de auxilios critica en Remolques")
    elif auxilio.tipo == TipoAuxilio(TipoAuxilio.Reparacion).value:                               #con reparacion tira Attribute Error: Reparador
      self.colaReparacion.enqueue(auxilio)
      if self.colaReparacion.tamanioCola() > self.cantCritica:
        print("Cantidad de auxilios critica en Reparaciones")

  '''primerAuxilioAEnviar(): Retorna el primer auxilio a enviar a los conductores de las
  grúas. Si hay auxilios de Remolque, devuelve el primer pedido de auxilio a extraer de la
  cola correspondiente, caso contrario, el auxilio a extraer de la cola de Reparaciones. No
  desencola el pedido, solo lo muestra.'''
  
  def primerAuxilioAEnviar(self): 
    if not self.colaRemolques.estaVacia():
      auxilioAEnviar = self.colaRemolques.top()
    else:
      auxilioAEnviar = self.colaReparacion.top()
    return auxilioAEnviar
      
  '''enviarAuxilio(zonaDeGrua): Recibe por parámetro la zona en donde se encuentra una
  grúa y desencola y retorna el primer auxilio que se le puede enviar. El auxilio debe tener como
  zona de partida la zona en la que esta la grúa (zonaDeGrua). Los pedidos de Remolque se
  tratan primero, si no hay ninguno de Remolque en la zona, se tratan los de Reparación.'''  

  def enviarAuxilio(self, zonaDeGrua):
    auxilio = 0
    for aux in range(len(self.colaRemolques.cola)):
      if ZonaAuxilio(zonaDeGrua).name == self.colaRemolques.cola[aux].zonaPartida.name:
        print(self.colaRemolques.cola[aux].zonaPartida.name)
        auxilio = self.colaRemolques.cola.pop(aux)
        break
      else:
        for aux in range(len(self.colaReparacion.cola)):
          if ZonaAuxilio(zonaDeGrua).name == self.colaReparacion.cola[aux].zonaPartida.name:
            auxilio = self.colaReparacion.cola.pop(aux)
            break
    return auxilio
 
  '''esCritica(): Retorna True si alguna de las dos colas tiene una cantidad de auxilios mayor
  que la cantidad crítica o False en caso contrario.'''

  def esCritica(self):
    return self.colaRemolques.tamanioCola() > self.cantCritica or self.colaReparacion.tamanioCola() > self.cantCritica

  '''buscarAuxilio(nroPatente): Recibe un número de patente (nroPatente) y si en alguna
  de las colas (cualquierade las dos) hay un auxilio pedido para ese vehiculo, lo retorna. El
  auxilio no debe ser eliminado de la cola.'''

  def buscarAuxilio(self, nroPatente): 
    auxilio = 0
    for aux in range(self.colaRemolques.tamanioCola()):
      if self.colaRemolques.cola[aux].patente == nroPatente:
        auxilio = self.colaRemolques.cola[aux]
    for aux in range(self.colaReparacion.tamanioCola()):
      if self.colaReparacion.cola[aux].patente == nroPatente:
        auxilio = self.colaReparacion.cola[aux]
    return auxilio   
  
  '''eliminarAuxilio(nroPatente): Recibe un número de patente (nroPatente) y si hay un
  pedido de auxilio para ese vehículo en alguna de las colas de la ocina de atención, lo elimina
  de ella.'''

  def eliminarAuxilio(self, nroPatente):
    for aux in range(self.colaRemolques.tamanioCola()):
      if self.colaRemolques.cola[aux].patente == nroPatente:
        auxilio = self.colaRemolques.cola.pop(aux)
    for aux in range(self.colaReparacion.tamanioCola()):
      if self.colaReparacion.cola[aux].patente == nroPatente:
       auxilio = self.colaRemolques.cola.pop(aux)
  
  '''auxiliosPorTipo(): Cantidad de auxilios de cada tipo (Remolque y Reparación por separado)
  y retorna ambos valores.'''  

  def auxiliosPorTipo(self):
    remolques = self.colaRemolques.tamanioCola()
    reparacion = self.colaReparacion.tamanioCola()
    print("Remolques: "+ str(remolques) +"\n"+ "Reparacion: "+ str(reparacion))

  '''cantidadTotalAuxilios(): Cantidad total de auxilios en la ocina de atención, sumando
  los de las dos colas.'''  

  def cantidadTotalDeAuxilios(self):
    cantidad = self.colaRemolques.tamanioCola() + self.colaReparacion.tamanioCola()
    return cantidad

  '''auxiliosEnEspera(): Retorna la cantidad total de auxilios (Remolque y Reparación) que
  estan en estado de Espera.'''  

  def auxiliosEnEspera(self):
    colaAux = []
    for aux in range(self.colaRemolques.tamanioCola()):
      if self.colaRemolques.cola[aux].estado == "Espera":
        cosa = self.colaRemolques.cola[aux]
        colaAux.append(cosa)
    for aux in range(self.colaReparacion.tamanioCola()):
      if self.colaRemolques.cola[aux].estado == "Espera":
        cosa = self.colaReparacion.cola[aux]
        colaAux.append(cosa)
    return len(colaAux)

  '''hayPedidoPara(nroPatente): Devuelve true o false. Si hay algun pedido para el numero de patente'''  

  def hayPedidoPara(self, nroPatente): 
    lista = []
    for aux in range(self.colaRemolques.tamanioCola()):
      if self.colaRemolques.cola[aux].patente == nroPatente:
        dato = self.colaRemolques.cola[aux]
        lista.append(dato)
    for aux in range(self.colaReparacion.tamanioCola()):
      if self.colaReparacion.cola[aux].patente == nroPatente:
       dato = self.colaReparacion.cola[aux]
       lista.append(dato)
    return len(lista) > 0

  '''cambiaDeTipo(nroPatente): Cambia el tipo del auxilio del vehículo con la patente nro-
  Patente (de Reparación a Remolque o viceversa), en consecuencia, debe cambiarlo de
  cola. La operación debe verificar previamente que exista un pedido de auxilio para ese
  vehiculo en la oficina.'''

  def cambiaDeTipo(self, nroPatente):
    if self.hayPedidoPara(nroPatente):                              #se fija si ese nro de patente esta en alguna lista, lo pide en el tp
     for aux in range(self.colaRemolques.tamanioCola()):                     # recorre la lista
      if self.colaRemolques.cola[aux].patente == nroPatente:             # compara patentes
        dato = self.colaRemolques.cola.pop(aux)                          # saca de la lista y guarda el dato
        self.colaReparacion.enqueue(dato)                            # lo pone en la otra lista
        break
      else:                                                         #si recorrio la lista y no la encontro, recorre la otra y hace el mismo procedimiento ya descripto
        for aux in range(self.colaReparacion.tamanioCola()):
          if self.colaReparacion.cola[aux].patente == nroPatente:
            dato = self.colaReparacion.cola.pop(aux)
            self.colaRemolques.enqueue(dato)
            break

###################################################################
######################## TDA EDIFICIO #############################
###################################################################

class EdificioEmpresa:
  def __init__(self, cantPisos, nroHabitaculos):
    self.cantPisos = cantPisos
    self.nroHabitaculos = nroHabitaculos
    self.Edificio = self.creacion()
    
    
  def creacion(self):                     # esto es para hace y llenar la matriz. la matriz seria pisos, que esta dividida arriba. 
    pisos = []
    habitaculos = []
    for i in range(self.cantPisos):         
      pisos.append(habitaculos)            
      for j in range(self.nroHabitaculos):
        habitaculos.append(None)
    return pisos

  '''establecerOficina(numeroPiso, numeroHabitaculo, oficinaAtencion): Pone la ofi-
  cinaAtencion en habitáculo correspondiente.'''  

  def establecerOficina(self, piso, habitaculo, oficina): 
    if self.Edificio[piso][habitaculo] == None:
      self.Edificio[piso][habitaculo] = oficina
    else:
      print("El habitaculo esta ocupado")
  
  '''cantidadDeOficinasCriticas(piso): Operación recursiva que retorna la cantidad de ofi-
  cinas en situación crítica en el piso que recibe por parámetro.'''  

  def cantidadDeOficinasCriticas(self, piso): 
    cantidad = 0
    for i in range(self.nroHabitaculos):              #la logica seria, que revise los habitaculos del piso. desp que se fije que no este vacio
     if self.Edificio[piso][i] != None:               # desp, si no esta vacio, que se fije si es critica, si es asi suma 1 a cantidad, y devuelve cantidad.
       if self.Edificio[piso][i].esCritica():
         cantidad = cantidad + 1
    return cantidad

  '''oficinaMenosRecargada(): Retorna la ubicación (número de piso y número de habitáculo)
  de la oficina que tiene el menor número de auxilios de tipo Remolque pendientes en todo
  el edificio.'''  

  def oficinaMenosRecargada(self):                              
    losMenosCriticosXPiso = []
    for i in range(self.cantPisos):                              #con esto recorro pisos
      for j in range(self.nroHabitaculos):                      #con esto habitaculos
       dato = self.Edificio[i][j].colaRemolques.tamanioCola()        
       losMenosCriticosXPiso.append(dato)
    
    ordenamientoRapido(losMenosCriticosXPiso)
    for x in range(self.cantPisos):
      for y in range(self.nroHabitaculos):
        if self.Edificio[x][y].colaRemolques.tamanioCola() == losMenosCriticosXPiso[0]:
          return x, y
          break

  '''buscaOficina(nroInterno): Recibe el número de interno y retorna la ubicación de la
  oficina en el edificio (número de piso y número de habitáculo).'''  

  def buscaOficina(self, nroInterno):
    pisoYOf = []
    for i in range(self.cantPisos):
      for j in range(self.nroHabitaculos):
        if self.Edificio[i][j].nroInterno == nroInterno:
          pisoYOf.append(i)
          pisoYOf.append(j)
          return pisoYOf             

  '''moverAuxilio(nroPatente, internoOficinaOrigen, internoOficinaDestino): Saca el
  auxilio del vehículo con patente nroPatente de la oficina internoOficinaOrigen y lo pasa
  a la oficina de internoOficinaDestino.'''  

  def moverAuxilio(self, nroPatente, internoOficinaOrigen, internoOficinaDestino):
    auxilio = 0
    for i in range(self.cantPisos):
      for j in range(self.nroHabitaculos):
        auxilio = self.Edificio[i][j].buscarAuxilio(nroPatente)
        if auxilio != 0:
          self.Edificio[i][j].eliminarAuxilio(nroPatente)
          coordenadas = self.buscaOficina(internoOficinaDestino)
          self.Edificio[coordenadas[0]][coordenadas[1]].recibeAuxilio(auxilio)
        