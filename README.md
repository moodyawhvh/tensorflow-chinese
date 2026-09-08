<div align="center">

# tensorflow 中文翻译版

**[中文版] tensorflow — Google 开源的端到端机器学习平台,覆盖训练、推理与跨平台部署**

[![原项目](https://img.shields.io/badge/原项目-tensorflow--tensorflow-blue?style=flat-square&logo=github)](https://github.com/tensorflow/tensorflow)
[![中文文档](https://img.shields.io/badge/中文文档-README.zh--CN.md-orange?style=flat-square)](README.zh-CN.md)
[![GitHub Stars](https://img.shields.io/github/stars/tensorflow/tensorflow?style=flat-square&label=原项目Stars)](https://github.com/tensorflow/tensorflow/stargazers)
[![微信联系](https://img.shields.io/badge/微信-uaycar-brightgreen?style=flat-square&logo=wechat)](#)

</div>

---

> 这是 [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) 的中文翻译版本。
> 完整源代码请访问原项目:https://github.com/tensorflow/tensorflow

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

---

## 📖 项目简介

TensorFlow 是一个端到端的开源机器学习平台,最初由 Google Brain 团队开发,现已成为业界最广泛使用的深度学习框架之一。它提供了完整而灵活的工具、库和社区资源生态,既支持研究人员探索机器学习前沿,也让开发者能够轻松构建并部署由机器学习驱动的应用。

TensorFlow 提供稳定的 Python 和 C++ API,并通过 TensorFlow Lite、TensorFlow.js 等延伸项目覆盖服务器、移动端、浏览器与嵌入式边缘设备,实现"一次建模,处处运行"。

## ✨ 主要特性

- **端到端机器学习平台**:从数据准备、模型训练、评估到部署上线的完整工作流
- **Keras 高层 API**:简洁易用的模型构建接口,同时保留底层自定义能力
- **稳定的 Python 与 C++ API**:并提供 Java、JavaScript 等其他语言接口
- **GPU / TPU 加速**:原生支持 CUDA GPU 与 Google TPU 分布式训练
- **多平台部署**:TensorFlow Lite(移动与边缘设备)、TensorFlow.js(浏览器)、TensorFlow Serving(服务端)
- **丰富生态**:TensorBoard 可视化、TensorFlow Hub 预训练模型、官方模型库与示例
- **活跃社区**:完善的教程、博客、论坛与课程资源
- **Apache 2.0 开源协议**:可自由用于个人与商业项目

## 📁 文件说明

| 文件 | 说明 |
|:-----|:-----|
| README.md | 本文件(中文简介) |
| README.zh-CN.md | 详细中文文档(完整汉化) |

## 🚀 快速开始

1. 安装当前稳定版(支持 CUDA GPU,Ubuntu 与 Windows):

```
 pip install tensorflow
```

2. 仅需 CPU 版本时,可安装更小的独立包:

```
 pip install tensorflow-cpu
```

3. 升级到最新版本时,在上述命令后加上 `--upgrade` 参数;测试新特性可安装 `tf-nightly` 夜间构建包。

4. 运行你的第一个 TensorFlow 程序:

```shell
$ python
```

```python
>>> import tensorflow as tf
>>> tf.add(1, 2).numpy()
3
>>> hello = tf.constant('Hello, TensorFlow!')
>>> hello.numpy()
b'Hello, TensorFlow!'
```

5. 更多示例请参阅 [TensorFlow 官方教程](https://www.tensorflow.org/tutorials/),GPU 支持、Docker 与源码编译等安装方式见[官方安装指南](https://www.tensorflow.org/install)。

完整源代码与最新版本请访问原项目:https://github.com/tensorflow/tensorflow

## 📞 联系方式

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

---

本项目为 [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) 的中文翻译版本,所有代码版权归原项目作者所有,遵循其原始许可证(Apache License 2.0)。

**如果觉得有用,请给原项目点个 Star!** ⭐
