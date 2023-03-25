import cv2
img = cv2.imread('monyet.png')
while True:
    cv2.imshow('mandrill',img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.imwrite('final_image.png',img)

cv2.destroyAllWindows()