> Pre-requisite : Pytest 
1. Avoid Hard Coding Test Data 
- Ensure the test data should be injected from tests rather than beign hard coded within test methods.
2. Externalize Test Data
- Feed test data from external files to maintain isolation between the test logic and data sources. This will enhance easier maintainace & Scalability.
3. Implement Page Object Model.
- Apply the page object design pattern to seperate page locators and actions from test files.
- This improved code reusability, readability and maintainability.
4. Centralised re-usable code 
- Use common utilities (utilities.py) and Configuration files(config.py) to store re-usable code thoroughout the framework.
5. Define Global Environment Variables.
6. Apply grouping/tags to run targeted test and running test in parallel mode.
7. Generate HTML reports.
8. Capture logs & screenshot.