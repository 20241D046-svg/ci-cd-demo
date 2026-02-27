import crud

def test_create_and_read():
    crud.data = [] # Limpiar datos
    crud.create("item1")
    assert "item1" in crud.read()

def test_update():
    crud.data = []
    crud.create("item2")
    assert crud.update(0, "item2 updated")
    assert crud.read()[0] == "item2 updated"

def test_delete():
    crud.data = []
    crud.create("item3")
    assert crud.delete(0)
    assert "item3" not in crud.read()