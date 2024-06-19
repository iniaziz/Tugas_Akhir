# Polymorphism

class mobil:
  def __init__(self, merek, jenis):
    self.merek = merek
    self.jenis = jenis

  def berkendara(self):
    print("\nBerkendara dengan", self.merek, "model", self.jenis)

class kapal_laut:
  def __init__(self, merek, jenis):
    self.merek = merek
    self.jenis = jenis

  def berkendara(self):
    print("Berselancar dengan", self.merek, "model", self.jenis)

class Kapal_terbang:
  def __init__(self, merek, jenis):
    self.merek = merek
    self.jenis = jenis

  def berkendara(self):
    print("Terbang dengan", self.merek, "model", self.jenis, "\n****************************")

mobil1 = mobil("Bugatti", "Chiron")
kapal_laut1 = kapal_laut("Sea Ray", "SPX 190")
Kapal_terbang1 = Kapal_terbang("Airbus", "A320")

for i in (mobil1, kapal_laut1, Kapal_terbang1):
  i.berkendara()