# 题目：基于 ResNet50 的水果分类

## 背景：使用基于卷积的深度神经网络 ResNet50 对 30 种水果进行分类

## 任务

划分训练集和验证集  
按照 MMPreTrain CustomDataset 格式组织训练集和验证集  
使用 MMPreTrain 算法库，编写配置文件，正确加载预训练模型  
在水果数据集上进行微调训练  
使用 MMPreTrain 的 ImageClassificationInferencer 接口，对网络水果图像，或自己拍摄的水果图像，使用训练好的模型进行分类  
需提交的验证集评估指标（不能低于 60%）  
ResNet-50


我的训练  
这次老师没有做数据集的结构化处理，我们需要自己分测试训练和验证，这里图不太多就测试验证同一批图了，具体操作见  
这里我使用了resnet50的预训练网络 https://download.openmmlab.com/mmclassification/v0/resnet/resnet50_8xb32_in1k_20210831-ea4938fc.pth ，迭代了100epoch，具体config请见 

```
Epoch(val) [100][28/28]    accuracy/top1: 93.0180  data_time: 0.0020  time: 0.0271
```
inference一下自己的模型用ImageClassificationInferencer接口，正好刚刚吃完一个西瓜，试一下  
```
(openmmlab) lvjunjie@suzhou-desktop:~/CODE/openmmlab_homework/class_2/mmpretrain/projects/fruit30$ ipython
Python 3.9.16 (main, Mar  8 2023, 14:00:05) 
Type 'copyright', 'credits' or 'license' for more information
IPython 8.4.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from mmpretrain import ImageClassificationInferencer

In [2]: inferencer = ImageClassificationInferencer("./resnet18_finetune.py",pretrained="exp1/epoch_99.pth")
Loads checkpoint by local backend from path: exp1/epoch_99.pth

In [3]: inferencer("./微信图片_20230607145635.jpg")
Inference ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 100% 0:00:00
Out[3]: 
[{'pred_scores': array([1.7108948e-10, 4.9415389e-12, 2.7177219e-11, 8.2835822e-10,
         1.4494353e-07, 8.1413987e-11, 3.1739620e-13, 6.2912418e-12,
         3.6645487e-09, 2.5233808e-12, 1.9508560e-11, 4.6443027e-10,
         6.0838912e-12, 2.5039717e-13, 2.1043712e-11, 4.8427178e-12,
         2.6823875e-12, 3.7887592e-08, 7.9820606e-10, 3.0109234e-08,
         3.1558270e-10, 5.0973132e-11, 7.2481876e-14, 1.7193403e-11,
         5.3435971e-12, 9.9999988e-01, 8.9138086e-10, 4.4663673e-09,
         2.5873173e-13, 2.8021621e-08], dtype=float32),
  'pred_label': 25,
  'pred_score': 0.9999998807907104,
  'pred_class': '西瓜'}]

In [4]: 
```


预测正确