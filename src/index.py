from varasto import Varasto


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")


    olut_getterit(olutta)
    mehu_setterit(mehua)

    virhe_tilanteita()

    olut_varasto_lisays(olutta, 1000.0)
    mehu_varasto_lisays(mehua, -666.0)
    olut_varasto_otto(olutta, 1000.0)
    mehu_varasto_otto(mehua, -32.9)

def mehu_setterit(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")


def olut_getterit(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")


def virhe_tilanteita():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)


def mehu_varasto_lisays(mehua, lisays):
    print(f"Mehuvarasto: {mehua}")
    print(f"mehua.lisaa_varastoon({lisays})")
    mehua.lisaa_varastoon(lisays)
    print(f"Mehuvarasto: {mehua}")

def olut_varasto_lisays(olutta, lisays):
    print(f"Olutvarasto: {olutta}")
    print(f"olutta.lisaa_varastoon({lisays})")
    olutta.lisaa_varastoon(lisays)
    print(f"Olutvarasto: {olutta}")

def olut_varasto_otto(olutta, otto ):
    print(f"Olutvarasto: {olutta}")
    print(f"olutta.ota_varastosta({otto})")
    saatiin = olutta.ota_varastosta(otto)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

def mehu_varasto_otto(mehua, otto):
    print(f"Mehuvarasto: {mehua}")
    print(f"mehua.otaVarastosta({otto})")
    saatiin = mehua.ota_varastosta(otto)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")

if __name__ == "__main__":
    main()
