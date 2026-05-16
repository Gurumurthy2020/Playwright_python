import pytest


@pytest.fixture(scope="session")
def initialsetup():
    print("browser initialized")
    yield
    print("browser closed in session")