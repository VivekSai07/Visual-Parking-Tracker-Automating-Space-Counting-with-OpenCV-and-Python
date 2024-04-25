
import cv2
import pickle # used to save all the parking location

# img = cv2.imread('carParkImg.png')

width, height = 107, 48


# loads 'CarParkPos', which is the file saved with car positions, 
# if created/exists load it with saved positions, 
# else create a new posList with empty list.  
try:
    with open('CarParkPos', 'rb') as f:
        posList = pickle.load(f)
except:
    posList = []


# MouseClick function to draw rectangle in car park space, 
# erase the rectangle if placed in wrong positions, and
# save the positions (x, y) in posList.
def mouseClick(events, x, y, flags, params):
    if events == cv2.EVENT_LBUTTONDOWN: # mouse click to create a rectangle for car park space
        posList.append((x, y))

    if events == cv2.EVENT_RBUTTONDOWN: # mouse click in between the created rectangle at wrong place
        for i, pos in enumerate(posList):
            x1, y1 = pos
            if x1 < x < x1 + width and y1 < y < y1 + height:
                posList.pop(i)

    with open('CarParkPos', 'wb') as f:
        pickle.dump(posList, f)

while True:
    img = cv2.imread('carParkImg.png')
    # cv2.rectangle(img, (50, 192), (157, 240), (255, 0, 255), 2)
    
    for pos in posList:
        cv2.rectangle(img, pos, (pos[0]+width, pos[1]+height), (255, 0, 255), 2)
        
    cv2.imshow("Image", img)
    cv2.setMouseCallback("Image", mouseClick)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break