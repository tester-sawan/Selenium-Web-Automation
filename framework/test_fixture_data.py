import pytest


@pytest.mark.usefixtures("test_data")
class TestCreateUserProfile:
    def test_basicProfile(self,test_data):
        print(test_data)
        print(test_data[0])
        print(test_data[1])