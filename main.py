import cv2 as cv

img = cv.imread("dubu.jpg")

if(len(img.shape)<3):
    cv.imshow("Black and White, GAGI!!!.")
    cv.waitKey(0)
    cv.destroyAllWindows()
if(len(img.shape)==3):
    cv.imshow("dubu", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    print("ACCESS PIXEL:")
    x = int(input("X: "))
    y = int(input("Y: ")) 
    print("PIXEL VALUE: ",img[x,y],"\n")

    print("MODIFY PIXAL VALUES")
    blue = input("Blue (0-255): ")
    green = input("Green (0-255): ")
    red = input("Red (0-255): ")
    print("\nBEFORE: ", img[x, y])
    img.itemset((x, y, 0), blue)
    img.itemset((x, y, 1), green)
    img.itemset((x, y, 2), red)
    print("AFTER: ", img[x, y])

    InDime = img.shape
    fixDime = (255, 255, 0)
    if(InDime[0]>=fixDime[0] and InDime[1]>=fixDime[1]):
        print("\nNOICE!!! The image is within boundary.")
    else:
        print("\nGAGI!!! The image is out of boundary.")

    if(img.size>98989899):
        print("\nThe set pixel is lower than image total pixel count.")
    else:
        print("\nThe set pixel is higher than image total pixel count.")

    print("\nImage Datatype: ", img.dtype,"\n")