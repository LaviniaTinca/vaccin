from Domain.vaccin_validator import VaccinValidator
from Repository.file_repository import FileRepository
from Service.vaccin_service import VaccinService
from Test.file_utils import clear_file


def test_vaccin_service():
    clear_file("vaccin-test.txt")
    vaccin_repository = FileRepository("vaccin-test.txt")
    vaccin_validator = VaccinValidator()

    vaccin_service = VaccinService(vaccin_repository, vaccin_validator)

    vaccin_service.adaugare('1', 'aaa', 'virus inactiv')
    assert len(vaccin_service.get_all()) == 1
    added = vaccin_repository.get_by_id('1')
    assert added is not None
    assert added.id_entitate == '1'
    assert added.nume == "aaa"
    assert added.tehnologie == 'virus inactiv'

    try:
        vaccin_service.adaugare('1', 'bbb', 'mRNA')
        assert False
    except Exception:
        assert True