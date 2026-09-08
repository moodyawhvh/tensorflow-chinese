> 🌐 本文档由 [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow) 翻译,英文原版见原项目。

# Release 2.22.0

## TensorFlow

<在此插入关于本版本重点方向及潜在工具链变更的简短说明>

### 破坏性变更(Breaking Changes)

默认不再包含 TensorBoard 依赖。如果你使用 `tf.summary.*` API 或 `tf.keras.callbacks.TensorBoard`,请单独安装 `tensorboard` 包(`pip install tensorboard`),否则 TensorFlow 将抛出 ImportError。

在 `tensorflow/c/experimental/filesystem/filesystem_interface.h` 中,移除了 `TF_TransactionToken` 及相关 API。

### 已知注意事项

* <与本版本相关的注意事项(非破坏性变更)>
* <新增/升级依赖应记录在此>
* <某些平台上已知的支持缺失应记录在此>

### 主要特性与改进

* `tf.lite`
    * Dequantize 算子新增对 QUI4(4 位无符号量化)的支持。
    * Unpack 算子新增对 FP16 和 BF16 的支持。
    * Transpose 和 DynamicUpdateSlice 算子新增对 FP16 的支持。
    * Transpose 现在最高支持 8 维张量。
    * 新增 FLOAT8_E4M3FN 和 FLOAT8_E5M2 数据类型支持。

### Bug 修复及其他变更

* `BatchFunction Operator`
    * 新增 `num_warmup_batch_threads` op 属性,支持为预热请求使用独立线程池。
    * 新增 `per_criticality_batch_timeout_micros` op 属性,支持按关键性级别设置不同的批处理超时。
* `TensorFlow API`
    * 在 `tuple` 子类(如 `tf.io.FixedLenFeature`)的公共 API golden 文件中导出 `__new__`,修复静态类型检查的误报。
* `tf.data`
    * 修复 `tf.data.Dataset.scan` 中 `scan_func` 返回状态的形状未对初始状态做严格校验的问题。
*   `tf.image.adjust_contrast`

    *   为 `AdjustContrastv2` op 注册缺失的 Python 梯度,`tf.image.adjust_contrast`
        现在可以通过 `GradientTape` 求微分。修复
        [#126083](https://github.com/tensorflow/tensorflow/issues/126083)。
*   `tf.nn.softsign`

    *   修复 `tf.nn.softsign` 的二阶梯度。此前由于 `SoftsignGrad`
        反向 op 未注册 Python 梯度,二次求导会因查找错误而失败。

*   `tf.math.reciprocal`

    *   将 `Reciprocal` 和 `Inv` 的 XLA 注册约束到具备设备内核的类型,
        因此 `jit_compile=True` 不再静默接受 eager 执行与自动聚簇都会拒绝的整数输入。修复
        [#126414](https://github.com/tensorflow/tensorflow/issues/126414)。

*   `tf.experimental.numpy`

    *   `tf.experimental.numpy.isclose` 与 `tf.experimental.numpy.allclose`
        现在对整数输入也应用 `rtol` 和 `atol`,与 NumPy 行为一致,而不是做纯相等比较。
        比较仍在整数运算中完成;整数输入与浮点容差(含默认值)组合使用时,除非启用自动类型提升,否则会报错——这使类型提升的开销保持为可选。

*   oneDNN(MKL)卷积与转置内核

    *   `Conv3DBackpropFilterV2` 输入秩不匹配、以及对标量做 `ConjugateTranspose`
        时,现在抛出 `InvalidArgumentError` 而不是直接中止进程。修复
        [#118340](https://github.com/tensorflow/tensorflow/issues/118340) 与
        [#118345](https://github.com/tensorflow/tensorflow/issues/118345)。

*   `tf.image.non_max_suppression`

    *   修复 `jit_compile=True` 下 `boxes` 与 `scores` 为空时段错误。XLA lowering
        现在返回空选择结果,与非 XLA 内核一致。修复
        [#117245](https://github.com/tensorflow/tensorflow/issues/117245)。

* <类似上文,记录其他重要变更 / Bug 修复>
* <若某变更关闭了某个 GitHub issue,应在此记录>
* <注释应按模块分组>

## 感谢我们的贡献者

本版本包含来自 Google 众多成员以及以下贡献者的贡献:

<INSERT>, <NAME>, <HERE>, <USING>, <GITHUB>, <HANDLE>

# Release 2.21.0

## TensorFlow

### 破坏性变更(Breaking Changes)

* 自 TF 2.21 起,移除对 Python 3.9 的支持。
* 自 TF 2.21 起,移除 TensorBoard(TB)依赖。

### 主要特性与改进

* `tf.lite`
    * SQRT 算子新增 int8 与 int16x8 支持。
    * EQUAL 与 NOT_EQUAL 算子新增 int16x8 支持。
    * 新增 int2 类型支持。
    * tfl.cast 新增 int2/int4 支持。
    * tfl.fully_connected 新增 SRQ int2 支持。
    * tfl.slice 新增 int4 支持。
    * 新增 uint4 类型支持。

*  `tf.image`
    * decode_image 新增 JPEG XL 支持。

### Bug 修复及其他变更

* `tf.data`
    * 将 `NoneTensorSpec` 纳入公共 API,从而可以通过
      `isinstance(..., tf.NoneTensorSpec)` 识别 `element_spec` 中的 `None`。

## 感谢我们的贡献者

本版本包含来自 Google 众多成员以及以下贡献者的贡献:

Aaraviitkgp, Abhijeet, Abhinav Gunjal, Abhishek, Adam Paszke, Aditya Gupta, Aditya Jha, Aditya Sharma, Adrian Kuegel, Aiden Grossman, Akarsh, Akhil Goel, Alan Kelly, Aleksa Arsic, Aleksei, Aleksei Nurmukhametov, Alex, Alexander Belyaev, Alexander Grund, Alexander Lyashuk, Alexander Shaposhnikov, Alex Pivovarov, Aliia Khasanova, Alina Sbirlea, Allan Renucci, Amelia Thurdekoos, Amit Sabne, Andrei Ivanov, Andrew Dame, Andrey Portnoy, Anish Nair, Anlun Xu, Antonio Sanchez, anuj chincholikar, Anuj Chincholikar, Aravindh Balaji, aravindhbalaji1985, Arian Arfaian, Armin Felder, Artem Belevich, Ashish Rao, Ashitesh Singh, A. Unique TensorFlower, Bart Chrzaszcz, benediktjohannes, Benjamin Chetioui, Benjamin Kramer, Berkin Ilbeyi, Bhatu, Bhavani Subramanian, Bhupendra Dubey, Bill Varcho, Bixia Zheng, Blake Hechtman, Bodhi Silberling, BruceXinXin, Bryan Massoth, Buddh Prakash, Byungchul Kim, Ce Zheng, Changhui Lin, Chao, Charles Alaras, Chase Riley Roberts, Chenhao Jiang, Chris Ashton, Chris Jones, Chris Kennelly, Christian Sigg, Chuan He, Chunlei Niu, Chun-nien Chan, Chunyu Jin, Clive Verghese, Cong Liu, Corentin Kerisit, Daniel Chen, Daniel Kuts, Daniel Ng, Daniel Sosa, Daniel Suo, Danila Malyutin, David Duneavy, David Majnemer, David Pizzuto, Deepika Rajani, deeptanshusekhri, dependabot[bot], Deqiang Chen, Derek Murray, Dillon Sharlet, Dimitar (Mitko) Asenov, Dimitris Vardoulakis, Dirk Hornung, DottsGit, Dragan Mladjenovic, Eetu Sjöblom, Elen Kalda, Emilio Cota, Emily Fertig, Eugene Zhulenev, Eusebio Durán Montaña, Evan Brown, Ezekiel Calubaquib, Faijul Amin, Felix Wang, Fengwu Yao, Fergus Henderson, Frederic Rechtenstein, Frederik Gossen, Gabriel Gerlero, Gagan Nagaraj, gaikwadrahul8, garry00107, gaurides, George Pawelczak, Georg Stefan Schmid, gns, Goran Flegar, Graham, Grant Jensen, Greg Olechwierowicz, Gregory Pataky, Grzegorz Gawryał, Gunhyun Park, guozhong.zhuang, Haibo Huang, Hana Joo, Hariprasad Ravishankar, Harsha H S, Harshit Monish, Henning Becker, Hittanshu, Hoeseong (Hayden) Kim, Hugo Mano, Hyeontaek Lim, Ibrahim Umit Akgun, ILCSFNO, Ilia Sergachev, Ilya Tikhonovskiy, Iman Hosseini, Ionel Gog, Isha Arkatkar, isharif168, Ivo Ristovski List, Jacques Pienaar, Jae H. Yoo, Jaeyoon Jung, Jake Harmon, James Hilliard, jameslovespancakes, James Spooner, Jane Liu, Jaroslav Sevcik, Jeff Parker, Jeffrey A. Dean, Jeremy Meredith, Jialei Chen, Jian Cai, Jian Li, Jie Luo, Jim Lin, Jing Pu, Jinliang Wei, Jiya Zhang, Joel Wee, Johannes Buchner, Johannes Reifferscheid, Johnny, Jorge Gorbe Moya, Joshua Lang, Joshua Wang, Joss Briody, jparkerh, Juanli Shen, Juhyun Lee, Jun Jiang, Junwhan Ahn, Kadir Barut, Kanglan Tang, Kanish Anand, Kanvi Khanna, Karlo Basioli, Ken Franko, Kevin Chen, Kevin Gleason, Kingston Mandisodza, Koki Ibukuro, Kostiantyn Liepieshov, Krishna Haridasan, Krishna Somani, Krzysztof Kosiński, Kuy Mainwaring, lambert, Larry Lansing, Lin Chai, Lord ε Rebel, Luke Baumann, Luke Hutton, madhavmadupu, Majid Dadashi, Mani Ananth, Manjunath Gaonkar, Marcello Maggioni, Marcin Radomski, Maria Lyubimtseva, Marissa Ikonomidis, Mark Daoust, Mason Chang, Matej Aleksandrov, Mateusz Sokół, Matthias Guenther, Matthias Kramm, Matt Hurd, Matt Kreileder, Maxime France-Pillois, Maxim Ermilov, Mehrdad Khani, Melissa Weber Mendonça, MERT-CKR, Michael Goldfarb, Michael Green, Michael Kuperstein, Michael Voznesensky, Michael Whittaker, Mihai Maruseac, Mikhail Goncharov, Ming-Xu Huang, Mircea Trofin, Misha Gutman, misterBart, mmakevic-amd, Mohamed AbdElmoneim, Mohamed Amine Zghal, Mohammadreza Heydary, Mohammed Anany, mraunak, Mudit Gokhale, Nayana Thorat, Nevi, nhatle, Nhat Le, Nihar0071, Nikhil, Nikita Putikhin, Niklas Vangerow, Nitin Srinivasan, Oleg Shyshkov, Olli Lupton, Om Thakkar, Pankaj Kanwar, Parker Schuh, Paul Ganssle, Pauline Sho, Pavithra Eswaramoorthy, Pedro Gonnet, pemeliya, Penporn Koanantakool, Perry Gibson, Peter Buchlovsky, Peter Gavin, Peter Hawkins, Pham Binh, Phani Paladugula, Philipp Hack, Praneeth Mandala, Praveen Batra, psinfinity, Qingwei Zhang, Quentin Khan, Quoc Truong, QZero, Rachel Han, Raffi Khatchadourian, Ram Rachum, RasheedAli-Shaik, Raviteja Gorijala, Reed Wanderman-Milne, Reilly Grant, Renjie Wu, Richard Levasseur, Robert David, Ryan M. Lefever, Sachin M, Sagun Bajra, Sai Ganesh Muthuraman, Saksham Singh Rathore, Sannidhya Chauhan, Sayan Saha, Sean Talts, Seher Ellis, Sergei Lebedev, Sergey Kozub, Sevin Fide Varoglu, Shahriar Rouf, Shanbin Ke, Shaogang Wang, Sharad Vikram, Shawn Lu, Siddhartha Menon, Siqiao Wu, skill, Smit Hinsu, snadampal, Sohaib Iftikhar, Soowon Jeong, spiao, Srijan Upadhyay, stevemcgregory, Subham Soni, Subhankar Shah, Swachhand Lokhande, Tai Ly, TensorFlower Gardener, Terry Heo, Terry Sun, Terry Tao, Theotime Combes, Thomas Joerg, Thomas Köppe, Tiago Quelhas, TJ Xu, Toli Yevtushenko, Tomás Longeri, Tom Hennigan, Tommy Chiang, Tom Natan, Tongfei Guo, Tori Baker, Uwe L. Korn, Vadym Matsishevskyi, Vamsi Manchala, Venkat6871, Victor Stone, Ville Vesilehto, Vitalii Dziuba, Vladimir Belitskiy, Vlad Sytchenko, Volodymyr Kysenko, Wai Hon Law, wan3x, Weiyi Wang, Will Froom, William S. Moses, wondertx, Xuefei Jiang, Yang Chen, Yash Katariya, Yasir Ashfaq, yasiribmcon, Yeou Chiou, Yicheng Luo, Yi Kong, Yimei Sun, Yin Zhang, Yuchen Yao, Yue Sheng, Yulia Baturina, Yunjie Xu, Yunlong Liu, Yun Peng, Yurii Topin, Zac Cranko, Zac Mustin, Zenong Zhang, Zeyu Wang, Zhanyong Wan, Zixuan Jiang, Ziyin Huang, Zviki Nozadze

# Release 2.20.0

## TensorFlow

### 破坏性变更(Breaking Changes)

* 由于 `tensorflow-io-gcs-filesystem` 包的支持状况不确定且受限,现改为可选依赖。如需与 `tensorflow` 一并安装,请执行 `pip install "tensorflow[gcs-filesystem]"`。

### 主要特性与改进

* `tf.data`
    * 在 `tf.data.Options` 中新增 `autotune.min_parallelism`,以加快输入流水线预热。
* `tf.lite`
    * LiteRT 在 Google IO '25 上[发布了新版本](https://developers.googleblog.com/en/litert-maximum-performance-simplified/),在 TFLite 基础上改进了端侧 ML/AI 应用的 NPU 与 GPU 硬件加速及性能。相关 API 提供 Kotlin 和 C++ 版本。
    * 此外,LiteRT 代码库将与 TensorFlow 仓库解耦,未来的 TensorFlow Python 包中将移除 `tf.lite`。详细信息将在后续版本说明中公布。
    * 如需持续更新请迁移到 LiteRT;新仓库见 https://github.com/google-ai-edge/LiteRT 。更多信息与 NPU EAP 报名请联系团队:[g.co/ai/LiteRT-NPU-EAP](https://g.co/ai/LiteRT-NPU-EAP)。

## 感谢我们的贡献者

本版本包含来自 Google 众多成员以及以下贡献者的贡献:

1ndig0, 372046933, abhinav, afzpatel, Akhil Goel, Alain Carlucci, Aleksei, Alen Huang, Alex, Amrinfathima-Mcw, Aravindh Balaji, Armand Picard, Aseem Athale, Ashiq Imran, Assoap, Chao, Chase Riley Roberts, Chenhao Jiang, chunhsue, c

> 注:篇幅所限仅译核心章节,完整内容见原项目。
