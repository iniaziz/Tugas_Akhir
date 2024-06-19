# class

class manusia:
    def __init__(self,nama, prodi, nim):
        self.nama = nama
        self.prodi = prodi
        self.nim = nim
    
    def hello(self):
        print(f"\nNama saya {self.nama}, saya berasal dari prodi {self.prodi}, NIM saya adalah {self.nim}")
        print("********************************************************************************************")

manusia1 = manusia("Aziz", "Teknik Informatika", 230403010050)
manusia2 = manusia("Pandu", "PGSD", 230403010310)
manusia3 = manusia("Furqon", "Manajemen", 230403010230)
manusia1.hello()
manusia2.hello()
manusia3.hello()