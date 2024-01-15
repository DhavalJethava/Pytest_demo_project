# Pytest_demo_project
A small pytest-bdd demo project which search for products on elgiganten site 

## 1. Pre-requiaites:
- Python and pytest installed. and environment variables are configured on your computer.
- This test project is developed and tested on a windows machine. So it is better to use a windows computer to perform a test run.

## 2. Installation: 
- Download or clone the code from repository.
- Required libraries as mentioned in requirements.txt file. Install them with the commmad `pip install -r requirements.txt`  

## 3. Execution:
- Run the following pytest command on the working directory
	`python3 -m pytest -k "demo" tests/step_defs/ --alluredir ./allure-reports --junitxml=./reports/junitreport.xml`
	
## 4. Reports:
- Allure report is used to generate html reports based on pytest bdd test execution format. That means, the allure will capture the features, scenarios and steps that are been executed. As well as a screenshot is captured at the end of test execution and attached in the report. 
- To see the allure report in html format, install allure, configure environment variable, then use the following command on the working directory:
	`allure serve ./allure-reports`
- This will generate report to an temporary directory, and give user a link to open web view of the report as shown here:

![38809da510e3d23ea2643378b9b40e9c.png](:/2bea581ee2e04999a32e3476482f0b73)
