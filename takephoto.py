from picamera2 import Picamera2, Preview
import subprocess
import os
import keyboard

cam = Picamera2()
config = cam.create_preview_configuration(
    main={"size": (500, 500)}
)

cam.configure(config)
cam.start_preview(Preview.DRM, x=1280-500, y=720-500, width=500, height=500,)
cam.set_controls({"AfMode": 0, "LensPosition": 0.0394}) #manual mode
    #Note: Min at 0, Max at 10.0 (distance from 1/0m = infinity to 1/10m = 10 cm)
    #Here, is set to 10 inches = 25.4 cm --> position = 1/25.4 = 0.0394
is_on = True
while True:
    if keyboard.is_pressed('space'):
        cam.start()
        is_on = True
    else:
        cam.stop()
        is_on = False

    if is_on:
        try:
            #cam.set_controls({"AfMode": 1 ,"AfSpeed":0, "AfTrigger": 0}) #autofocus mode!    
            cam.capture_file("frame.png") 
            subprocess.run(["./rxing_test"]) #filename hardcoded into rust bin
        except KeyboardInterrupt:
            os.remove("frame.png")
            cam.stop()
            cam.close()