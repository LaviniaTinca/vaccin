from Domain.vaccin import Vaccin


class VaccinService:
    def __init__(self, vaccin_repository, vaccin_validator):
        """
        instantiaza service-ul
        :param vaccin_repository: repository pt vaccin
        :param vaccin_validator: validator pt vaccin
        """
        self.__vaccin_repository = vaccin_repository
        self.__vaccin_validator = vaccin_validator

    def get_all(self):
        """
        obtinem baza de date
        :return: o lista cu localitatile
        """
        return self.__vaccin_repository.get_all()

    def adaugare(self, id_vaccin, nume, tehnologie):
        """
        adauga un obiect
        :param id_localitate: id-ul vaccinului
        :param nume: numele
        :param tehnologie: mRNA, virus inactiv, virus atenuat
        :return: None
        """
        vaccin  = Vaccin(id_vaccin, nume, tehnologie)
        self.__vaccin_validator.valideaza(vaccin)
        self.__vaccin_repository.adaugare(vaccin)
