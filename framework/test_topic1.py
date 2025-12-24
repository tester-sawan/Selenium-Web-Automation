
import pytest

@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello to pytest learning.")
@pytest.mark.xfail
def test_secondProgram():
    msg = "Hello Sawan!"
    assert msg == "Hello Sawan!","Test Failed as the information mismatches."
@pytest.mark.smoke

def test_thirdProgram_smoke():
    a=5
    b=10
    assert a+2 == 7, "Expected sum not matched with actual sum."

def test_crossBrowser(crossBrowser):
    print(crossBrowser)