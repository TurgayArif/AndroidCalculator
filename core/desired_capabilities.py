from utilities.test_data import TestData

caps = {"platformName": TestData.platformName,
        "appium:platformVersion": TestData.platformVersion,
        "appium:deviceName": TestData.deviceName,
        "appium:automationName": TestData.automationName,
        "appium:app": TestData.path_to_android_calc,
        "appium:ensureWebviewsHavePages": True, "appium:nativeWebScreenshot": True, "appium:newCommandTimeout": 3600,
        "appium:connectHardwareKeyboard": True}
