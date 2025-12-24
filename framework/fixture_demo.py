import pytest


@pytest.mark.usefixtures('setup')
class TestFile:
    def test_case1(self):
        print("Test Case-1 Executed.")
    def test_case2(self):
        print("Test Case-2 Executed.")
    def test_case3(self):
        print("Test Case-3 Executed.")