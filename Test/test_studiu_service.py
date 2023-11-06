from Domain.studiu import Studiu
from Domain.studiu_validator import StudiuValidator
from Domain.vaccin import Vaccin
from Domain.vaccin_validator import VaccinValidator
from Repository.file_repository import FileRepository
from Service.studiu_service import StudiuService
from Service.vaccin_service import VaccinService
from Test.file_utils import clear_file




def test_studiu_service():

    v1 = Vaccin('1', 'moderna', 'mRNA')
    v2 = Vaccin('2', 'chadox', 'virus atenuat')
    v3 = Vaccin('3', 'pfeizer', 'virus activ')

    s1 = Studiu('1', '1', 5000, 10, 90)
    s2 = Studiu('2', '2', 4000, 5, 70)
    s3 = Studiu('3', '3', 2000, 7, 89)
    s4 = Studiu('4', '2', 1000, 12, 88)

    filename_vaccinuri = 'test_vaccin_service.json'
    filename_studii = 'test_studii_service.json'
    clear_file(filename_vaccinuri)
    clear_file(filename_studii)
    vaccin_repository = FileRepository(filename_vaccinuri)
    studii_repository = FileRepository(filename_studii)
    studiu_validator = StudiuValidator()
    studiu_service = StudiuService(studii_repository, vaccin_repository, studiu_validator)

    vaccin_repository.adaugare(v1)
    vaccin_repository.adaugare(v2)
    vaccin_repository.adaugare(v3)

    # CRUD
    try:
        studiu_service.adaugare('1', '100', 5000, 80, 10)
        assert False
    except KeyError:
        assert True
    assert len(studiu_service.get_all()) == 0

    studiu_service.adaugare(s1.id_entitate, s1.id_vaccin, s1.nr_subiecti, s1.pr_grup_vaccinati, s1.pr_grup_placebo)
    assert len(studiu_service.get_all()) == 1
    assert studii_repository.get_by_id(s1.id_entitate) == s1

    try:
        studiu_service.adaugare('2', '1', 5000, -1, 103)
        assert False
    except ValueError:
        assert True
    assert len(studiu_service.get_all()) == 1

    # cerinta 3
    studii_repository.adaugare(s2)
    studii_repository.adaugare(s3)
    studii_repository.adaugare(s4)

    result = studiu_service.get_vaccinuri_ordonate_eficienta()
    assert result[0] == (v1, (90 - 10) / 90 * 100)
    assert result[1][1] > result[0][1]
    assert result[2][1] > result[1][1]

    # cerinta 4
    result = studiu_service.get_with_nr_subiecti_mai_mare_decat(1500)
    assert len(result) == 3
    for r in result:
        assert r[0].nr_subiecti > 1500

    # cerinta 5
    filename = 'test_export.json'
    studiu_service.export_json(filename)
    try:
        with open(filename, 'r'):
            assert True
    except:
        assert False

#######################################################
    # teste model cristina

