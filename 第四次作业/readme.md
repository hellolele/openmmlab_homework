# mmsegmentation 代码作业

##  模型配置文件
[pspnet-watermelonDataset_20230612.py](https://github.com/hellolele/openmmlab_homework/blob/main/%E7%AC%AC%E5%9B%9B%E6%AC%A1%E4%BD%9C%E4%B8%9A/pspnet-watermelonDataset_20230612.py)
## 训练日志
[20230614_194209.log](https://github.com/hellolele/openmmlab_homework/blob/main/%E7%AC%AC%E5%9B%9B%E6%AC%A1%E4%BD%9C%E4%B8%9A/20230614_194209/20230614_194209.log)

## 需提交的测试集评估指标（不能低于 baseline 指标的 50% ）：  

```
aAcc: 60.6200
mIoU: 21.1400
mAcc: 28.4600
```

## 训练结果
```
+------------+-------+-------+
|   Class    |  IoU  |  Acc  |
+------------+-------+-------+
|    red     | 84.45 | 93.26 |
|   green    | 83.15 | 95.04 |
|   white    | 36.92 | 42.69 |
| seed-black | 66.25 | 71.29 |
| seed-white | 53.26 | 58.24 |
| Unlabeled  |  5.65 |  5.68 |
+------------+-------+-------+
06/14 17:17:32 - mmengine - INFO - Iter(val) [11/11]  aAcc: 88.4000  mIoU: 54.9500  mAcc: 61.0300  data_time: 0.0008  time: 0.0970
```

## 模型推理效果
单张测试图片  
![西瓜图片测试](https://github.com/hellolele/openmmlab_homework/blob/main/%E7%AC%AC%E5%9B%9B%E6%AC%A1%E4%BD%9C%E4%B8%9A/watermelon_demo.jpg)