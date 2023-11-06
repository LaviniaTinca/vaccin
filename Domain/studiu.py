from Domain.entitate import Entitate


class Studiu(Entitate):

    def __init__(self, id_studiu, id_vaccin, nr_subiecti, pr_grup_vaccinati, pr_grup_placebo):
        """
        creeaza un studiu
        :param id_studiu: id-ul studiului
        :param id_vaccin: id-ul vaccinului, sa existe
        :param nr_subiecti: intreg >0
        :param pr_grup_vaccinati: intreg intre 0-100
        :param pr_grup_placebo: intreg intre 0-100
        """

        super(Studiu, self).__init__(id_studiu)
        self.__id_vaccin = id_vaccin
        self.__nr_subiecti = nr_subiecti
        self.__pr_grup_vaccinati = pr_grup_vaccinati
        self.__pr_grup_placebo = pr_grup_placebo

    @property
    def id_vaccin(self):
        return self.__id_vaccin

    @property
    def nr_subiecti(self):
        return self.__nr_subiecti

    @property
    def pr_grup_vaccinati(self):
        return self.__pr_grup_vaccinati

    @property
    def pr_grup_placebo(self):
        return self.__pr_grup_placebo

    def __str__(self):
        return f'{self.id_entitate} - vaccin : {self.id_vaccin}, subiecti: {self.__nr_subiecti},' \
               f' procent vaccinati: {self.__pr_grup_vaccinati}, procent placebo: {self.__pr_grup_placebo}'
