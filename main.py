import pytest

pytest.main([ "tests/test_login.py", "tests/test_inventario.py", "tests/test_carrito.py", "--html=reporte.html", "--self-contained-html", "-v" ])