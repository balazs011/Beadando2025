from Jarat import Jarat

class BelfoldiJarat(Jarat):

    def __init__(self, jaratszam, celallomas, jegyar):
        super().__init__(jaratszam, celallomas, jegyar)
        self.tipus = "Belföldi"