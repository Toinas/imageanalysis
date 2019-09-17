import time
import picamera
import imagediff

filepath = '/home/pi/Desktop/image-difference/testimages/'
def ImageCapture():
    with picamera.PiCamera() as camera:
    #camera.start_preview()
    #time.sleep()       
        for i in range(2):        
            camera.capture(filepath +'image'+str(i)+'.png')
            time.sleep(30) # wait .5 minutes
            print str(i)
            
ImageCapture()
            
filelist = [ f for f in os.listdir("/home/pi/Desktop/image-difference/testimages/") if f.endswith(".png") ]
if (filelist.len ==2):
    imagediff -f /home/pi/Desktop/image-difference/testimages/image0.png -s /home/pi/Desktop/image-difference/testimages/image1.png
