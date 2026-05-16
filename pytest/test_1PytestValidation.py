import pytest


# @pytest.fixture(scope="function")
# def initialSetup():
#     print("browser initialized")
#
# def test_firstpyprogram(initialSetup):
#     print(("first test"))
#
# def test_secondpyprogram(initialSetup):
#     print(("second test"))


class TestClass:
    @pytest.fixture(scope="module")
    def setup(self):
        print("setup")
        yield
        print("function done")

    def test_firstpyprogram(self, initialsetup, setup):
        print(("first test"))

    def test_secondpyprogram(self, initialsetup):
        print(("second test"))