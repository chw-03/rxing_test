from picamera2 import Picamera2, Preview
import time
import subprocess

side = 500
cam = Picamera2()
config = cam.create_preview_configuration(
    main={"size": (side, side)}
)

cam.configure(config)
cam.start_preview(Preview.DRM)
cam.start()

try:
    while True:
        time.sleep(1.0)
        cam.set_controls({"AfMode": 1 ,"AfTrigger": 0}) #autofocus mode!     
        print("aaaa")  
        cam.capture_file("framecap.png")
        subprocess.run(["./rxing_test", "framecap.png", "true"])
except KeyboardInterrupt:
    cam.stop()
    cam.close()

