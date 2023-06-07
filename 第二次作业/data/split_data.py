import shutil
import os
import random


def split_one_class(fruit_class):
    ## 给每个类别的水果分为test_set 和training_set val_set
    ## 这里就不区分test_set 和val_set了，图不是很多

    total_file = []
    for root ,_,filelist in os.walk("./fruit30/%s"% fruit_class):
        for i in filelist:
            total_file.append(os.path.join(root,i))
    random.shuffle(total_file)
    training_list = total_file[:int(len(total_file)*0.8)]
    val_list = total_file[int(len(total_file)*0.8):]

    for i in training_list:
        if not os.path.exists("./fruit30_data/training_set/%s"% fruit_class):
            os.makedirs("./fruit30_data/training_set/%s"% fruit_class)
        shutil.copy(i,'./fruit30_data/training_set/%s'% fruit_class)
    for i in val_list:
        if not os.path.exists("./fruit30_data/val_set/%s"% fruit_class):
            os.makedirs("./fruit30_data/val_set/%s"% fruit_class)
        shutil.copy(i,'./fruit30_data/val_set/%s'% fruit_class) 

if __name__ == '__main__':
    all_class = os.listdir('fruit30')
    for each_fruit in all_class:
        print(each_fruit)
        split_one_class(each_fruit)