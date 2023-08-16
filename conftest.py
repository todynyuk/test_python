from selenium import webdriver

options = webdriver.ChromeOptions()
options.platform_name = "linux"
options.browser_version = "latest"
options.set_capability("enableVideo", "true")