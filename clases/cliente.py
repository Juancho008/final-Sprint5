from clases.direccion import Direccion

class Cliente:
    def __init__(self,data):
        self.tipo=data['tipo']
        self.dni=data['dni']
        self.numero = data['numero']
        self.nombre=data['nombre']
        self.apellido=data['apellido']
        self.tarjeta_debito = True
        self.cuentas = []
        self.direccion = Direccion(data['direccion'])
        print('Se creo cliente: '+self.dni)
        
    def crear_cuenta(self,cuenta):
        self.cuentas.append(cuenta)
        
    def puede_comprar_dolar(self):
        return True
    
    def puede_crear_tarjeta_credito(self,tarjetas):
        return False 
    
    def puede_crear_chequera(self,chequeras):
        return False

class ClienteGold(Cliente):

    def __init__(self, data):
        print('Se creo gold')  
        super().__init__(data)
        
    def puede_crear_tarjeta_credito(self,tarjetas):

        return tarjetas < 1
   
    def puede_crear_chequera(self,chequeras):
        return chequeras < 1
           

class ClienteClassic(Cliente):
    
    def __init__(self, data):
        print('Se creo classic')
        super().__init__(data) 
        
    def puede_comprar_dolar(self):
        return False

class ClienteBlack(Cliente):
    def __init__(self, data):
        print('Se creo black')
        super().__init__(data)
    
    def puede_crear_tarjeta_credito(self,tarjetas):
        return tarjetas < 5
   
    def puede_crear_chequera(self,chequeras):
        return chequeras < 2


