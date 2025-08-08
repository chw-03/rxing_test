import cv2

print("start")
cap = cv2.VideoCapture(0)
print("read")
while True:
    ret, frame = cap.read()
    print("a")
    #with open('/dev/fb0', 'rb+') as buf:
    #   buf.write(frame)
    if cv2.waitKey(1) & 0xFF == 32: #spacebar = key 32            
        break
cap.release()