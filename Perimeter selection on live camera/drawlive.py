import cv2
import numpy as np
import keyboard
cap = cv2.VideoCapture('st2.mp4')
all_rect = []
crop = False
rectangle = False
ix,iy = -1,-1
fx,fy = -1,-1
line_draw = []
drawings = []
global mykey
keyx = None
cropped_frames = []
global poly_points
poly_points = []
show_mask = False

# def draw_lines(event,x,y,flags,params):
#     global ix,iy,fx,fy
#     if event == cv2.EVENT_LBUTTONDOWN:
#         rectangle = True 
#         ix,iy = x,y
def region_of_interest(points,frame):
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    points = np.array(points,'int32')
    print(points)
    mask = np.zeros_like(frame)
    cv2.fillConvexPoly(mask,points,(255,255,255) )
    #condition = np.stack((mask,), axis=-1) 
    #print(condition.shape)
    print(frame.shape)
    colorMask = cv2.bitwise_and(frame,mask,mask = None)
    xmin = min(points[:,0])
    xmax = max(points[:,0])
    ymin = min(points[:,1])
    ymax = max(points[:,1])
    colorMask = colorMask[ymin:ymax,xmin:xmax]
    #output_image = np.where(condition,frame, mask)
    return colorMask



def draw_rectangle(event,x,y,flags,params):
    global ix,iy,fx,fy,rectangle
    if mykey =='a':
        if event == cv2.EVENT_LBUTTONDOWN:
            rectangle = True
            ix,iy = x,y
            fx,fy = -1,-1
        elif event == cv2.EVENT_MOUSEMOVE:
            if rectangle:
                fx,fy = x,y
        elif event == cv2.EVENT_LBUTTONUP:
            rectangle = False
            fx,fy = x,y
            line_draw.append([(ix,iy),(fx,fy)])
            poly_points.append((ix,iy))
       
            ix,iy = -1,-1
            fx,fy = -1,-1

    if mykey=='b':
        if event == cv2.EVENT_LBUTTONDOWN:
            rectangle = True
            ix,iy = x,y
            cv2.circle(frame,(ix,iy),1,(0,255,0),2)
        elif event == cv2.EVENT_MOUSEMOVE:
            if rectangle:
                fx,fy = x,y
        elif event == cv2.EVENT_LBUTTONUP:
            rectangle = False
            fx,fy = x,y
            all_rect.append([(ix,iy),(fx,fy)])
            ix,iy = -1,-1
            fx,fy = -1,-1




while True:
    
    cv2.namedWindow('Webcam')
    cv2.setMouseCallback('Webcam',draw_rectangle)
    keyx = cv2.waitKey(1) & 0xFF
    if keyx==ord('c'):crop=True
    # if crop:
    #     r = cv2.selectROI(frame,False,False)
    #     print(r)
    #     cropped_image = frame[int(r[1]):int(r[1]+r[3]), 
    #                 int(r[0]):int(r[0]+r[2])]
    if crop:
        for f in cropped_frames:
            cv2.imshow('f',f)
            cv2.waitKey(100)


    ret,frame = cap.read()
    frame = cv2.resize(frame,(1280,720), interpolation = cv2.INTER_AREA)
    if cv2.waitKey(1)==ord('a'):
        mykey = 'a'
    #if rectangle:
    #all_rect.append(cv2.rectangle(frame,(ix,iy),(fx,fy),(0,255,0),2))
    # if keyboard.read_key() == 'a':
    #     mykey = 'a'
    elif cv2.waitKey(1)==ord('b'):
        mykey = 'b'

    # if mykey:
    #     if mykey=='a':
            
    #     if mykey=='b':
    print(all_rect) 
    if line_draw:

        for lines in line_draw:
                cv2.line(frame,lines[0],lines[1],(0,255,0),2)
                
    if cv2.waitKey(1)==ord('l'):
        show_mask = True
        # for lines in line_draw:
        #     cv2.line(frame,lines[0],lines[1],(0,255,0),2)
                
            #poly_points.append(lines[0])
    if show_mask:
        print(poly_points)
        img = region_of_interest(poly_points,frame)
        cv2.imshow('img',img)
        cv2.waitKey(10)   
            
            
    for lines in all_rect:
            cv2.rectangle(frame,lines[0],lines[1],(0,255,0),2)
            crops = frame[lines[0][1]:lines[0][0],lines[0][0]:lines[1][0]]
            cropped_frames.append(crops)
            
    # if cv2.waitKey(1)==ord('s'):
    #     cv2.rectangle(frame,(ix,iy),(fx,fy),(0,255,0),2)
    #     ix,iy = -1,-1
    #     fx,fy = -1,-1



    #
    # for rect in all_rect:
    #     rect

    
    cv2.imshow('Webcam',frame)

    # ix,iy = -1,-1
    # fx,fy = -1,-1

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllwindows()
        


    
    

    



