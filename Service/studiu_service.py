import json

from Domain.studiu import Studiu


class StudiuService:
    '''
    Service pentru studii.
    '''

    def __init__(self, studiu_repository, vaccin_repository, studiu_validator):
        '''
        Instantiaza service-ul.

        :param studiu_repository: repository-ul de studii.
        :param vaccin_repository: repository-ul de vaccinuri.
        :param studiu_validator: validatorul pentru studii
        '''

        self.__studiu_repository = studiu_repository
        self.__vaccin_repository = vaccin_repository
        self.__studiu_validator = studiu_validator

    def adaugare(self,  id_studiu, id_vaccin, nr_subiecti, pr_grup_vaccinati, pr_grup_placebo):
        """
        adauga un studiu
        :param id_studiu: id studiu
        :param id_vaccin: id vaccin, sa existe
        :param nr_subiecti: nr de subiecti
        :param pr_grup_vaccinati: procent imbolnaviti din grupul vaccinati
        :param pr_grup_placebo: procent imbolnaviti din grupul placebo
        :return: None
        :raises ValueError: daca exista erori de validare
        :raises KeyError: daca id-ul exista deja sau daca id_vaccin  nu exista
        """

        studiu = Studiu(id_studiu, id_vaccin, nr_subiecti, pr_grup_vaccinati, pr_grup_placebo)
        if self.__vaccin_repository.get_by_id(id_vaccin) is None:
            raise KeyError(f'Nu exista nici un vaccin cu id-ul {id_vaccin}!')

        self.__studiu_validator.valideaza(studiu)
        self.__studiu_repository.adaugare(studiu)

    def get_all(self):
        '''
        Intoarce toate obiectele.

        :return: o lista cu toate rutele.
        '''
        return self.__studiu_repository.get_all()


##########################################################################################

    def get_vaccinuri_ordonate_eficienta(self):
        '''
        Determina ordonarea vaccinurile dupa eficienta lor din studiile clinice.

        :return: o lista de perechi (vaccin, media eficientelor) ordonata crescator dupa media eficientelor.
        '''

        result = {}
        for studiu in self.get_all():
            eficienta = (studiu.pr_grup_placebo - studiu.pr_grup_vaccinati) / studiu.pr_grup_placebo * 100
            if studiu.id_vaccin in result:
                result[studiu.id_vaccin].append(eficienta)
            else:
                result[studiu.id_vaccin] = [eficienta]

        for id_vaccin in result:
            result[id_vaccin] = sum(result[id_vaccin]) / len(result[id_vaccin])

        return sorted([(self.__vaccin_repository.get_by_id(elem[0]), elem[1]) for elem in result.items()], key=lambda x: x[1])

    def get_with_nr_subiecti_mai_mare_decat(self, min_nr_subiecti):
        '''
        Determina toate studiile clinice cu nr de subiecti mai mare decat un numar dat

        :param min_nr_subiecti: numarul minim de subiecti considerat.

        :return: o lista de perechi (studiu clinic, tehnologia vaccinului studiat)
        '''

        result = []
        for studiu in self.get_all():
            if studiu.nr_subiecti > min_nr_subiecti:
                result.append((studiu, self.__vaccin_repository.get_by_id(studiu.id_vaccin).tehnologie))

        return result



    def export_json(self, filename):
        """
        exporta tehnologiile si studiile aferente vaccinurilor pt acea tehnologie intr-un fisier json citit de la tastatura
        :param filename: numele fisierului
        :return: NOne
        """
        vaccinuri = self.__vaccin_repository.get_all()
        studii = self.get_all()

        result = {}

        for studiu in studii:
            tehnologie = self.__vaccin_repository.get_by_id(studiu.id_vaccin).tehnologie
            if tehnologie in result:
                result[tehnologie] += 1
            else:
                result[tehnologie] = 1

        with open(filename, 'w') as f:
            json.dump(result, f, indent = 10)


