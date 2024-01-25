import numpy as np
import os
import cv2

datasets_path = "/rss/zhangxutong/2023_temp"
save_path = "./datasets"
#400*400
new_size = 200
def resize_image():
    for droot, ddir, filelist in os.walk(datasets_path):
        if len(filelist) > 0:
            for fname in filelist:
                if fname[-4:] == ".txt":
                    label_path = os.path.join(droot,fname)
                    with open(label_path, 'r') as f:
                        lb = np.array([x.split() for x in f.read().strip().splitlines()])
                            # cv2.imshow('show', img1)
                        #h, w = img.shape[:2]
                        i = 0
                        for x in lb:
                            if float(x[4]) > 0.5:
                                print("ok")
                                    #center_point = [float(x[3])*w+new_size, float(x[4])*h+new_size]
                                    #y0 = int(center_point[1]-new_size)
                                    #y1 = int(center_point[1]+new_size)
                                    #x0 = int(center_point[0]-new_size)
                                    #x1 = int(center_point[0]+new_size)
                                    #cropped = img1[y0:y1, x0:x1]
                                    # cv2.imshow('show', cropped)
                                    #save = os.path.join(save_path,str(i)+'_'+fname.replace(".txt", ".jpg"))
                                    #cv2.imwrite(save, cropped)
                                    #i += 1
                                    #cv2.waitKey(0)
                                    #cv2.destroyAllWindows()
                                    #lb_small_size = convert_small(list(x), [w, h])
                                    #with open(save.replace(".jpg", ".txt"), 'w') as txt_label:
                                     #   txt_label.write(" ".join([str(pt) for pt in lb_small_size]))
                                    #    txt_label.write('\

if __name__ == "__main__":
    resize_image()
