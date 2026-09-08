<div align="center">

# tensorflow 中文文档

**[中文翻译版] tensorflow — 端到端开源机器学习平台**

[![原项目](https://img.shields.io/badge/原项目-tensorflow--tensorflow-blue?style=flat-square&logo=github)](https://github.com/tensorflow/tensorflow)
[![原版 README](https://img.shields.io/badge/原版文档-English-blue?style=flat-square)](https://github.com/tensorflow/tensorflow#readme)
[![微信联系](https://img.shields.io/badge/微信-uaycar-brightgreen?style=flat-square&logo=wechat)](#)

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

</div>

---

> 本文档是 [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) 官方 README 的中文翻译版本,仅供学习参考;如有歧义,请以英文原文为准。
> 完整源代码请访问原项目:https://github.com/tensorflow/tensorflow

---

## 📖 项目简介

[TensorFlow](https://www.tensorflow.org/) 是一个端到端的开源机器学习平台。它拥有全面而灵活的生态系统,涵盖各类[工具](https://www.tensorflow.org/resources/tools)、[库](https://www.tensorflow.org/resources/libraries-extensions)与[社区](https://www.tensorflow.org/community)资源,既能让研究人员推动机器学习领域的前沿进展,也能让开发者轻松构建并部署由机器学习驱动的应用程序。

TensorFlow 最初由 Google Brain 机器智能团队的研究员与工程师开发,用于开展机器学习与神经网络方面的研究;如今该框架已经足够通用,同样可以胜任其他领域的任务。

TensorFlow 提供稳定的 [Python](https://www.tensorflow.org/api_docs/python) 和 [C++](https://www.tensorflow.org/api_docs/cc) API,并为[其他语言](https://www.tensorflow.org/api_docs)提供不保证向后兼容的 API。

如需及时了解版本发布与安全更新,可订阅 [announce@tensorflow.org](https://groups.google.com/a/tensorflow.org/forum/#!forum/announce) 邮件列表;全部邮件列表见 [TensorFlow 社区论坛](https://www.tensorflow.org/community/forums)。

## 📦 安装

详细安装方式请参考 [TensorFlow 安装指南](https://www.tensorflow.org/install),其中包括:[pip 包安装](https://www.tensorflow.org/install/pip)、[启用 GPU 支持](https://www.tensorflow.org/install/gpu)、[Docker 容器](https://www.tensorflow.org/install/docker)以及[从源码构建](https://www.tensorflow.org/install/source)。

安装当前稳定版(支持 CUDA GPU 显卡,*Ubuntu 与 Windows*):

```
 pip install tensorflow
```

其他设备(DirectX 与 MacOS-metal)可通过[设备插件(Device Plugins)](https://www.tensorflow.org/install/gpu_plugins#available_devices)获得支持。

也有体积更小的纯 CPU 版本包:

```
 pip install tensorflow-cpu
```

在上述命令后加上 `--upgrade` 参数即可升级到最新版本。

*夜间构建(Nightly)版本可通过 PyPI 上的 [tf-nightly](https://pypi.python.org/pypi/tf-nightly) 与 [tf-nightly-cpu](https://pypi.python.org/pypi/tf-nightly-cpu) 包获取,用于测试新特性。*

### 🧪 尝试你的第一个 TensorFlow 程序

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

更多示例请参阅 [TensorFlow 官方教程](https://www.tensorflow.org/tutorials/)。

## 🤝 贡献指南

**如果你想为 TensorFlow 贡献代码,请先阅读[贡献指南](https://github.com/tensorflow/tensorflow/blob/master/CONTRIBUTING.md)。本项目遵循 TensorFlow [行为准则](https://github.com/tensorflow/tensorflow/blob/master/CODE_OF_CONDUCT.md),参与本项目即表示你同意遵守该准则。**

**项目使用 [GitHub Issues](https://github.com/tensorflow/tensorflow/issues) 跟踪需求与缺陷;一般性问题和讨论请前往 [TensorFlow Forum](https://discuss.tensorflow.org/);具体的技术问题请到 [Stack Overflow](https://stackoverflow.com/questions/tagged/tensorflow) 提问。**

TensorFlow 项目始终遵循开源软件开发中普遍认可的最佳实践。

## 🩹 补丁(Patching)指南

若需要对特定版本的 TensorFlow 打补丁(例如修复缺陷或安全漏洞),请按以下步骤操作:

*   克隆 TensorFlow 仓库,并切换到目标版本对应的分支——例如 2.8 版本对应 `r2.8` 分支;
*   应用所需的改动(即 cherry-pick),并解决所有代码冲突;
*   运行 TensorFlow 测试,确认全部通过;
*   [从源码构建](https://www.tensorflow.org/install/source) TensorFlow 的 pip 包。

## 🔧 持续构建状态

更多由社区支持的平台与构建配置,请查看 [TensorFlow SIG Build 社区构建列表](https://github.com/tensorflow/build#community-supported-tensorflow-builds)。

### 官方构建

官方持续集成覆盖 **Linux CPU / GPU / XLA**、**macOS**、**Windows CPU / GPU**、**Android**、**Raspberry Pi 0/1/2/3** 等平台。各平台的构建状态徽章与产物(对应 PyPI 上的 tf-nightly 系列夜间包)详见[原 README 的 Official Builds 章节](https://github.com/tensorflow/tensorflow#official-builds)。

## 📚 资源

*   [TensorFlow.org](https://www.tensorflow.org) — 官方站点与文档
*   [TensorFlow Tutorials](https://www.tensorflow.org/tutorials/) — 官方教程
*   [TensorFlow Official Models](https://github.com/tensorflow/models/tree/master/official) — 官方模型库
*   [TensorFlow Examples](https://github.com/tensorflow/examples) — 官方示例代码
*   [TensorFlow Codelabs](https://codelabs.developers.google.com/?cat=TensorFlow) — 动手实践实验
*   [TensorFlow Blog](https://blog.tensorflow.org) — 官方博客
*   [Learn ML with TensorFlow](https://www.tensorflow.org/resources/learn-ml) — 机器学习学习路径
*   [TensorFlow Twitter](https://twitter.com/tensorflow) — 官方 Twitter
*   [TensorFlow YouTube](https://www.youtube.com/channel/UC0rqucBdTuFTjJiefW5t-IQ) — 官方 YouTube 频道
*   [TensorFlow model optimization roadmap](https://www.tensorflow.org/model_optimization/guide/roadmap) — 模型优化路线图
*   [TensorFlow White Papers](https://www.tensorflow.org/about/bib) — 官方白皮书/论文
*   [TensorBoard Visualization Toolkit](https://github.com/tensorflow/tensorboard) — 可视化工具
*   [TensorFlow Code Search](https://cs.opensource.google/tensorflow/tensorflow) — 源码检索

更多关于 [TensorFlow 社区](https://www.tensorflow.org/community)以及[参与贡献](https://www.tensorflow.org/community/contribute)的信息,请访问对应页面。

## 🎓 课程

* [Coursera](https://www.coursera.org/search?query=TensorFlow) 上的 TensorFlow 相关课程
* [Udacity](https://www.udacity.com/courses/all?search=TensorFlow) 上的 TensorFlow 相关课程
* [Edx](https://www.edx.org/search?q=TensorFlow) 上的 TensorFlow 相关课程

## 📄 许可证

TensorFlow 基于 [Apache License 2.0](https://github.com/tensorflow/tensorflow/blob/master/LICENSE) 协议开源。

---

**代部署 / 定制服务 / 技术咨询 请添加微信:uaycar**

---

> 本仓库是 [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) 的中文翻译版本,仅翻译官方 README 用于学习交流,不包含任何源代码;所有代码与原始文档的版权归 TensorFlow 项目作者所有,遵循 Apache License 2.0 原始许可证。
>
> **如果觉得有用,请给原项目点个 Star!** ⭐
