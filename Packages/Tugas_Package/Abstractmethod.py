# Abstractmethod

from abc import ABC, abstractmethod
class hewan(ABC):
    @abstractmethod
    def jenis(self):
        pass
    def kriteria(self):
        pass
    def golongan(self):
        pass

class omnivora(hewan):
    def __init__(self, nama, spesies, kategori):
        self.nama = nama
        self.spesies = spesies
        self.kategori = kategori
    def jenis(self):
        return self.nama 
    def kriteria(self):
        return self.spesies
    def golongan(self):
        return self.kategori
    
class karnivora(hewan):
    def __init__(self, nama, spesies, kategori):
        self.nama = nama
        self.spesies = spesies
        self.kategori = kategori
    def jenis(self):
        return self.nama 
    def kriteria(self):
        return self.spesies
    def golongan(self):
        return self.kategori
    
class herbivora(hewan):
    def __init__(self, nama, spesies, kategori):
        self.nama = nama
        self.spesies = spesies
        self.kategori = kategori
    def jenis(self):
        return self.nama 
    def kriteria(self):
        return self.spesies
    def golongan(self):
        return self.kategori


omnivora = omnivora("Ayam" ,"unggas" , "omnivora")
print("\n"+omnivora.jenis(),"merupakan jenis hewan", omnivora.kriteria())
print(omnivora.jenis(),"termasuk spesies golongan hewan",omnivora.golongan())

karnivora = karnivora("Singa" ,"mamalia" , "karnivora")
print("************************************************\n"+karnivora.jenis(),"merupakan jenis hewan", karnivora.kriteria())
print(karnivora.jenis(),"termasuk spesies golongan hewan",karnivora.golongan())

herbivora = herbivora("sapi" ,"mamalia" , "herbivora")
print("************************************************\n"+herbivora.jenis(),"merupakan jenis hewan", herbivora.kriteria())
print(herbivora.jenis(),"termasuk spesies golongan hewan",herbivora.golongan(),"\n************************************************")