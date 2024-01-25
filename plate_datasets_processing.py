import numpy as np
import os
import cv2

datasets_path = "/rss/zhangxutong/2023_temp"
#save_path = "/rss/zhangxutong/2023_Q4_recognition_datasets"

def resize_image():
    for droot, ddir, filelist in os.walk(datasets_path):
        if len(filelist) > 0:
            for fname in filelist:
                if fname[-4:] == ".txt":
                    label_path = os.path.join(droot,fname)
                    image_path = label_path.replace(".txt", ".jpg")
                    if os.path.exists(image_path):
                        #print(image_path)
                        with open(label_path, 'r') as f:
                            lb = np.array([x.split() for x in f.read().strip().splitlines()])
                            img = cv2.imread(str(image_path))
                            # cv2.imshow('show', img1)
                            h, w = img.shape[:2]
                            i = 0
                            for x in lb:
                                save_path = "/rss/zhangxutong/2023_Q4_color/2024_Q1_recognition_datasets_0"
                                if float(x[4])>0:  #image position
                                    #print(x)
                                    print(h,w)
                                    #label x y w h  pt1x pt1y pt2x pt2y pt3x pt3y pt4x pt4y
                                    center_point = [float(x[3])*w, float(x[4])*h]
                                    box_size = [float(x[5])*w, float(x[6])*h]
                                    y0 = max(int(center_point[1]-box_size[1]),0)
                                    y1 = min(int(center_point[1]+box_size[1]),h)
                                    x0 = max(int(center_point[0]-box_size[0]),0)
                                    x1 = min(int(center_point[0]+box_size[0]),w)
                                    if y0 == y1:
                                        y0 -= 1
                                        y1 += 1
                                    print(y0,y1,x0,x1)
                                    img1 = img[y0:y1, x0:x1]
                                    # cv2.imshow('show', cropped)
                                    save_p = os.path.join(save_path,str(x[1]))
                                    if os.path.exists(save_p):
                                        save = os.path.join(save_p,str(i)+'_'+fname.replace(".txt", ".jpg"))
                                        print(save)
                                        if img1.size is not None:
                                            cv2.imwrite(save, img1)
                                            i += 1
                                            cv2.waitKey(0)
                                            cv2.destroyAllWindows()
                                        #save_path = "/rss/zhangxutong/2023_Q4_recognition_datasets"
if __name__ == "__main__":
    resize_image()
