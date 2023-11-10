import os
import shutil
import random

add_list=["E:/Chinese_license_plate_detection_recognition-main/detect_plate_datasets"]

labels_dir = "/data_hengyang/copy_data/little_data/lables"
images_dir = "/data_hengyang/copy_data/little_data/images"
all_data = []
def add_data():
    #find all data names
    for subdir in add_list:
        for droot, ddir, filelist in os.walk(subdir):
            if len(filelist) > 0:
                for fname in filelist:
                    if fname[-4:] == ".txt":
                        all_data.append(os.path.join(droot, fname))
    print("all data: ", len(all_data))

    # random mix all_data
    random.shuffle(all_data)
    train_num = int(len(all_data) * 0.95)
    train_data = all_data[:train_num]
    val_data = all_data[train_num:]

    # put train data
    for train_label in train_data:
        train_image = train_label.replace("txt", "jpg")
        if os.path.exists(train_image):
            shutil.copy(train_label, os.path.join(labels_dir, "train"))
            shutil.copy(train_image, os.path.join(images_dir, "train"))
            print("Train: ", train_label)
    print("train data: ", len(train_data))

    # put val data

    for val_label in val_data:
        val_image = val_label.replace(".txt", ".jpg")
        if os.path.exists(val_image):
            shutil.copy(val_label, os.path.join(labels_dir, "val"))
            shutil.copy(val_image, os.path.join(images_dir, "val"))
            print("Val: ", val_label)
    print("train data: ", len(val_data))

if __name__=="__main__":
    add_data()
