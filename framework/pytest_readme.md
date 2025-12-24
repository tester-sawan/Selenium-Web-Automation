> Pytest is a popular Python testing framework used to write and execute unit tests, integration tests, and functional tests in a simple and scalable way. It is widely used in QA / SDET automation and works very well with Python projects, APIs, and web automation (Selenium, Playwright, etc.).
> What is Pytest?

>Pytest allows you to:
- Write test cases using plain Python functions
- Execute tests with a single command
- Get detailed test reports for passed, failed, and skipped tests
> Pytest Framework:
- Install Pytest - pip install pytest
- Naming Convention to be followed: Any pytest file should starts with 'test_'
- As per pytest test standard, all the cases will be written inside a function called as 'Test Methods'
- All the test methods names should starts with 'test_<method_name>'
> Running pytest from terminal:
- Open the current file directory where all tests file is showing in terminal.
- 1. pytest - run all the test file available under the test folder.
- 2. pytest -v : to view more information. (v for verbose)
- 3. pytest -v -s: to view more information like console.
- 4. Always make sure that there should not any same function name in same file.
> How to run selected test file in pytest.
- 1. pytest <test_file_name.py> -v -r
- 2. if we want to run specific test cases from a file or files, we can use common method name. as pytest -k <'testCase_keyword'> -v -s
> Grouping test with pytest mark to run selected groups.
- 1. In case, we identify some test cases for smoke or regression, we use pytest.mark
- 2. We need to define @pytest.mark.<'test_type'> above the test cases as shown :
  - @pytest.mark.smoke

    def test_firstProgram():

    print("Hello to pytest learning.")
- Run :  pytest -m <smoke> -v -s 
> If we want to skip any test cases say, having some issue then follow this option:
- @pytest.mark.skip : above the test method name.
- @pytest.mark.xfail : This provide all the test cases to run but not reported in report.
> In pytest, fixtures are one of the most important and powerful features.
They are mainly used to prepare test data or test setup and clean it up after execution.

- Since you’re working with Selenium + Pytest, fixtures are mandatory in real projects.
- What are Fixtures in Pytest?
  - A fixture is a function that:

  - Runs before a test (setup)

  - Can also run after a test (teardown)

  - Supplies data or resources to test functions
  - Syntax : @pytest.fixture [Used by simply passing the fixture name as a test parameter.]
  - add the above tag in the method that need to be executed first. then, pass the method name as parameter.
  - Used Yield to run after the test execution.
    - def test_topicFirst_smoke(setup):
    
      print("I will execute after the fixture call.")
    
      msg = "Access Granted"
    
      assert msg == "Access Granted","Not matched with the expected result."

      - @pytest.fixture()
      
      def setup():
    
    print("I will be executing first.")
    
    yield
    
    print("Testing Completed.")
> Importance of conftest file & Scopes of fixtures for building generic fixtures.
- In pytest, conftest.py is a special configuration file used to define shared fixtures, hooks, and configuration that can be used across multiple test files without importing them explicitly.

- This is a very important interview and framework-level topic.
- If we want to add fixture through out any class then, define a class and put all methods inside a class and add @pytest.mark.usefixture('method_name') above the class name.
- In case, defined method in fixture will be applicable for all the methods used in the class, If we want that(at class level), at start-executed and last one will be execute at last.
- use this - @pytest.fixture(scope="class") in your conftest.py file.

> Introduction to the data driven fixture to load the data.
