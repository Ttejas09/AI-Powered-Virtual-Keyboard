import cv2
from cvzone.HandTrackingModule import HandDetector
import cvzone
from time import sleep
from pynput.keyboard import Controller

video = cv2.VideoCapture(0) # 0 for inbuilt, 1 for external

# Set Resolution (Optional - depends on camera support)
video.set(3, 1280) # Width
video.set(4, 720)  # Height

detector = HandDetector(detectionCon=0.85)
keys = [["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P"],
        ["A", "S", "D", "F", "G", "H", "J", "K", "L", ";"],
        ["Z", "X", "C", "V", "B", "N", "M", ",", ".", "/"]]
finalText = ""
keyboard = Controller()

def drawAll(frame, buttonList):
    for button in buttonList:
        x, y = button.pos
        w, h = button.size
        cvzone.cornerRect(frame, (button.pos[0], button.pos[1], button.size[0], button.size[1]),
                          20, rt=0)
        cv2.rectangle(frame, button.pos, (x + w, y + h), (0, 0, 0), cv2.FILLED)
        cv2.putText(frame, button.text, (x + 20, y + 65),
                    cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
    return frame

class Button():
    def __init__(self, pos, text, size=[85, 85]):
        self.pos = pos
        self.size = size
        self.text = text

buttonList = []
for i in range(len(keys)):
    for j, key in enumerate(keys[i]):
        buttonList.append(Button([100 * j + 50, 100 * i + 50], key))

while True:
    success, frame = video.read()

    if not success:
        print("Failed to read frame from camera. Exiting...")
        break

    
    frame = cv2.flip(frame, 1) 

    # findHands returns the list of hands AND the annotated image
    hands, frame = detector.findHands(frame)

    landmark_list = []
    bounding_box = []
    frame = drawAll(frame, buttonList)

    if hands:
        # We only look at the first hand detected (hands[0])
        hand = hands[0]
        landmark_list = hand["lmList"]
        bounding_box = hand["bbox"]
        # print(landmark_list) 
    if landmark_list:
        for button in buttonList:
            x, y = button.pos
            w, h = button.size

            if x < landmark_list[8][0] < x + w and y < landmark_list[8][1] < y + h:
                cv2.rectangle(frame, (x - 5, y - 5), (x + w + 5, y + h + 5), (175, 0, 175), cv2.FILLED)
                cv2.putText(frame, button.text, (x + 20, y + 65),
                            cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                l, _, _ = detector.findDistance(landmark_list[8][0:2], landmark_list[12][0:2], img=frame)
                print(l)

                ## when clicked
                if l < 20:
                    keyboard.press(button.text)
                    cv2.rectangle(frame, button.pos, (x + w, y + h), (0, 255, 0), cv2.FILLED)
                    cv2.putText(frame, button.text, (x + 20, y + 65),
                                cv2.FONT_HERSHEY_PLAIN, 4, (255, 255, 255), 4)
                    finalText += button.text
                    sleep(0.5)
    
    cv2.rectangle(frame, (50, 350), (700, 450), (175, 0, 175), cv2.FILLED)
    cv2.putText(frame, finalText, (60, 430),
                cv2.FONT_HERSHEY_PLAIN, 5, (255, 255, 255), 5)

    cv2.imshow("Keyboard", frame)
    
    # Press 'esc' to quit, 27 = ascii value of esc key
    if cv2.waitKey(1) & 0xFF == 27:
        print('Quitting...')
        break

video.release()
cv2.destroyAllWindows()