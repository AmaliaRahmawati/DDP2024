class animal():
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def info_animal(self):
        print(f'nama hewan \t\t\t:', self.name,
              "\nMakanan \t\t\t: ", self.makanan,
              "\nTempat Hidup \t\t\t: ", self.hidup,
              "\nCara berkembang biak \t\t: ", self.berkembang_biak)

# hewan = animal( "kucing garing", "cimol", "udara", "bertelur")
# hewan.info_animal()