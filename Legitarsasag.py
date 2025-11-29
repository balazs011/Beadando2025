from JegyFoglalas import JegyFoglalas

class Legitarsasag:
    def __init__(self, nev):
        self._nev = nev
        self._jaratok = []
        self._foglalasok = []

    @property
    def nev(self):
        return self._nev

    def jarat_hozzaadasa(self, jarat):
        self._jaratok.append(jarat)

    def get_jaratok(self):
        return self._jaratok

    def jegy_foglalas(self, jaratszam, utas_nev):
        for jarat in self._jaratok:
            if jarat.jaratszam == jaratszam:
                uj_foglalas = JegyFoglalas(jarat, utas_nev)
                self._foglalasok.append(uj_foglalas)
                return jarat.jegyar
        raise ValueError("Nincs ilyen járatszám!")

    def foglalas_lemondasa(self, jaratszam, utas_nev):
        for foglalas in self._foglalasok:
            if foglalas.jarat.jaratszam == jaratszam and foglalas.utas_nev == utas_nev:
                self._foglalasok.remove(foglalas)
                return True
        return False

    def foglalasok_listazasa(self):
        if not self._foglalasok:
            print("Nincs aktuális foglalás.")
        for foglalas in self._foglalasok:
            print(f"Név: {foglalas.utas_nev} -> {foglalas.jarat}")