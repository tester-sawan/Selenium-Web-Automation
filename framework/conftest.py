import pytest
from httplib2.auth import params


@pytest.fixture(scope="class")
def setup():
    print("I will be executing first.")
    yield
    print("Testing Completed.")
@pytest.fixture()
def test_data():
    print("User profile data has been created.")
    return ["Sawan Kumar","Adventus.io",4082]
@pytest.fixture(params=["chrome","firefox","ie"])
def test_crossBrowser(request):
    return request.params