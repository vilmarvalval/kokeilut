class Auto:
    def __init__(self, rekkari, huippu_kmh):
        self.rekkari = rekkari
        self.huippu_nop = huippu_kmh
        self.nyky_nop = 0
        self.trippi_mit = 0

auto = Auto("ABC-123", 142)

print(f"Rekirsteri: {auto.rekkari}\n"
      f"Huippunopeus: {auto.huippu_nop}\n"
      f"Nykynopeus: {auto.nyky_nop}\n"
      f"Kuljettu matka: {auto.trippi_mit}")