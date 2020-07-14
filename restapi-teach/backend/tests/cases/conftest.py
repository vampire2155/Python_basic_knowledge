import pytest


@pytest.fixture(scope='session')
def couse1():
    print("*** !!! couse1 setting up ***")