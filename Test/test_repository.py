from Domain.entitate import Entitate
from Repository.file_repository import FileRepository
from Utils.file_utils import clear_file


def test_add_repository():
    clear_file("repository-test.txt")
    entitati_repository = FileRepository("repository-test.txt")

    entitate1 = Entitate('1')

    entitati_repository.adaugare(entitate1)
    assert len(entitati_repository.get_all()) == 1
    added = entitati_repository.get_by_id('1')
    assert added is not None
    assert added.id_entitate == '1'

    try:
        entitate2 = Entitate('1')
        entitati_repository.adaugare(entitate2)
        assert False
    except Exception:
        assert True

def test_delete_repository():
    clear_file("repository-test.txt")
    entitati_repository = FileRepository("repository-test.txt")
    entitate1 = Entitate('1')
    entitate2 = Entitate('2')
    entitati_repository.adaugare(entitate1)
    entitati_repository.adaugare(entitate2)

    try:
        entitati_repository.stergere('3')
        assert False#
    except Exception:
        assert True

    entitati_repository.stergere('1')
    assert len(entitati_repository.get_all()) == 1
    deleted = entitati_repository.get_by_id('1')
    assert deleted is None
    remaining = entitati_repository.get_by_id('2')
    assert remaining is not None
    assert remaining.id_entitate == '2'

def test_modificare_repository():
    clear_file("repository-test.txt")
    entitati_repository = FileRepository("repository-test.txt")
    entitate1 = Entitate('1')
    entitate2 = Entitate('2')
    entitati_repository.adaugare(entitate1)
    entitati_repository.adaugare(entitate2)

    entitate3 = Entitate('1')
    entitati_repository.modificare(entitate3)
    modificared = entitati_repository.get_by_id('1')
    assert modificared is not None
    assert modificared.id_entitate == '1'

    unchanged = entitati_repository.get_by_id('2')
    assert unchanged is not None
    assert unchanged.id_entitate == '2'

    try:
        entitate4 = Entitate('3')
        entitati_repository.modificare(entitate4)
        assert False
    except Exception:
        assert True