from animal import animal

class mamalia(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_kulit, jenis_gigi):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_kulit = jenis_kulit
        self.jenis_gigi = jenis_gigi

    def info_mamalia(self):
        super().info_animal()
        print("Ciri fisik \t\t\t: ", self.jenis_kulit, 
            "\nJenis gigi\t\t: ", self.jenis_gigi)  
        
Mamalia = mamalia(" kelelawar", "buah", "gua", "melahirkan", "berbulu", "gigi seri dan taring")
Mamalia.info_mamalia()

Mamalia2 = mamalia(" sapi", "rumput", "peternakan", "melahirkan", "berbulu", "seri, taring dan geraham")
Mamalia2.info_mamalia()

Mamalia3 = mamalia(" lumba-lumba", "ikan kecil", "laut", "melahirkan", "tidak berbulu", "gigi berbentuk kerucut")
Mamalia3.info_mamalia()
