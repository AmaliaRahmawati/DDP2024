from animal import animal

class herbivora(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jumlah_tanduk, kingdom_animalia):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jumlah_tanduk = jumlah_tanduk
        self.kingdom_animalia = kingdom_animalia

    def info_herbivora(self):
        super().info_animal()
        print("Jumlah tanduk \t\t\t: ", self.jumlah_tanduk, 
            "\nGolongan kingdom animalia\t: ", self.kingdom_animalia)

Herbivora = herbivora(" Kambing", "tumbuhan", "peternakan", "melahirkan", "2", "vertebrata")
Herbivora.info_herbivora()

print()
Herbivora = herbivora(" Belalang", "tumbuhan", "padang rumput", "bertelur", "0", "invertebrata")
Herbivora.info_herbivora()

print()
Herbivora = herbivora(" Banteng", "tumbuhan", "hutan", "melahirkan", "2", "vertebrata")
Herbivora.info_herbivora()
