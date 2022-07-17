import json
from clases import cliente
from clases import direccion
from clases import cuenta
# lo q hace esta clase es parsearme el json para que lo pueda usar 
class Parser():
    #creo el constructor
    def __init__(self,file):
        self.file=file
        #se ejecuta este metodo q defino para levantar el json
        self.load()
        self.get_cliente()
        self.eventos = self.data['transacciones']
        # metodo para levantar el json,obtngo el diccionario parseado
        
    def load(self):
        f=open(self.file)
        self.data=json.load(f)
        f.close()
    
    def get_cliente(self):
        if self.data['tipo'] == 'BLACK':
            self.cliente=cliente.ClienteBlack(self.data)
            self.cliente.crear_cuenta(cuenta.Cuenta(100000,100000000,-1,0,0))
            self.cliente.crear_cuenta(cuenta.Cuenta(100000,100000000,-1,0,0))
            self.cliente.crear_cuenta(cuenta.Cuenta(100000,100000000,-1,0,-10000))
        elif self.data['tipo'] == 'GOLD':
            self.cliente=cliente.ClienteGold(self.data)
            self.cliente.crear_cuenta(cuenta.Cuenta(20000,500000,-1,0.005,0))
            self.cliente.crear_cuenta(cuenta.Cuenta(20000,500000,-1,0.005,0))
            self.cliente.crear_cuenta(cuenta.Cuenta(20000,500000,-1,0.005,-10000))
        else:
            self.cliente=cliente.ClienteClassic(self.data)
            self.cliente.crear_cuenta(cuenta.Cuenta(10000,150000,-1,0.01,0))
