from animal import animal
class carnivora(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, lama_hidup, maksimal_massa):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.lama_hidup = lama_hidup
        self.maksimal_massa = maksimal_massa
        
    def info_carnivora(self):
        super().info_animal()
        print("Lama hidup \t\t\t: ", self.lama_hidup, 
            "\nMaksimal massa tubuh\t\t: ", self.maksimal_massa)


Carnivora = carnivora(" Piranha", "ikan, bangkai, dan hewan lain", "Laut", "Bertelur", "10-25 tahun", "7 pound")
Carnivora.info_carnivora()

print()
Carnivora2 = carnivora(" Harimau", "babi hutan, rusa, dll", "Hutan", "Melahirkan", "10-15 tahun", "310 kg")
Carnivora2.info_carnivora()

print()
Carnivora3 = carnivora(" Komodo", "Daging", "Darat", "Bertelur", "50 tahun", "90 kg")
Carnivora3.info_carnivora()

