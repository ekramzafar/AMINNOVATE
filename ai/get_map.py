
import pickle
import cv2
import numpy as np

#########################
cam_id = 1
width, height = 1920, 1080
#########################

cap = cv2.VideoCapture(cam_id)
cap.set(3, width)
cap.set(4, height)
points = np.zeros((4, 2), int)
counter = 0


def mousePoints(event, x, y, flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:
        points[counter] = x, y
        counter += 1
        print(f"Clicked points: {points}")


def warp_image(img, points, size=[1920, 1080]):
    pts1 = np.float32(points)
    pts2 = np.float32([[0, 0], [size[0], 0], [0, size[1]], [size[0], size[1]]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    imgOutput = cv2.warpPerspective(img, matrix, (size[0], size[1]))
    return imgOutput, matrix


while True:
    success, img = cap.read()

    if counter == 4:
        fileObj = open("map.p", "wb")
        pickle.dump(points, fileObj)
        fileObj.close()
        print("Points saved to file: map.p")


        imgOutput, matrix = warp_image(img, points)
        cv2.imshow("Output Image ", imgOutput)

    for x in range(0, 4):
        cv2.circle(img, (points[x][0], points[x][1]), 3, (0, 255, 0), cv2.FILLED)

    cv2.imshow("Original Image ", img)
    cv2.setMouseCallback("Original Image ", mousePoints)
    cv2.waitKey(1)

cap.release()
cv2.destroyAllWindows()

