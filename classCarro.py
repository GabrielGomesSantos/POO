class Carro:
    def exibir(self):
        print(f"Marca: {self.marca} \nModelo: {self.modelo}\nAno: {self.ano}")
        
carro1 = Carro() #criando uma instancia da classe carro 

carro1.marca = "Mitsubishi"
carro1.modelo = "Pajero-Tr4"
carro1.ano = 2009

carro2 = Carro() #criando outra instancia da classe carro 

carro2.marca = "Ford"
carro2.modelo = "Fiesta"
carro2.ano = 2016

carro3 = Carro() #criando outra instancia da classe carro 

carro3.marca = "chevrolet"
carro3.modelo = "Impala"
carro3.ano = 1967


carro4 = Carro() #criando outra instancia da classe carro 

carro4.marca = "supra"
carro4.modelo = "mk4"
carro4.ano = 1995


carro2.exibir()