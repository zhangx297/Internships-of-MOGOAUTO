import numpy as np
import os
import cv2

datasets_path = "/rss/zhangxutong/2023_temp"
save_path = "./Small_size_datasets_2"
#400*400
new_size = 200
def resize_image():
    for droot, ddir, filelist in os.walk(datasets_path):
        if len(filelist) > 0:
            for fname in filelist:
                if fname[-4:] == ".txt":
                    label_path = os.path.join(droot,fname)
                    image_path = label_path.replace(".txt", ".jpg")
                    if os.path.exists(image_path):
                        print(image_path)
                        with open(label_path, 'r') as f:
                            lb = np.array([x.split() for x in f.read().strip().splitlines()])
                            img = cv2.imread(str(image_path))
                            img1 = cv2.copyMakeBorder(img, new_size, new_size, new_size, new_size, cv2.BORDER_CONSTANT, value=0)
                            # cv2.imshow('show', img1)
                            h, w = img.shape[:2]
                            i = 0
                            for x in lb:
                                if float(x[4]) > 0.5:
                                    center_point = [float(x[3])*w+new_size, float(x[4])*h+new_size]
                                    y0 = int(center_point[1]-new_size)
                                    y1 = int(center_point[1]+new_size)
                                    x0 = int(center_point[0]-new_size)
                                    x1 = int(center_point[0]+new_size)
                                    cropped = img1[y0:y1, x0:x1]
                                    # cv2.imshow('show', cropped)
                                    save = os.path.join(save_path,str(i)+'_'+fname.replace(".txt", ".jpg"))
                                    cv2.imwrite(save, cropped)
                                    i += 1
                                    cv2.waitKey(0)
                                    cv2.destroyAllWindows()
                                    lb_small_size = convert_small(list(x), [w, h])
                                    with open(save.replace(".jpg", ".txt"), 'w') as txt_label:
                                        txt_label.write(" ".join([str(pt) for pt in lb_small_size]))
                                        txt_label.write('\n')

def convert_small(x, image_size):
    small_label = []
    # print(x)
    small_label.append(float(x[2]))
    for a in range(2):
        small_label.append(0.5)
    w_small_size = float(x[5])*image_size[0]
    h_small_size = float(x[6])*image_size[1]
    [w_normalization,h_normalization] = w_small_size/(2*new_size), h_small_size/(2*new_size)
    x1 = (new_size-float(w_small_size/2))/(2*new_size)
    y1 = (new_size-float(h_small_size/2))/(2*new_size)
    x2 = (new_size+float(w_small_size/2))/(2*new_size)
    y2 = (new_size-float(h_small_size/2))/(2*new_size)
    x3 = (new_size+float(w_small_size/2))/(2*new_size)
    y3 = (new_size+float(h_small_size/2))/(2*new_size)
    x4 = (new_size-float(w_small_size/2))/(2*new_size)
    y4 = (new_size+float(h_small_size/2))/(2*new_size)
    for temp in [w_normalization,h_normalization, x1, y1, x2, y2, x3, y3, x4, y4]:
        small_label.append(temp)
    small_label = np.array(small_label, dtype=np.float32)
    print(small_label)
    return small_label

if __name__ == "__main__":
    resize_image()
