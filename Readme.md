# 说明

本项目基于YOLOv5的框架，主要的功能是实现基于TT100K数据集的交通信号灯与标志牌识别任务。

在YOLOv5的框架下，我所作的主要贡献之一是提供了将TT100K原本的数据集转化为YOLOv5训练所需数据集的格式，具体代码见demox.py，其中x表示数字，之所以会有不同版本的demo是基于不同的情况；共享之二是改进了原本YOLOv5的网络结构，使得改进后的网络对于小目标物体的检测能力得到加强，同时使得网络轻量化，大幅降低了网络参数。

下面是一些我们的实验结果：
![image-20231229170422142](C:\Users\18709\AppData\Roaming\Typora\typora-user-images\image-20231229170422142.png)

![image-20231229170436294](C:\Users\18709\AppData\Roaming\Typora\typora-user-images\image-20231229170436294.png)

![image-20231229170444261](C:\Users\18709\AppData\Roaming\Typora\typora-user-images\image-20231229170444261.png)