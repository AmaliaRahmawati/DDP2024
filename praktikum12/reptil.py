from animal import animal

class reptil(animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, jumlah_kaki, berbisa):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.jumlah_kaki = jumlah_kaki
        self.berbisa = berbisa

    def info_reptil(self):
        super().info_animal()
        print("Jumlah kaki \t\t\t: ", self.jumlah_kaki, 
            "\nBerbisa atau tidak\t\t: ", self.berbisa)

Reptil = reptil(" Buaya", "burung, katak, dll", "air tawar", "bertelur", "4", "tidak")
Reptil.info_reptil()

print()
Reptil = reptil(" Ular", "Daging dan hewan lain", "rawa, hutan", "bertelur", "0", "berbisa")
Reptil.info_reptil()

print()
Reptil = reptil(" Bunglon", "serangga", "hutan hujan", "bertelur dan melahirkan", "4", "tidak")
Reptil.info_reptil()
