éáfrom Legitarsasag import Legitarsasag
from BelfoldiJarat import BelfoldiJarat
from NemzetkoziJarat import NemzetkoziJarat


class BookingSystem:

    def __init__(self):
        self._legitarsasag = Legitarsasag("GDE Airlines")
        self._init_data()

    def _init_data(self):


        jarat1 = BelfoldiJarat("B001", "Debrecen", 15000)
        jarat2 = NemzetkoziJarat("N001", "Róma", 45000)
        jarat3 = NemzetkoziJarat("N002", "Bécs", 120000)

        self._legitarsasag.jarat_hozzaadasa(jarat1)
        self._legitarsasag.jarat_hozzaadasa(jarat2)
        self._legitarsasag.jarat_hozzaadasa(jarat3)


        try:
            self._legitarsasag.jegy_foglalas("B001", "Kiss Tamás")
            self._legitarsasag.jegy_foglalas("B001", "Teszt Anna")
            self._legitarsasag.jegy_foglalas("N001", "Kovács Géza")
            self._legitarsasag.jegy_foglalas("N001", "Szabó Éva")
            self._legitarsasag.jegy_foglalas("N002", "Teszt Béla")
            self._legitarsasag.jegy_foglalas("N002", "Varga Judit")
        except Exception as e:
            print(f"Hiba az betöltéskor: {e}")

    def user_interact(self):
        while True:
            print("\n--- BMJ879 Repülőjegy Foglalási Rendszer ---")
            print("1. Járatok listázása")
            print("2. Jegy foglalása")
            print("3. Foglalás lemondása")
            print("4. Foglalások listázása")
            print("5. Bezárás")
            print("---------------------")
            choice = input("Válassz menüpontot: ")

            if choice == "1":
                for jarat in self._legitarsasag.get_jaratok():
                    print(jarat)

            elif choice == "2":
                try:
                    jaratszam = input("Add meg a járatszámot: ")
                    nev = input("Add meg az utas nevét: ")
                    ar = self._legitarsasag.jegy_foglalas(jaratszam, nev)
                    print(f"Sikeres foglalás! A jegy ára: {ar} Ft")
                except ValueError as e:
                    print(f"Hiba: {e}")
                except Exception as e:
                    print("Váratlan hiba történt.")

            elif choice == "3":
                jaratszam = input("Add meg a lemondandó járatszámot: ")

                nev = input("Add meg az utas nevét: ")
                siker = self._legitarsasag.foglalas_lemondasa(jaratszam, nev)
                if siker:
                    print("Sikeres törlés.")
                else:
                    print("Nincs ilyen fogélalás.")

            elif choice == "4":
                self._legitarsasag.foglalasok_listazasa()

            elif choice == "5":
                break
            else:
                print("Érvénytelen választás!")


if __name__ == "__main__":
    system = BookingSystem()
    system.user_interact()
