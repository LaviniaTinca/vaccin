from Domain.entitate import Entitate


class Vaccin(Entitate):

    def __init__(self, id_vaccin, nume, tehnologie):
        '''
        Creeaza un vaccin.
        :param id_vaccin: id-ul vaccinului
        :param nume: numele (nenul)
        :param tehnologie: nRNA, virus inactiv, virus atenuat
        '''

        super().__init__(id_vaccin)
        self.__nume = nume
        self.__tehnologie = tehnologie

    @property
    def nume(self):
        return self.__nume

    @property
    def tehnologie(self):
        return self.__tehnologie

    def __str__(self):
        return f'{self.id_entitate} - nume: {self.nume}, tehnologie: {self.__tehnologie}'
