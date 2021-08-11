# https://microsoft.github.io/AirSim/object_detection/
import setup_path 
import airsim
import cv2
import numpy as np 
import pprint
import time


# connect to the AirSim simulator
client = airsim.VehicleClient()
client.confirmConnection()

# set camera name and image type to request images and detections
camera_name = "0"
image_type = airsim.ImageType.Scene

# set detection radius in [cm]
client.simSetDetectionFilterRadius(camera_name, image_type, 200 * 200) 
# add desired object name to detect in wild card/regex format
client.simAddDetectionFilterMeshName(camera_name, image_type, "Person*") 


while True:
    rawImage = client.simGetImage(camera_name, image_type)
    if not rawImage:
        continue
    png = cv2.imdecode(airsim.string_to_uint8_array(rawImage), cv2.IMREAD_UNCHANGED)
    people = client.simGetDetections(camera_name, image_type)
    if people:
        for person in people:
            s = pprint.pformat(person)
            #print("Person: %s" % s)

            # cv2.rectangle => bbox
            # cv2.putText=> 식별자 이름
            cv2.rectangle(png,(int(person.box2D.min.x_val),int(person.box2D.min.y_val)),(int(person.box2D.max.x_val),int(person.box2D.max.y_val)),(255,0,0),2)
            cv2.putText(png, person.name, (int(person.box2D.min.x_val),int(person.box2D.min.y_val - 10)), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (36,255,12))
        
         

    # 한줄 추가
    #png = cv2.resize(png, dsize=(640, 300))
    cv2.imshow("AirSim", png)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    elif cv2.waitKey(1) & 0xFF == ord('c'):
        client.simClearDetectionMeshNames(camera_name, image_type)
    elif cv2.waitKey(1) & 0xFF == ord('a'):
        client.simAddDetectionFilterMeshName(camera_name, image_type, "Person*")


    
cv2.destroyAllWindows() 