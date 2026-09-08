> 🌐 本文档由 [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) 翻译,英文原版见原项目。

# 自定义算子示例

以下子目录包含自定义算子(Custom Ops)的示例。

* multiplex_1:入门示例,类似 np.where
* multiplex_2:GPU(和 CPU)示例,类似 np.where
* multiplex_3:分派到特化内核(以及稀疏张量)
* multiplex_4:C++ 向后兼容示例:张量列表
* simple_hash_table:使用基于引用计数的 Resource 维护内部状态
* sleep:基于 AsyncOpKernel 的异步(非阻塞)sleep 算子
