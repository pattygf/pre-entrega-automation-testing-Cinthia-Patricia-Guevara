import pytest

pytest.main([ "tests/test_login.py", "--html=reporte.html", "--self-contained-html", "-v" ])