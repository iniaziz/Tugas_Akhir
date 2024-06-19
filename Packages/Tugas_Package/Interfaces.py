# Interfaces

from abc import ABC, abstractmethod
class makanan(ABC):
    def type(self):
        pass
    def asal(self):
        pass
    def harga(self):
        pass

class rawon(makanan):
    def type(self):
        return "Rawon"
    def asal(self):
        return "Jawa Timur"
    def harga(self):
        return 8000
class soto(makanan):
    def type(sefl):
        return "Soto"
    def asal(self):
        return "Lamongan"
    def harga(self):
        return 7000
class pecel(makanan):
    def type(self):
        return "Pecel"
    def asal(self):
        return "Madiun"
    def harga(self):
        return 5000

def kuliner(makanan:makanan):
    print(f"\nNama makanan:{makanan.type()}")
    print(f"Asal makanan:{makanan.asal()}")
    print(f"Harga makanan:{makanan.harga()}\n***********************")

rawon = rawon();
soto = soto();
pecel = pecel();

kuliner(rawon);
kuliner(soto);
kuliner(pecel);