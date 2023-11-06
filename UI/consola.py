class Consola:
    def __init__(self, vaccin_service, studiu_service):
        self.__vaccin_service = vaccin_service
        self.__studiu_service = studiu_service

    def __print_menu(self):
        print('')
        print("1. Adaugare vaccin")
        print("2. Adaugare studiu clinic")
        print("3. Afisare localitati ordonate crescator dupa nr. de rute dus-intors din care pornesc + acest nr.")
        print("4. Afisare rute care se opresc intr-un municipiu")
        print("5. Export JSON")
        print("-----------------------")
        print("a1. Afisare vaccinuri")
        print("a2. Afisare studii clinice")
        print("x. Iesire")

    def run_console(self):
        while True:
            self.__print_menu()
            optiune = input("Dati optiunea: ")
            if optiune == '1':
                self.__ui_adaugare_a()
            elif optiune == '2':
                self.__ui_adaugare_b()
            elif optiune == '3':
                #self.__show_all(self.__studiu_service.afisare_localitati_dupa_nr_rute_dus_intors())
                #self.__ui_afisare_localitati_dupa_nr_rute()
                self.__ui_get_vaccinuri_ordonate_eficienta()
            elif optiune == '4':

                self.__ui_afisare_rute_care_se_opresc_in_municipiu()
            elif optiune == '5':
                filename = input('Numele fisierului pt export: ')
                self.__studiu_service.export_json(filename)
            elif optiune =="a1":
                self.__show_all(self.__vaccin_service.get_all())
            elif optiune =="a2":
                self.__show_all(self.__studiu_service.get_all())
            elif optiune == "x":
                break
            else:
                print("Optiune invalida. Reincercati!")

    def __ui_adaugare_a(self):
        try:
            id_vaccin = input("Dati id-ul vaccinului: ")
            nume = input ("Dati numele vaccinului: ")
            tehnologie = input("Dati tipul tehnologiei (mRNA, virus inactiv, virus atenuat): ")

            self.__vaccin_service.adaugare(id_vaccin, nume, tehnologie)
        except Exception as e:
            print(e)

    def __ui_adaugare_b(self):
        try:
            id_studiu = input("Dati id-ul studiului: ")
            id_vaccin = input("Dati id-ul vaccinului: ")
            nr_subiecti = int(input("Dati nr subiecti: "))
            pr_grup_vaccinati = int(input("Dati nr imbolnaviti dintre cei vaccinati (0-100): "))
            pr_grup_placebo = int(input("Dati nr imbolnaviti din grupul placebo (0-100): "))

            self.__studiu_service.adaugare(id_studiu, id_vaccin, nr_subiecti, pr_grup_vaccinati, pr_grup_placebo)
        except Exception as e:
            print(e)

    def __show_all(self, lista):
        for elem in lista:
            print(elem)

