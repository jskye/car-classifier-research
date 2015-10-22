import cv2
import glob

refPt = []
cropping = False
outputfil = "labels.txt"
global imgcounter, roidcounter
imgcounter = 0
roidcounter = 0

def click_and_crop(event, x, y, flags, param):
    global refPt, cropping, imgcounter, roidcounter
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
    elif event == cv2.EVENT_LBUTTONUP:
        roidcounter+=1
        refPt.append((x, y))
        cropping = False
    # else:
    #     tempPt = [(x, y)]
    #     cv2.rectangle(image, tempPt[0], tempPt[1], (255, 255, 0), 2)
        # draw a rectangle around the region of interest
        cv2.rectangle(image, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", image)
        print("imgcounter: "+str(imgcounter))
        # write to output
        if roidcounter > 1:
           print("roidcounter after buttonup (if > 1): "+str(roidcounter))
        else:
           print("othet stuff")
           print("roidcounter after buttonup (else): "+str(roidcounter))
           #write roi data
fils=glob.glob("*.jpg")
for fil in fils:
    print("inloop")
    imgcounter+=1
    print("roidcounter before reset: "+str(roidcounter))
    roidcounter = 0
    print("roidcounter after reset: "+str(roidcounter))
    globalfil = fil
    #write to output
    image = cv2.imread(fil)
    clone = image.copy()
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)

    while True:
        cv2.imshow("image", image)
        key = cv2.waitKey(1) & 0xFF

        if key == ord("r"):
            image = clone.copy()

        elif key == ord("c"):
            break

    cv2.destroyAllWindows()
