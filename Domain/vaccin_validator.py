class VaccinValidator:
    def valideaza(self, vaccin):
        """
        valideaza un obiect
        :param obiect: obiectul de validat
        :return: None
        :raises: ValueErrors: daca obiectul nu are campurile completate valid.
        """
        erori= []
        if  vaccin.nume == '':
            erori.append('string gol')
        if vaccin.tehnologie not in ['mRNA', 'virus inactiv', 'virus atenuat']:
            erori.append('tehnologia trebuie sa fie: mRNA, virus inactiv, virus atenuat!')

        if len(erori) > 0:
            raise ValueError(erori)
