import json
import os
import numpy as np
import shutil

label_dir = "/rss/zhangxutong/20240122"
txt_label_dir = "/rss/zhangxutong/2023_temp"
'''
txt格式：单双排、车牌、颜色、x、y、w、h、pt1x、pt1y、pt2x、pt2y、pt3x、pt3y、pt4x、pt4y

单双排：单，0；双，1
车牌：label
颜色：blue，green，yellow，yellow-green，white，black，light-green
右下、左下、左上、右上
GitHub上数据集关键点：左上，右上，右下，左下（归一化）x,y是中心点除以图片宽高，w,h是框的宽高除以图片宽高，ptx，pty是关键点坐标除以宽高
'''
def Points(points, img_size):
    x = (abs(points[0][0]-points[2][0])/2+points[2][0])/img_size[0]
    y = (abs(points[0][1]-points[2][1])/2+points[2][1])/img_size[1]
    w = abs(points[0][0]-points[2][0])/img_size[0]
    h = abs(points[0][1]-points[2][1])/img_size[1]
    pt1x = points[0][0]/img_size[0]
    pt1y = points[0][1]/img_size[1]
    pt2x = points[1][0]/img_size[0]
    pt2y = points[1][1]/img_size[1]
    pt3x = points[2][0]/img_size[0]
    pt3y = points[2][1]/img_size[1]
    pt4x = points[3][0]/img_size[0]
    pt4y = points[3][1]/img_size[1]
    print(x,y,w,h,pt1x,pt1y,pt2x,pt2y,pt3x,pt3y,pt4x,pt4y)
    return (x,y,w,h,pt3x,pt3y,pt4x,pt4y,pt1x,pt1y,pt2x,pt2y)
all_data = []
def convert(label_dir, file_name):
    txt_dir = os.path.join(txt_label_dir, file_name.replace(".json",".txt"))
    with open(txt_dir, 'w') as txt_data:
        json_path = os.path.join(label_dir,file_name)
        data = json.load(open(json_path, 'r', encoding='utf-8'))
        img_w = data["imageWidth"]
        img_h = data["imageHeight"]
        color = {"蓝色":"blue", "绿色":"green", "黄色":"yellow", "黄绿":"yellow-green", "白色":"white",
                "黑色":"black", "浅绿":"li-green", "ignore" : "ignore"}
        for type_one in np.arange(len(data["shapes"])):
            dictionary = data["shapes"][type_one]
            label = '0' if dictionary["label"] == "单排" else '1'
            plate_num = dictionary["plate_num"]
            plate_color = color[dictionary["plate_color"]]
            points = Points(dictionary["points"],[img_w,img_h])
            txt_data.write(plate_num+' '+plate_color+' '+label+" "+' '.join([str(pt) for pt in points]))
            txt_data.write('\n')
    txt_data.close()
    if os.path.exists(label_dir.replace("json","img")):
        shutil.copy(os.path.join(label_dir.replace("json","img"),file_name.replace(".json",".jpg")),txt_label_dir)
    else:
        shutil.copy(os.path.join(label_dir.replace("json","jpg"),file_name.replace(".json",".jpg")),txt_label_dir)
    print(txt_dir)
if __name__ == "__main__":
    for droot, ddir, filelist in os.walk(label_dir):
        if len(filelist) > 0:
            for fname in filelist:
                if fname[-5:] == ".json":
                    convert(droot, fname)
