import os
import time
import shutil
import tempfile
import threading
from datetime import datetime
from subprocess import call
import platform

# "Cansu"

class Recorder:

    def __init__(self,driver,fps,path=""):
        self.driver = driver
        self.fps = fps
        self.status = False
        self.tempdir = tempfile.gettempdir()
        self.path = path
        
    def __record(self):
        frame = 0
        while self.status:
            try:
                self.driver.get_screenshot_as_file(self.tempdir+"/reconium/{}.png".format(frame))
                frame = frame+1
                time.sleep(1/self.fps)
            except Exception as e:
                pass


    def start(self):

        if not os.path.exists(self.tempdir+"/reconium/"):
            os.makedirs(self.tempdir+"/reconium/")
        else:
            shutil.rmtree(self.tempdir+"/reconium/")
            os.makedirs(self.tempdir+"/reconium/")

        self.status = True
        self.rec = threading.Thread(target=self.__record)
        self.rec.start()
    

    def stop(self):
        self.status = False

        if platform.system() == 'Linux':
            name = self.path+str(datetime.now())
        elif platform.system() == 'Windows':
            name = self.path+str(datetime.now().strftime("%Y-%m-%d %H_%M_%S"))
        else:
            name = self.path+str(datetime.now())

        fps = int(self.fps/4)
        try:
            call(["ffmpeg","-framerate",str(fps),"-i",self.tempdir+"/reconium/%00d.png",name+".avi"])
        except Exception as e:
            print(e)
        finally:
            shutil.rmtree(self.tempdir+"/reconium/")