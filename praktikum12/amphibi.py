from animal import animal

class amphibi(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jenis_air, bernapas):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jenis_air = jenis_air
        self.bernapas = bernapas

    def info_amphibi(self):
        super().info_animal()
        print("Jenis air \t\t\t: ", self.jenis_air, 
            "\nBernapas menggunakan\t\t: ", self.bernapas)

Amphibi = amphibi(" katak", "serangga", "dua alam", "bertelur", "air tawar", "kulit dan paru-paru")
Amphibi.info_amphibi()

print()
Amphibi2 =amphibi(" kadal air", "kecebong", "dua alam", "bertelur", "air tawar", "paru-paru, kulit, dan rongga mulut")
Amphibi2.info_amphibi()

print()
Amphibi3 =amphibi(" salamander", "ikan", "dua alam", "bertelur dan melahirkan", "air tawar", "paru-paru dan insang")
Amphibi3.info_amphibi()
