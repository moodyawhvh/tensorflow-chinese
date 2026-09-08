> 🌐 本文档由 [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) 翻译,英文原版见原项目。

# TensorFlow 频谱图示例

本示例展示如何从 .wav 文件加载音频,转换为频谱图(spectrogram),再保存为 PNG 图片。频谱图是声音频率随时间变化的可视化,可以作为神经网络在噪声或语音上做识别的特征。

## 构建

运行以下命令构建:

```bash
bazel build tensorflow/examples/wav_to_spectrogram/...
```

构建完成后会得到一个可执行文件,可以这样运行:

```bash
bazel-bin/tensorflow/examples/wav_to_spectrogram/wav_to_spectrogram
```

它使用 TensorFlow 源码自带的默认测试音频,并把图片以 spectrogram.png 写入当前目录。

## 选项

要处理你自己的音频,需要提供 LIN16 格式的 .wav 文件,并用 `--input_audio` 标志传入路径。

可以用 `--window_size` 和 `--stride` 参数控制频谱图的生成方式,它们分别决定估计频率所用窗口的宽度,以及相邻窗口之间的间隔。

`--output_image` 标志设置图片保存路径。无论扩展名写的是什么,输出始终为 PNG 格式。

如果结果看起来太暗,可以试试 `--brightness` 标志,让输出图片更容易看清。

下面是把这些参数组合使用的示例:

```bash
bazel-bin/tensorflow/examples/wav_to_spectrogram/wav_to_spectrogram \
--input_wav=/tmp/my_audio.wav \
--window=1024 \
--stride=512 \
--output_image=/tmp/my_spectrogram.png
```
