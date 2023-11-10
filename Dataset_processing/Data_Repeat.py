import os
import numpy as np
import shutil
import heapq


labels_dir = "labels"
filter_labels_dir = "./filter.txt"
new_labels_dir = "labels_new"
new_images_dir = "images_new"
types_numbers = np.zeros(7) #analyzed types
"1 bike; 4 bus; 5 track"
choose_type = [1, 4, 5]
choose_perimage_number = [2, 4, 6]

#filter data
def data_type():
    # filter_path = os.mkdir(filter_dir)
    # with open(os.chmod(filter_dir, 0o755), 'w') as write_file:
    with open(filter_labels_dir, 'w') as write_file:
        for type_label in choose_type:
            for filename in os.listdir(labels_dir):
                file_path = os.path.join(labels_dir, filename)
                with open(file_path, 'r') as file:
                    if os.path.getsize(file_path) != 0:
                        temp = 0
                        for file_content in file.readlines():
                            if int(file_content[0]) == type_label:
                                temp += 1
                        if temp >= choose_perimage_number[choose_type.index(type_label)]:
                            write_file.write(file_path+'\n')
    write_file.close()

#repeat data
def repeat():
    with open(filter_labels_dir, 'r') as file:
        for file_label_dir in file.readlines():
            shutil.copy(file_label_dir[:-1], new_labels_dir)
            file_image_dir = file_label_dir[:-1].replace('labels','images').replace('.txt','.jpg')
            if os.path.exists(file_image_dir):
                shutil.copy(file_image_dir, new_images_dir)

#save dir
labels_new_dir = "labels_new"
images_new_dir = "images_new"

#rename
def rename():
    for filename in os.listdir(labels_new_dir):
        file_path = os.path.join(labels_new_dir, filename)
        os.rename(file_path, os.path.join(labels_new_dir, 'copy_' + filename))
    for filename in os.listdir(images_new_dir):
        file_path = os.path.join(images_new_dir, filename)
        os.rename(file_path, os.path.join(images_new_dir, 'copy_' + filename))

if __name__ == "__main__":
    # data_type()
    # repeat()
    rename()