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