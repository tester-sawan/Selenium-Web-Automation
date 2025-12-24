import pytest


@pytest.mark.smoke
# @pytest.mark.skip
def test_topicFirst_smoke(setup):
    print("I will execute after the fixture call.")
    msg = "Access Granted"
    assert msg == "Access Granted","Not matched with the expected result."

