import os
from pathlib import Path
import shutil

sub_list = [11,12,16,19,23,28,52,56,61,65,68,74,79,84,89,98,101,104,108,114,120,123,130,134,137,141,147,150,
       154,159,166,173,178,180,187,191,196,201,206,212,217,224,227,232,237,240,245,255,263,270,273,280,287,
            290,294,302,304,310]

# for i in range(len(sub_list)):
for i in range(1):
    sub = sub_list[i]
    print(sub)
    Original_Path_A = Path('/Users/dongwang/new_experiment/data_process/sub_' +str(sub)+ '/trainA/')
    Original_Path_B = Path('/Users/dongwang/new_experiment/data_process/sub_' +str(sub)+ '/trainB/')
    FileList_A = list(Original_Path_A.glob("*.jpg"))
    FileList_B = list(Original_Path_B.glob("*.jpg"))
    os.mkdir('/Users/dongwang/new_experiment/data_pairs/sub_'+ str(sub) +'_pairs')
    os.mkdir('/Users/dongwang/new_experiment/data_pairs/sub_'+ str(sub) +'_pairs/A')
    os.mkdir('/Users/dongwang/new_experiment/data_pairs/sub_'+ str(sub) +'_pairs/B')
# os.mkdir('/Users/dongwang/new_experiment/data_process/sub_'+ str(sub) +'_pairs')

# 定义个list，其中是 Original_Path_A 中 Part3 部分在 Original_B 中无对应的文件名称。
    Orginal_A_No_Part3 = []
    for File_A in FileList_A:
    
        File_Name_A = os.path.split(File_A)[1].split('.')[0]  # 将文件夹中各个文件的文件名读取出来

#         print(File_Name_A)

    # 将 File_Name_A 中的文件名字以下划线为间隔分割为 3 个不同的部分，分别为 FNA_P1, FNA_P2, FNA_P3;
        FNA_P1 = File_Name_A.split('_')[0]
        FNA_P2 = File_Name_A.split('_')[1]
        FNA_P3 = File_Name_A.split('_')[2]

#         print(FNA_P3)

    # 对该操作文件的文件，对 Original_B 下的文件进行对比。
        Pair_Flag = 0
        Distance = 10000
        Have_P3 = 0   # 这里 的标记是看是否存在有FNA_P3，却无 FNB_P3 的情况。
        for File_B in FileList_B:
            File_Name_B = os.path.split(File_B)[1].split('.')[0]

        # 将 File_Name_A 中的文件名字以下划线为间隔分割为 3 个不同的部分，分别为 FNA_P1, FNA_P2, FNA_P3;
            FNB_P1 = File_Name_B.split('_')[0]
            FNB_P2 = File_Name_B.split('_')[1]
            FNB_P3 = File_Name_B.split('_')[2]

        # 在确保第 3 部分相同的情况下，寻找 Original_B 中第 2 部分最相近的文件。

            if FNB_P3 == FNA_P3:
                Have_P3 = 1
                if Distance > abs(int(FNA_P2) - int(FNB_P2)):
                    Distance = abs(int(FNA_P2) - int(FNB_P2))
#                     print(Distance)
#                     if Distance <=2:
                    Pair_Flag = FNB_P2

#         print(Have_P3)
        if Have_P3 == 1:  # 如果B 文件夹中不存在与FNA_P3对应的文件，则不拷贝两个文件。
        # 将 File_Name_A 拷贝到 Result/A 中，文件名不变。
            shutil.copy(File_A, '/Users/dongwang/new_experiment/data_pairs/sub_'+str(sub)+'_pairs/A')

        # 将 Pair_Flag 作为第二部分，将相应的 Original_B 拷贝到 Result/B 中，文件名称改为 FNA_P2 的元素。
            shutil.copy('/Users/dongwang/new_experiment/data_process/sub_'+str(sub)+'/trainB/' + FNA_P1 + '_' + Pair_Flag + '_' +
                    FNA_P3 + '.jpg', '/Users/dongwang/new_experiment/data_pairs/sub_' + str(sub)+'_pairs/B/' + File_Name_A + '.jpg')
        else:
            Orginal_A_No_Part3.append(File_Name_A)
    
#     k+=1

#     print(Orginal_A_No_Part3)

