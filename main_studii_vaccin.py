from Domain.studiu_validator import StudiuValidator
from Domain.vaccin_validator import VaccinValidator
from Repository.file_repository import FileRepository
from Service.studiu_service import StudiuService
from Service.vaccin_service import VaccinService
from Test.file_utils import clear_file
from Test.test_repository import test_add_repository
from Test.test_studiu_service import test_studiu_service
from Test.test_vaccin import test_vaccin_service

from UI.consola import Consola


def main():
    test_add_repository()
    test_vaccin_service()
    test_studiu_service()

    vaccin_repository = FileRepository('vaccin.json')
    studiu_repository = FileRepository('studiu.json')
    clear_file('vaccin.json')
    clear_file('studiu.json')

    vaccin_validator = VaccinValidator()
    studiiu_validator = StudiuValidator()


    vaccin_service = VaccinService(vaccin_repository, vaccin_validator)
    studiu_service = StudiuService(studiu_repository, vaccin_repository, studiiu_validator)

    vaccin_service.adaugare('1', 'aaa', 'virus inactiv')
    vaccin_service.adaugare('2', 'bbb', 'virus atenuat')
    vaccin_service.adaugare('3', 'ccc', 'virus inactiv')
    vaccin_service.adaugare('4', 'ddd', 'mRNA')

    studiu_service.adaugare('10', '2', 30, 12, 76)
    studiu_service.adaugare('11', '1', 25, 30, 50)
    studiu_service.adaugare('12', '4', 18, 10, 90)
    studiu_service.adaugare('13', '4', 8, 4, 76)

    consola = Consola(vaccin_service, studiu_service)
    consola.run_console()

    main()

main()