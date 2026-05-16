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


    def test_thirdpyprogram(self, initialsetup):
        print(("3 test"))

    def test_fourthpyprogram(self, initialsetup):
        print(("fourth test"))