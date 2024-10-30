#class
#syntaxe

#marca, memoria ram, placa vidio
class computador:
    def __init__(self):
        self.marca='Asus'
        self.memoria_ram ='8gb'
        self.placa_de_vidio = 'Nvidia'
    pass
computador1 = computador()
computador2 = computador()
computador3 = computador()
print(computador1.marca,computador1.memoria_ram,computador1.placa_de_vidio)
print(computador2.marca,computador2.memoria_ram,computador2.placa_de_vidio)
print(computador3.marca,computador3.memoria_ram,computador3.placa_de_vidio)