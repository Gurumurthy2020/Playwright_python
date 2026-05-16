import pytest


class Testdetails:

    def test_details(self):
        print("details")

    @pytest.mark.skip
    def test_details1(self):
        print("details1")

