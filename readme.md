## 模型结果对比
- 目标检测Baseline模型（RTMDet-tiny）  
  [![242781076-0a1e11f3-5d6d-47b2-8617-06a83a490549](https://user-images.githubusercontent.com/18253636/242839237-e5b8d605-05f3-4e66-a33b-1ce8f8131574.jpg)](https://user-images.githubusercontent.com/18253636/242839237-e5b8d605-05f3-4e66-a33b-1ce8f8131574.jpg)


自训练RTMDet-tiny  

```shell
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.798
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets=100 ] = 0.970
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets=100 ] = 0.950
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.798
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=  1 ] = 0.829
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 10 ] = 0.831
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets=100 ] = 0.831
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= small | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets=100 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets=100 ] = 0.831
06/05 00:45:33 - mmengine - INFO - bbox_mAP_copypaste: 0.798 0.970 0.950 -1.000 -1.000 0.798
06/05 00:45:33 - mmengine - INFO - Epoch(test) [11/11]    coco/bbox_mAP: 0.7980  coco/bbox_mAP_50: 0.9700  coco/bbox_mAP_75: 0.9500  coco/bbox_mAP_s: -1.0000  coco/bbox_mAP_m: -1.0000  coco/bbox_mAP_l: 0.7980  data_time: 0.1936  time: 0.2146
```

- 关键点检测Baseline模型（RTMPose-s）
  [![242781136-3c1eeaa9-3599-4a89-ae01-ca3eddc7f52e](https://user-images.githubusercontent.com/18253636/242839254-171bbd5d-b630-46a7-9df1-8eadb1034b19.png)](https://user-images.githubusercontent.com/18253636/242839254-171bbd5d-b630-46a7-9df1-8eadb1034b19.png)

自训练RTMPose-s

```shell
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=   all | maxDets= 20 ] =  0.720
 Average Precision  (AP) @[ IoU=0.50      | area=   all | maxDets= 20 ] =  1.000
 Average Precision  (AP) @[ IoU=0.75      | area=   all | maxDets= 20 ] =  0.941
 Average Precision  (AP) @[ IoU=0.50:0.95 | area=medium | maxDets= 20 ] = -1.000
 Average Precision  (AP) @[ IoU=0.50:0.95 | area= large | maxDets= 20 ] =  0.720
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=   all | maxDets= 20 ] =  0.760
 Average Recall     (AR) @[ IoU=0.50      | area=   all | maxDets= 20 ] =  1.000
 Average Recall     (AR) @[ IoU=0.75      | area=   all | maxDets= 20 ] =  0.952
 Average Recall     (AR) @[ IoU=0.50:0.95 | area=medium | maxDets= 20 ] = -1.000
 Average Recall     (AR) @[ IoU=0.50:0.95 | area= large | maxDets= 20 ] =  0.760
06/05 01:48:59 - mmengine - INFO - Evaluating PCKAccuracy (normalized by ``"bbox_size"``)...
06/05 01:48:59 - mmengine - INFO - Evaluating AUC...
06/05 01:48:59 - mmengine - INFO - Evaluating NME...
06/05 01:48:59 - mmengine - INFO - Epoch(test) [6/6]    coco/AP: 0.720112  coco/AP .5: 1.000000  coco/AP .75: 0.941319  coco/AP (M): -1.000000 
```



目标检测结果

```shell
python demo/image_demo.py \
        data/test_triangle/demo_ear.jpg \
        data/rtmdet_tiny_ear.py \
        --weights work_dirs/rtmdet_tiny_ear/best_coco_bbox_mAP_epoch_192.pth \
        --out-dir outputs/ \
        --device cuda:0 \
        --pred-score-thr 0.3
```

![image](mmdetection/outputs/vis/demo_ear.jpg)



关键点检测结果

```shell
python demo/topdown_demo_with_mmdet.py \
        data/rtmdet_tiny_ear.py \
        work_dirs/rtmdet_tiny_ear/epoch_192.pth \
        data/rtmpose-s-ear.py \
        work_dirs/rtmpose-s-ear/best_PCK_epoch_270.pth \
        --input data/test/demo_ear.jpg \
        --output-root outputs/G2_Fasterrcnn-RTMPose \
        --device cuda:0 \
        --bbox-thr 0.5 \
        --kpt-thr 0.5 \
        --nms-thr 0.3 \
        --radius 36 \
        --thickness 30 \
        --draw-bbox \
        --draw-heatmap \
        --show-kpt-idx
```

![image](mmpose/output/demo_ear.jpg)
