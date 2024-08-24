# Python API Automation Framework

# Tech Stack

- Python 3.12
- Request - HTTP Requests
- Pytest - Testing Framework
- Reporting - Allure Report, Pytest HTML
- Test Data - CSV,Excel, JSON, Faker (it is library which generate fake data)
- Advance API Testcase - jsonschema
- Parallel Execution - x distribute (xdist)

How to install Packages ?

```pip install requests pytest pytest-html faker allure-pytest jsonschema ```

```python.exe -m pip install --upgrade pip ```

For parallel execution:

``` pip install pytest-xdist ```

### How to add the ,gitignore file ?

Copy the content from this to .gitignore file
https://www.toptal.com/developers/gitignore/api/pycharm+all


Implementation steps:
---------------------
1. Create a new project name as  "APIAutomationFramework"
2. Create package : **"src"** -> keep which are not related to the test 
3. Create package : **"tests"** -> Keep all test related TCs
4. Create new file : **".getignore"** -> It make sure you don't upload unwanted folder. 
                                    All the intelligent related folder we don't want to upload
    for example: .venv 
    ### How to add the ".gitignore" file ?
    Copy the content from this to .gitignore file
    https://www.toptal.com/developers/gitignore/api/pycharm+all
5. Create package : **src >> "utils"** -> It contain common utilities 

    For example : i) read data from CSV file, excel file
                  ii) set the header - application/json, application/xml 
6. Create python file : **src >> utils >> "utils.py"**
7. Create package : **src >> "constants"** -> Which contain all the end points . 
                                              It keeps all the URLs

    For example : i) read data from CSV file, excel file
                  ii) set the header - application/json, application/xml 
8. Create python file : **src >> constants >>"constants.py"**
9. Create package : **tests >> tests >> crud**
10. Create python file : **tests >> tests >> crud >> test_create_booking.py**
11. Divide TCs into 5 part:
12. Create package with python file : **src > > helpers >> api_request_wrapper.py** -> help you in making request
13. Create package with python file : **src > > helpers >> common_verification.py**
14. Create package with python file : **src > > helpers >> payload_manager.py*
15. Create Package : -> to store a resource like ".env"
16. But generally we keep ".env" file outside -> environment related file
    For Example: USERNAME = admin
                 PASSWORD = password123
17. Run the TCs before proceeding
In terminal:
```commandline
pytest tests/tests/curd/test_create_booking.py
```
```commandline
pytest tests/tests/curd/test_create_booking.py --alluredir=allure_result
```
```commandline
allure serve allure_result
```