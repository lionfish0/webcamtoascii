import cv2
import numpy as np

def ascii_draw(mat):
    symbols = np.array([s for s in ' .,:-=+*X#@@'])#[::-1]
    msg = ""
    mat = (11*mat/(np.max(mat)+1)).astype(int)
    mat[mat<0] = 0
    for i in range(0,len(mat),2):
        msg+=''.join(symbols[mat][i])+"\n"
    return msg
    
def run():
    cam = cv2.VideoCapture(0)

    while True:
        check, frame = cam.read()
        if frame is None: continue
        resized_frame = cv2.resize(np.mean(frame,2), (140,90)) #(91,53))
        #print(ascii_draw(np.mean(frame[::9,::7],2)))
        print(ascii_draw(resized_frame))

        key = cv2.waitKey(1)
        if key == 27:
            break

    cam.release()
    cv2.destroyAllWindows()
    
run()
