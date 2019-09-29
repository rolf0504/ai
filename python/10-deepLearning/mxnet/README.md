# mxnet

書籍 -- https://github.com/d2l-ai/d2l-zh


## mlpGluon1.py

```
PS D:\ccc\course\ai\python\10-deepLearning\mxnet> python mlpGluon1.py
epoch 1, loss 0.7854, train acc 0.706, test acc 0.830
epoch 2, loss 0.4908, train acc 0.819, test acc 0.848
epoch 3, loss 0.4308, train acc 0.840, test acc 0.863
epoch 4, loss 0.3945, train acc 0.853, test acc 0.867
epoch 5, loss 0.3689, train acc 0.862, test acc 0.868
```

## lenet1.py

```
PS D:\ccc\course\ai\python\10-deepLearning\mxnet> python lenet1.py
conv0 output shape:      (1, 6, 24, 24)
pool0 output shape:      (1, 6, 12, 12)
conv1 output shape:      (1, 16, 8, 8)
pool1 output shape:      (1, 16, 4, 4)
dense0 output shape:     (1, 120)
dense1 output shape:     (1, 84)
dense2 output shape:     (1, 10)
[18:05:36] c:\jenkins\workspace\mxnet-tag\mxnet\src\imperative\./imperative_utils.h:91: GPU support is disabled. Compile MXNet with USE_CUDA=1 to enable GPU support.
training on cpu(0)
epoch 1, loss 2.3199, train acc 0.103, test acc 0.100, time 151.1 sec
epoch 2, loss 1.8678, train acc 0.281, test acc 0.574, time 144.8 sec
epoch 3, loss 0.9355, train acc 0.633, test acc 0.702, time 144.9 sec
epoch 4, loss 0.7461, train acc 0.709, test acc 0.735, time 144.8 sec
epoch 5, loss 0.6694, train acc 0.736, test acc 0.757, time 144.9 sec
```