from colorama import Style
import pandas as pd
class GetHTML():
    def __init__(self,razones,cliente):
        self.razones = razones
        self.cliente = cliente
    
    def get_html(self): 
        head = '<html><head><title>Reporte</title><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-0evHe/X+R7YkIZDRvuzKMRqM+OrBnVFBL6DOitfPri4tjfHxaWutUpFmBp4vmVor" crossorigin="anonymous"></head>'
        div =  f"<div class='container my-4'><div class='display-5 mb-3'>{self.cliente.apellido}, {self.cliente.nombre}</div> <div class=''>Nmero de cliente: {self.cliente.numero}</div>  <div class=''>DNI: {self.cliente.dni}</div> <div class=''>Direccion: {self.cliente.direccion.get_direccion()}</div></div>"
        data = pd.DataFrame(self.razones)
        html = head + div + data.to_html(classes="container table mt-30 table-bordered ",index=False,justify="left") + '</html>'
                
        self.html = html
        with open("output.html", "w") as text_file:
            text_file.write(self.html)
