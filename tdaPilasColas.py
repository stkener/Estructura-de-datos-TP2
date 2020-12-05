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
######################### TDA PILA ###############################
##################################################################

class Stack:
  def __init__(self, startStack = None):
    self.pila = []
    if startStack:
      for elemento in startStack:
        self.pila.append(elemento)
 
  def vaciar(self):
    self.pila.clear()
 
  def push(self, elemento):
    self.pila.append(elemento)
 
  def estaVacia(self):
    return len(self.pila) == 0
 
  def pop(self):
    elemento = None
    if not self.estaVacia():
      elemento = self.pila.pop()
    return elemento
 
  def top(self):
    elemento = None
    if not self.estaVacia():
      elemento = self.pila[len(self.pila)-1]
    return elemento
 
  def clone(self):
    pilaNueva = Stack()
    for elemento in self.pila:
      pilaNueva.push(elemento)
    return pilaNueva
    
  def tamanioPila(self):
    return len(self.pila)
 
  def __repr__(self):
    return str(self.pila)

##################################################################
######################### TDA COLA ###############################
##################################################################

class Queue:
  def __init__(self, startQueue = None):
    self.cola = []
    if startQueue:
      for elemento in startQueue:
        self.cola.append(elemento)
 
  def vaciar(self):
    self.cola.clear()
 
  def enqueue(self, elemento):
    self.cola.insert(0, elemento)
 
  def estaVacia(self):
    return len(self.cola) == 0
 
  def dequeue(self):
    elemento = None
    if not self.estaVacia():
      elemento = self.cola.pop()
    return elemento
 
  def top(self):
    elemento = None
    if not self.estaVacia():
      elemento = self.cola[len(self.cola)-1]
    return elemento
 
  def clone(self):
    colaNueva = Queue()
    for elemento in self.cola:
      colaNueva.cola.append(elemento)
    return colaNueva
    
  def tamanioCola(self):
    return len(self.cola)
 
  def __repr__(self):
    return str(self.cola)