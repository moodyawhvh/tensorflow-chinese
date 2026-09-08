> 🌐 本文档由 [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) 翻译,英文原版见原项目。

# 贡献指南

## Pull Request 检查清单

在提交 pull request 之前,请确认你已完成以下事项:

-   阅读过[贡献指南](CONTRIBUTING.md)。
-   阅读过[行为准则](CODE_OF_CONDUCT.md)。
-   确认你已签署[贡献者许可协议(CLA)](https://cla.developers.google.com/)。
-   检查你的改动是否符合[贡献通用准则与理念](#general-guidelines-and-philosophy-for-contribution)。
-   改动符合[代码风格](#c-coding-style)要求。
-   运行过[单元测试](#running-unit-tests)。

## 如何成为贡献者并提交你自己的代码

![Screen Shot 2022-08-30 at 7 27 04 PM](https://user-images.githubusercontent.com/42785357/187579207-9924eb32-da31-47bb-99f9-d8bf1aa238ad.png)

### 典型的 Pull Request 流程

**1. 新建 PR**

- 作为贡献者,你在 GitHub 上提交一个新的 PR。
- 我们会检查每一个新进来的 PR,并给它打上若干标签,例如 `size:`、`comp:` 等。在这个阶段,我们会确认 PR 是否有效并满足一定的质量要求。例如:是否已签署 CLA、PR 描述是否充分、(如适用)是否补充了单元测试、是否是一次有实质意义的贡献(也就是说,不是只改一行的表面性 PR)。

**2. 是否有效?**

-   如果 PR 通过了所有质量检查,我们会为它分配一名审阅者。
-   如果 PR 没有达到校验标准,我们会要求你对 PR 做出修改以满足质量要求后再提交回来;在极少数情况下,我们可能会直接拒绝它。

**3. 审阅**

-   对于有效的 PR,审阅者(熟悉相关代码/功能的人)会检查 PR 是否合格,或是否还需要进一步修改。
-   如果一切正常,审阅者会批准该 PR。
-   如果需要修改,我们会请贡献者按照建议进行调整。
-   你完成修改后再次提交审阅。
-   这一循环会反复进行,直到 PR 被批准。
-   注意:友情提醒一下,如果 PR 超过两周一直等待你的回应,我们可能会主动联系你。

**4. 已批准**

-   PR 被批准后,会被打上 `kokoro:force-run` 标签,从而启动 CI/CD 测试。
-   如果这些测试失败,流程就无法继续推进。
-   在这种情况下,我们可能会要求你对 PR 做进一步修改,以便测试通过。
-   测试通过后,我们会通过一个名为 "copybara" 的任务把所有代码合入内部代码库。

**5. 复制到 Google 内部代码库并运行内部 CI**

-   PR 进入 Google 代码库后,我们会确认它与依赖项以及系统其余部分集成良好。
-   极少数情况下,如果这一阶段的测试失败,代码将无法合并。
-   必要时我们会请你做一些修改。有时卡住的可能是我们自己而不一定是你,请在我们修复问题时保持耐心。
-   内部测试通过后,我们会在内部和 GitHub 上同时合并代码。

以图形化的形式看,一个 PR 的完整生命周期如下所示:

![image](https://github.com/tensorflow/tensorflow/assets/52792999/3eea4ca5-daa0-4570-b0b5-2a2b03a724a3)

### 贡献者许可协议

我们非常乐意接受你的补丁!但在接受之前,必须先跨过几道法律门槛。

请填写个人或企业版贡献者许可协议(CLA)之一:

  * 如果你是以个人身份编写原创源代码,并且确定自己拥有相关知识产权,那么你需要签署[个人 CLA](https://code.google.com/legal/individual-cla-v1.0.html)。
  * 如果你所在的公司希望允许你贡献你的工作成果,那么需要签署[企业 CLA](https://code.google.com/legal/corporate-cla-v1.0.html)。

通过上面两个链接访问相应的 CLA,按照说明完成签署并提交。收到后,我们就可以接受你的 pull request 了。

***注意***:只有你及其他已签署 CLA 的人提交的原创源代码才能被合入主仓库。

### 提交代码

如果你对 TensorFlow 有改进,请向我们提交 pull request!如果你刚刚入门,GitHub 上有一份[操作指南](https://help.github.com/articles/using-pull-requests/)。

TensorFlow 团队成员会被指派来审阅你的 pull request。一旦 pull request 获得批准并通过持续集成检查,TensorFlow 团队成员会给你的改动打上 `ready to pull` 标签。这表示我们正在把你的 pull request 提交到内部仓库。改动在内部提交之后,你的 pull request 会在 GitHub 上自动合并。

如果你想参与贡献,可以从阅读 TensorFlow 代码库开始,然后打开
[GitHub "issues" 标签页](https://github.com/tensorflow/tensorflow/issues),从中挑选感兴趣的问题。如果不知道从哪里下手,可以先从较小/较容易的问题做起,也就是[带 "good first issue" 标签的问题](https://github.com/tensorflow/tensorflow/labels/good%20first%20issue),再看看[带 "contributions welcome" 标签的问题](https://github.com/tensorflow/tensorflow/labels/stat%3Acontributions%20welcome)。我们认为这些问题特别适合外部贡献者参与,往往是因为我们近期可能没有精力处理它们。如果你决定着手某个 issue,请留下一条评论,让别人知道你正在处理它。如果你想找人一起做,可以在 issue 的评论串里协调。

### 贡献准则与标准

在提交 pull request 进行
[审阅](https://github.com/tensorflow/tensorflow/pulls)之前,
请确保你的改动符合这些准则并遵循 TensorFlow 编码风格。

#### 贡献的通用准则与理念

*   贡献新功能时应附带单元测试,这既能 a) 证明你的代码工作正常,又能 b) 防范未来破坏性改动,降低维护成本。
*   Bug 修复通常同样需要单元测试,因为 Bug 的存在往往说明测试覆盖不足。
*   修改 TensorFlow 核心代码(例如
    [tensorflow/core](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core)
    和
    [tensorflow/python](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/python)
    中的代码)时,务必牢记 API 兼容性。
    TensorFlow 已经越过 1.0 版本,因此除非发布大版本,否则不能做不向后兼容的 API 变更。PR 审阅者会[按照 API 评审惯例](https://github.com/tensorflow/community/blob/master/governance/api-reviews.md)指出任何 API 兼容性问题。
*   当你向 TensorFlow 贡献一个新功能时,(默认情况下)维护负担会转移到 TensorFlow 团队。这意味着必须把贡献带来的收益与维护该功能的成本放在一起权衡。
*   完整的新功能(例如实现前沿算法的新 op)通常应先放入
    [tensorflow/addons](https://github.com/tensorflow/addons) 接受实际使用检验,再决定是否迁入核心库。
*   由于每个 PR 都需要消耗数个 CPU/GPU 小时的 CI 测试资源,我们不鼓励提交只修一个错别字、一个警告之类的 PR。我们建议至少在文件层面一并修复同类问题(例如:修掉一个文件里的所有错别字、消除一个文件里的全部编译警告等)。
*   测试应遵循[测试最佳实践](https://www.tensorflow.org/community/contribute/tests)指南。

#### 许可证

新文件的顶部必须包含许可证声明。

*   [C/C++ 许可证示例](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/framework/op.cc#L1)
*   [Python 许可证示例](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/python/ops/nn.py#L1)
*   [Java 许可证示例](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/java/src/main/java/org/tensorflow/Graph.java#L1)
*   [Go 许可证示例](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/go/operation.go#L1)
*   [Bash 许可证示例](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/ci_build/ci_build.sh#L2)
*   [JavaScript/TypeScript 许可证示例](https://github.com/tensorflow/tensorboard/blob/master/tensorboard/components/tf_backend/backend.ts#L1)

Bazel 的 BUILD 文件同样需要包含许可证段落,例如
[BUILD 示例](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/core/BUILD#L61)。

#### C++ 编码风格

对 TensorFlow C++ 代码的修改应符合
[Google C++ 风格指南](https://google.github.io/styleguide/cppguide.html)。

使用 `clang-format` 检查你的 C/C++ 改动。在 Ubuntu 上安装 `clang-format`:

```bash
sudo apt-get install -y clang-format
```

然后可以这样检查一个 C/C++ 文件:

```bash
clang-format <my_cc_file> --style=google > /tmp/my_cc_file.cc
diff <my_cc_file> /tmp/my_cc_file.cc
```

#### Python 编码风格

对 TensorFlow Python 代码的修改应符合
[Google Python 风格指南](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)。

使用 `pylint` 检查你的 Python 改动。安装 `pylint` 并基于 TensorFlow 自定义风格定义检查文件:

```bash
pip install pylint
pylint --rcfile=tensorflow/tools/ci_build/pylintrc myfile.py
```

注意 `pylint --rcfile=tensorflow/tools/ci_build/pylintrc` 必须在 tensorflow 顶层目录下运行。

#### 其他语言的编码风格

*   [Google Java 风格指南](https://google.github.io/styleguide/javaguide.html)
*   [Google JavaScript 风格指南](https://google.github.io/styleguide/jsguide.html)
*   [Google Shell 风格指南](https://google.github.io/styleguide/shellguide.html)
*   [Google Objective-C 风格指南](https://google.github.io/styleguide/objcguide.html)

#### 运行完整性检查

如果你的系统上装有 Docker,可以通过以下命令对你的改动做完整性检查:

```bash
tensorflow/tools/ci_build/ci_build.sh CPU tensorflow/tools/ci_build/ci_sanity.sh
```

它能发现你改动中存在的大部分许可证、Python 编码风格和 BUILD 文件问题。

#### 运行单元测试

运行 TensorFlow 单元测试有两种方式。

1.  使用直接安装在你系统上的工具和库。

    所需软件包请参考
    [CPU-only 开发者 Dockerfile](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/dockerfiles/dockerfiles/devel-cpu.Dockerfile)
    和
    [GPU 开发者 Dockerfile](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/tools/dockerfiles/dockerfiles/devel-gpu.Dockerfile)。
    或者直接使用前述
    [tensorflow/build Docker 镜像](https://hub.docker.com/r/tensorflow/build)
    (`tensorflow/tensorflow:devel` 和 `tensorflow/tensorflow:devel-gpu`
    已不再支持开发用途)。在开发中使用 TF SIG Build 的 Dockerfile 可以避免把软件包直接装进系统
    (这种情况下,进入运行中的容器后记得把目录从 `/root` 切换到 `/tensorflow`,
    这样 `bazel` 才能找到 `tensorflow` 工作区)。

    可以用如下命令完成,例如:

    ```bash
    docker run -it --rm -v $PWD:/tmp -w /tmp tensorflow/build:2.15-python3.10
    ```

    装好软件包后,就可以用 bazel 运行指定的单元测试:

    ```bash
    export flags="--config=linux -k"
    ```

    如果要在 GPU 上运行测试:

    *   对 v2.18.0 及以上版本:添加 `cuda` 选项标志。

        ```bash
        export flags="--config

> 注:篇幅所限仅译核心章节,完整内容见原项目。
