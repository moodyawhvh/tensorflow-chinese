> 🌐 本文档由 [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) 翻译,英文原版见原项目。

# TensorFlow C++ 与 Python 图像识别演示

本示例展示如何加载预训练的 TensorFlow 网络,并在 C++ 中用它识别图像中的物体。Java 版见 [Java
README](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/java),Go 版见 [godoc
示例](https://godoc.org/github.com/tensorflow/tensorflow/tensorflow/go#ex-package)。

## 说明

本演示使用 Google Inception 模型,对命令行传入的图像文件进行分类。

## 构建 / 安装 / 运行

包含模型定义与权重的 TensorFlow `GraphDef` 因体积原因不随仓库分发。你需要先把文件下载到源码树的 `data` 目录:

```bash
$ curl -L "https://storage.googleapis.com/download.tensorflow.org/models/inception_v3_2016_08_28_frozen.pb.tar.gz" |
  tar -C tensorflow/examples/label_image/data -xz
```

只要你能成功构建 TensorFlow 主框架,运行本示例所需的一切就已经就绪。

解压后,可以查看 data 目录中的标签文件了解所有可能类别,即 ImageNet 竞赛使用的 1000 个类别。

构建本示例:

```bash
$ bazel build tensorflow/examples/label_image/...
```

构建完成后会得到一个可执行文件,可以这样运行:

```bash
$ bazel-bin/tensorflow/examples/label_image/label_image
```

它使用框架自带的默认示例图片,输出大致如下:

```
I tensorflow/examples/label_image/main.cc:206] military uniform (653): 0.834306
I tensorflow/examples/label_image/main.cc:206] mortarboard (668): 0.0218692
I tensorflow/examples/label_image/main.cc:206] academic gown (401): 0.0103579
I tensorflow/examples/label_image/main.cc:206] pickelhaube (716): 0.00800814
I tensorflow/examples/label_image/main.cc:206] bulletproof vest (466): 0.00535088
```

这里用的是 Grace Hopper 海军上将的默认图片,可以看到网络正确识别出她身穿军装,得分高达 0.8。

接下来,通过 `--image=` 参数在你自己的图片上试一试,例如:

```bash
$ bazel-bin/tensorflow/examples/label_image/label_image --image=my_image.png
```

想深入了解这段代码,可以阅读 [Inception 教程](https://github.com/tensorflow/docs/blob/master/site/en/r1/tutorials/images/image_recognition.md)的 C++ 部分。

## Python 实现

label_image.py 是与上述 C++ 代码对应的 Python 实现。相比
[Inception 教程](https://github.com/tensorflow/docs/blob/master/site/en/r1/tutorials/images/image_recognition.md)中提到的 Python 代码,它与 C++ 版本的映射更直观,
也更容易加入可视化或调试代码。

执行

```bash
$ bazel build tensorflow/examples/label_image/...
```

之后会生成 `bazel-bin/tensorflow/examples/label_image/label_image_py`。

运行:

```bash
$ bazel-bin/tensorflow/examples/label_image/label_image_py
```

或者,在已安装 TensorFlow Python 包的环境下:

```bash
$ python3 tensorflow/examples/label_image/label_image.py
```

输出结果大致如下:
```
military uniform 0.834305
mortarboard 0.0218694
academic gown 0.0103581
pickelhaube 0.00800818
bulletproof vest 0.0053509
```
