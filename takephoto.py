from picamera2 import Picamera2, Preview
#import time
import subprocess

side = 500
cam = Picamera2()

config = cam.create_preview_configuration(
    main={"size": (side, side)}
)

cam.configure(config)
cam.start_preview(Preview.DRM, x=1280-side, y=720-side, width=side, height=side,)
cam.start()
cam.set_controls({"AfMode": 0, "LensPosition": 0.0358}) #manual mode
    #Note: Min at 0, Max at 10.0 (distance from 1/0m = infinity to 1/10m = 10 cm)
    #Here, is set to 11 inches = 27.94 cm --> position = 1/27.94 = 0.0358

try:
    while True:
        #cam.set_controls({"AfMode": 1 ,"AfSpeed":0, "AfTrigger": 0}) #autofocus mode!
        #start = time.time()     
        cam.capture_file("frame.png") 
        subprocess.run(["./rxing_test"]) #filename hardcoded into rust bin
        #print(f"time to read frame: {time.time() - start}")
except KeyboardInterrupt:
    cam.stop()
    cam.close()