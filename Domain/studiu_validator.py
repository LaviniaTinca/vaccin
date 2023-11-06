class StudiuValidator:
    def valideaza(self, studiu):
        """
        valideaza un obiect
        :param obiect: obiectul de validat
        :return: None
        :raises: ValueErrors: daca obiectul nu are campurile completate valid.
        """
        erori= []

        if studiu.nr_subiecti <= 0:
            erori.append('numar subiecti nr negativ')
        if studiu.pr_grup_vaccinati not in range(0, 101):
            erori.append('Procentul de imbolnaviti in grupul vaccinati trebuie sa fie intre 0 si 100!')
        if studiu.pr_grup_placebo not in range(0, 101):
            erori.append('Procentul de imbolnaviti in grupul placebo trebuie sa fie intre 0 si 100!')
        if len(erori) > 0:
            raise ValueError(erori)
