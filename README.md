This is a project for automation testing a calculator app on android emulator, using appium, pytest and allure for reports.
In 'utilities' package fill 'path_to_android_calc' with the path to the .apk file on your computer.
You can start the test with 'pytest tests -rA -v'
If you want to generate reports with allure, you must install allure-pytest (pip install allure-pytest). You can also visit the qameta website for more information: https://docs.qameta.io/allure/#_pytest