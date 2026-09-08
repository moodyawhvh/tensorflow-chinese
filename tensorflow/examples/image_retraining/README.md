> 🌐 本文档由 [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) 翻译,英文原版见原项目。

**注意:此代码已迁移至**
https://github.com/tensorflow/hub/tree/master/examples/image_retraining

retrain.py 是一个示例脚本,展示如何把预训练网络改造用于其他分类问题
(包括配合 TFLite 使用与量化)。

自 TensorFlow 1.7 起,建议使用来自 TensorFlow Hub 的预训练网络,即使用上述位置中的新版示例,详见 TensorFlow 修订后的
[图像再训练教程](https://www.tensorflow.org/hub/tutorials/tf2_image_retraining)。

旧版示例(使用冻结的 GraphDef 而非 TensorFlow Hub 模块)仍可在
TensorFlow 1.7 及更早版本的 release 分支中找到。
