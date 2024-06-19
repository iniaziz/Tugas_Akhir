# method Parameter

class kampus:
    def __init__(self, nama, umur, pekerjaan, tugas):
        self.nama = nama
        self.umur = umur
        self.pekerjaan = pekerjaan
        self.tugas = tugas

class dosen(kampus):
    def dosen1(self):
        print("\nNama saya adalah", self.nama, "umur saya", self.umur, "tahun")
    def dosen2(self):
        print("Saya menjabat sebagai", self.pekerjaan)
    def dosen3(self):
        print("Tugas saya", self.tugas,"\n**************************************")

class karyawan(kampus):
    def karyawan1(self):
        print("\nNama saya adalah", self.nama, "umur saya", self.umur, "tahun")
    def karyawan2(self):
        print("Saya menjabat sebagai", self.pekerjaan)
    def karyawan3(self):
        print("Tugas saya", self.tugas,"\n**************************************")

class rektor(kampus):
    def rektor1(self):
        print("\nNama saya adalah", self.nama, "umur saya", self.umur, "tahun")
    def rektor2(self):
        print("Saya menjabat sebagai", self.pekerjaan)
    def rektor3(self):
        print("Tugas saya", self.tugas,"\n**************************************")

class satpam(kampus):
    def satpam1(self):
        print("\nNama saya adalah", self.nama, "umur saya", self.umur, "tahun")
    def satpam2(self):
        print("Saya menjabat sebagai", self.pekerjaan)
    def satpam3(self):
        print("Tugas saya", self.tugas,"\n**************************************")

manusia1 = dosen("Aziz", 25, "dosen", "mengampu mahasiswa")
manusia1.dosen1()
manusia1.dosen2()
manusia1.dosen3()

manusia2 = karyawan("Furqon", 23, "karyawan", "mengelola keuangan kampus")
manusia2.karyawan1()
manusia2.karyawan2()
manusia2.karyawan3()

manusia2 = rektor("Pandu", 15, "rektor", "menjadi presiden kampus")
manusia2.rektor1()
manusia2.rektor2()
manusia2.rektor3()

manusia2 = satpam("Wahyu", 20, "satpam", "menjaga kampus")
manusia2.satpam1()
manusia2.satpam2()
manusia2.satpam3()