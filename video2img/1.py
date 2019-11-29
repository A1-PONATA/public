import cv2
import os

video_path = '/home/pirl/img/'
save_path = '/home/pirl/img3/'

action_list = os.listdir(video_path)
for action in action_list:
    if not os.path.exists(save_path+action+'/'):
        os.mkdir(save_path+action)
    video_list = os.listdir(video_path+action)
    idx=0
    for video in video_list:
        prefix = video.split('.')[0]
        if not os.path.exists(save_path+action+'/'+prefix):
            pass
            #os.mkdir(save_path+action+'/'+prefix)
        save_name = save_path + action + '/' + prefix + '/'
        video_name = video_path+action+'/'+video
        cap = cv2.VideoCapture(video_name)
        fps = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        fps_count = 0
        for i in range(fps):
            ret, frame = cap.read()
            if ret:
                cv2.imwrite(save_path+"/"+action+'/'+str(10000+idx)+'.jpg', frame)
                #print(action+'/'+str(10000+idx)+'.jpg')
                fps_count += 1
                idx+=1
                if idx %100 ==0:
                    print(action+'/'+str(10000+idx)+'.jpg')