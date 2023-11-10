import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

'''
Number of Object Labels per Class and Image. This figure shows how often an object occurs in an image. 
Since our labeling efforts focused on cars and pedestrians, these are the most predominant classes here. 
'''

labels_dir = "./labels"
occurrence_number = 100 #横轴长度

def type_number():
    for type_label in np.arange(7):
        number = np.zeros(200)
        for filename in os.listdir(labels_dir):
            file_path = os.path.join(labels_dir, filename)
            with open(file_path, 'r') as file:
                if os.path.getsize(file_path) != 0:
                    temp = 0
                    for file_content in file.readlines():
                        if int(file_content[0]) == type_label:
                            temp += 1
                    if temp != 0:
                        number[temp] += 1
        #number 该图中该类型有多少种
        print(number)
        PerImages_analysis(number, type_label)

#Visualization
def PerImages_analysis(data, name_number):
    type = ['person', 'bike', 'car', 'motor', 'bus', 'truck', 'rider']
    plt.figure(type[name_number])
    plt.bar(x = np.arange(occurrence_number),
            height=data[:occurrence_number],
            alpha=0.7,
            width=0.8,)
    plt.title(type[name_number])
    plt.xticks(np.arange(0, occurrence_number, 25), np.arange(0, occurrence_number, 25))
    plt.xlabel('Number per Image')
    plt.ylabel('NUmber of Images')
    plt.savefig('./'+ type[name_number])
    # plt.show()
if __name__ == "__main__":
    type_number()
