> 🌐 本文档由 [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) 翻译,英文原版见原项目。

# TensorFlow C++ MultiBox 目标检测演示

本示例展示如何加载预训练的 TensorFlow 网络,并在 C++ 中检测图像中的物体。另一种实现见
[Android TensorFlow 演示](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/android)

## 说明

本演示使用基于 [Scalable Object Detection using Deep NeuralNetworks](https://arxiv.org/abs/1312.2249) 的模型,检测命令行传入图像中的人物。Android TensorFlow 演示中相机预览里的实时人物检测与跟踪用的也是同一模型。

## 构建 / 安装 / 运行

包含模型定义与权重的 TensorFlow `GraphDef` 因体积原因不随仓库分发。你需要先把文件下载到源码树的 `data` 目录:

```bash
$ wget https://storage.googleapis.com/download.tensorflow.org/models/mobile_multibox_v1a.zip -O tensorflow/examples/multibox_detector/data/mobile_multibox_v1a.zip

$ unzip tensorflow/examples/multibox_detector/data/mobile_multibox_v1a.zip -d tensorflow/examples/multibox_detector/data/
```

只要你能成功构建 TensorFlow 主框架,运行本示例所需的一切就已经就绪。

解压后,查看 data 目录中的 box priors 文件。该文件包含全部 784 个可能检测框的均值与标准差,按左、上、右、下顺序归一化到 0-1。

构建本示例:

```bash
$ bazel build --config opt tensorflow/examples/multibox_detector/...
```

构建完成后会得到一个可执行文件,可以这样运行:

```bash
$ bazel-bin/tensorflow/examples/multibox_detector/detect_objects --image_out=$HOME/x20/surfers_labeled.png
```

它使用框架自带的默认示例图片,输出大致如下:

```
I0125 18:24:13.804047    8677 main.cc:293] ===== Top 5 Detections ======
I0125 18:24:13.804058    8677 main.cc:307] Detection 0: L:324.542 T:76.5764 R:373.26 B:214.957 (635) score: 0.267425
I0125 18:24:13.804077    8677 main.cc:307] Detection 1: L:332.896 T:76.2751 R:372.116 B:204.614 (523) score: 0.245334
I0125 18:24:13.804087    8677 main.cc:307] Detection 2: L:306.605 T:76.2228 R:371.356 B:217.32 (634) score: 0.216121
I0125 18:24:13.804096    8677 main.cc:307] Detection 3: L:143.918 T:86.0909 R:187.333 B:195.885 (387) score: 0.171368
I0125 18:24:13.804104    8677 main.cc:307] Detection 4: L:144.915 T:86.2675 R:185.243 B:165.246 (219) score: 0.169244
```

这里用的是一张公共领域的海滩冲浪者图库照片,得分最高的两个检测框对应画面右侧的两个人。通过 `--num_detections=N` 增加检测数量后,还会包含左侧的冲浪者,以及最终低于某一阈值的非人物框。

你可以打开生成的 png 文件 '~/surfers_labeled.png' 直观查看检测框。

接下来,通过 `--image=` 参数在你自己的图片上试一试,例如:

```bash
$ bazel-bin/tensorflow/examples/multibox_detector/detect_objects --image=my_image.png
```

这项工作的另一实现可参阅 [Android
TensorFlow 演示](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/android)。
