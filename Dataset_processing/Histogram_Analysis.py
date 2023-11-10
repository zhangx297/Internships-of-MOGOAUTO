import os
import numpy as np
import matplotlib.pyplot as plt

labels_dir = "./labels_new"

#analyzed number of types
types_numbers = np.zeros(7)
def data_type():
    for filename in os.listdir(labels_dir):
        file_path = os.path.join(labels_dir, filename)
        with open(file_path, 'r') as file:
            if os.path.getsize(file_path) != 0:
                for file_content in file.readlines():
                    types_numbers[int(file_content[0])] += 1
    # type_numbers in the dataset
    # print(types_numbers)
    histogram(types_numbers)

#Visualization
def histogram(data):
    print(data)
    type = ['person', 'bike', 'car', 'motor','bus', 'truck', 'rider']
    plt.bar(x = np.arange(7),
            height=data,
            alpha=0.7,
            tick_label=type,
            width=1,
            label='type_number',)
    for i in np.arange(7):
        plt.text(x = i-0.45, y = data[i]+1000, s = "%.2f%%" % (data[i]*100/sum(data)))
    # plt.savefig('./直方图')
    plt.savefig('./新直方图')

if __name__ == "__main__":
    data_type()

