# 作业：基于 RTMDet 的气球检测

## 背景：熟悉目标检测和 MMDetection 常用自定义流程。

## 任务：

基于提供的 notebook，将 cat 数据集换成气球数据集  
按照视频中 notebook 步骤，可视化数据集和标签  
使用MMDetection算法库，训练 RTMDet 气球目标检测算法，可以适当调参，提交测试集评估指标  
用网上下载的任意包括气球的图片进行预测，将预测结果发到群里  
按照视频中 notebook 步骤，对 demo 图片进行特征图可视化和 Box AM 可视化，将结果发到群里 需提交的测试集评估指标（不能低于baseline指标的50%）  
目标检测 RTMDet-tiny 模型性能不能 65 mAP  
数据集 气球数据集可以直接下载 https://download.openmmlab.com/mmyolo/data/balloon_dataset.zip

同时也欢迎各位选择更复杂的数据集进行训练，可以选用一下 10 类的饮料数据集。 https://github.com/TommyZihao/Train_Custom_Dataset/tree/main/%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B/%E7%9B%AE%E6%A0%87%E6%A3%80%E6%B5%8B%E6%95%B0%E6%8D%AE%E9%9B%86

课程当中的ipynb请在下面链接下载： https://github.com/hellolele/openmmlab_homework/blob/main/%E7%AC%AC%E4%B8%89%E6%AC%A1%E4%BD%9C%E4%B8%9A/rtmdet_cat_tutorial.ipynb

训练结果
```
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.739
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.837
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.813
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.541
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.840
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.232
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.804
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.828
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = 0.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = 0.750
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.900
06/11 21:17:41 - mmengine - INFO - bbox_mAP_copypaste: 0.739 0.837 0.813 0.000 0.541 0.840
06/11 21:17:41 - mmengine - INFO - Epoch(test) [13/13]  coco/bbox_mAP: 0.7390  coco/bbox_mAP_50: 0.8370  coco/bbox_mAP_75: 0.8130  coco/bbox_mAP_s: 0.0000  coco/bbox_mAP_m: 0.5410  coco/bbox_mAP_l: 0.8400  data_time: 0.1801  time: 0.1942
```

map0.5 为 0.739  
单张测试图片  
![网络图片测试](https://github.com/hellolele/openmmlab_homework/blob/main/%E7%AC%AC%E4%B8%89%E6%AC%A1%E4%BD%9C%E4%B8%9A/output_image/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20230611213823.png)