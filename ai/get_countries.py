

import pickle


import cv2
import numpy as np

#############################
map_file_path = "map.p"
countries_file_path = "countries.p"
cam_id = 1
width, height = 1920, 1080
#############################



cap = cv2.VideoCapture(cam_id)

cap.set(3, width)
cap.set(4, height)

file_obj = open(map_file_path, 'rb')
map_points = pickle.load(file_obj)
file_obj.close()
print(f"Loaded map coordinates.", map_points)


current_polygon = []

counter = 0


if countries_file_path:
    file_obj = open(countries_file_path, 'rb')
    polygons = pickle.load(file_obj)
    file_obj.close()
    print(f"Loaded {len(polygons)} countries.")
else:
    polygons = []


def warp_image(img, points, size=[1920, 1080]):

    pts1 = np.float32(points)  # Convert points to float32
    pts2 = np.float32([[0, 0], [size[0], 0], [0, size[1]], [size[0], size[1]]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (size[0], size[1]))
    return imgOutput, matrix



def mousePoints(event, x, y, flags, params):

    global counter, current_polygon


    if event == cv2.EVENT_LBUTTONDOWN:

        current_polygon.append((x, y))


while True:

    success, img = cap.read()
    imgWarped, _ = warp_image(img, map_points)


    key = cv2.waitKey(1)


    if key == ord("s") and len(current_polygon) > 2:
        country_name = input("Enter the Country name: ")
        polygons.append([current_polygon, country_name])
        current_polygon = []
        counter += 1
        print("Number of countries saved: ", len(polygons))


    if key == ord("q"):
        fileObj = open(countries_file_path, 'wb')
        pickle.dump(polygons, fileObj)
        fileObj.close()
        print(f"Saved {len(polygons)} countries")
        break

    if key == ord("d"):
        polygons.pop()

    if current_polygon:
        cv2.polylines(imgWarped, [np.array(current_polygon)], isClosed=True, color=(0, 0, 255), thickness=2)

    overlay = imgWarped.copy()

    for polygon, name in polygons:
        cv2.polylines(imgWarped, [np.array(polygon)], isClosed=True, color=(0, 255, 0), thickness=2)
        cv2.fillPoly(overlay, [np.array(polygon)], (0, 255, 0))

    cv2.addWeighted(overlay, 0.35, imgWarped, 0.65, 0, imgWarped)


    cv2.imshow("Warped Image", imgWarped)
    cv2.imshow("Original Image", img)

    cv2.setMouseCallback("Warped Image", mousePoints)

