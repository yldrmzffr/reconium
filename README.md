# reconium

Record Video for Selenium Test

## Install
        pip install reconium

## Usage
        import reconium
    
        rc = reconium.Recorder(webdriver,fps)
    
        rc.start()
        # record here selenium test
        rc.stop()

## Example for both Linux and Windows
    from selenium import webdriver
    import reconium
    import time
    import platform
    
    
    if(platform.system()=='Linux'):
    	driver_path = 'resources/geckodriver'
    elif(platform.system()=='Windows'):
    	driver_path = 'resources/geckodriver.exe'
    
    
    driver = webdriver.Firefox(executable_path=driver_path)
    fps=20
    
    rc = reconium.Recorder(driver,fps)
    rc.start()
    
    # record here selenium test
    driver.get("https://www.google.com")
    time.sleep(10)
    driver.quit()
    
    rc.stop()