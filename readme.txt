本文件夹主要用频率派且reward分布服从伯努利分布的方法进行ucb的ｍab
mainly use: main,my_model,UCB

score:yellow>blue>red>other
存在问题:
1.状态不能随着action改变，一个动作必须迅速得到结果(在定位器任务中这个是可以接受的)
2.action/state space均为离散值才行(非常不好)
接下来的方向
1. 通过贝叶斯派加高斯分布的方式实现状态空间连续下的躲避赌博机
2. 探讨怎样实现动作空间的连续化(是否要借助深度强化学习了？)