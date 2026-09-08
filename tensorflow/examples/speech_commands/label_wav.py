# Copyright 2017 The TensorFlow Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================
# 注:本示例注释已由 tensorflow-chinese 项目汉化,代码逻辑保持原样。

r"""用训练好的音频模型识别 WAVE 文件并输出结果。

脚本会按参数加载模型、标签和 .wav 文件,然后把模型对音频数据的预测结果
打印到控制台。这个脚本很适合对训练好的模型做快速 sanity check,
也是从 Python 调用音频模型的一个示例。

运行示例:

python tensorflow/examples/speech_commands/label_wav.py \
--graph=/tmp/my_frozen_graph.pb \
--labels=/tmp/speech_commands_train/conv_labels.txt \
--wav=/tmp/speech_dataset/left/a5d485dc_nohash_0.wav

"""
import argparse
import sys

import tensorflow as tf


FLAGS = None


def load_graph(filename):
  """从文件反序列化计算图,并将其设为默认图。"""
  with tf.io.gfile.GFile(filename, 'rb') as f:
    graph_def = tf.compat.v1.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')


def load_labels(filename):
  """读取标签文件,每行一个标签。"""
  return [line.rstrip() for line in tf.io.gfile.GFile(filename)]


def run_graph(wav_data, labels, input_layer_name, output_layer_name,
              num_top_predictions):
  """把音频数据喂入计算图并打印预测结果。"""
  with tf.compat.v1.Session() as sess:
    # 将音频数据作为输入喂给计算图。
    #   predictions 是一个二维数组:一维对应输入样本数量,
    #   另一维对应每个类别的预测得分。
    softmax_tensor = sess.graph.get_tensor_by_name(output_layer_name)
    predictions, = sess.run(softmax_tensor, {input_layer_name: wav_data})

    # 按置信度从高到低排序并展示标签
    top_k = predictions.argsort()[-num_top_predictions:][::-1]
    for node_id in top_k:
      human_string = labels[node_id]
      score = predictions[node_id]
      print('%s (score = %.5f)' % (human_string, score))

    return 0


def label_wav(wav, labels, graph, input_name, output_name, how_many_labels):
  """加载模型与标签,执行推理并打印预测结果。"""
  if not wav or not tf.io.gfile.exists(wav):
    raise ValueError('Audio file does not exist at {0}'.format(wav))
  if not labels or not tf.io.gfile.exists(labels):
    raise ValueError('Labels file does not exist at {0}'.format(labels))

  if not graph or not tf.io.gfile.exists(graph):
    raise ValueError('Graph file does not exist at {0}'.format(graph))

  labels_list = load_labels(labels)

  # 加载计算图(存储在默认会话中)
  load_graph(graph)

  with open(wav, 'rb') as wav_file:
    wav_data = wav_file.read()

  run_graph(wav_data, labels_list, input_name, output_name, how_many_labels)


def main(_):
  """脚本入口,把命令行标志转换为函数参数。"""
  label_wav(FLAGS.wav, FLAGS.labels, FLAGS.graph, FLAGS.input_name,
            FLAGS.output_name, FLAGS.how_many_labels)


if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument(
      '--wav', type=str, default='', help='Audio file to be identified.')
  parser.add_argument(
      '--graph', type=str, default='', help='Model to use for identification.')
  parser.add_argument(
      '--labels', type=str, default='', help='Path to file containing labels.')
  parser.add_argument(
      '--input_name',
      type=str,
      default='wav_data:0',
      help='Name of WAVE data input node in model.')
  parser.add_argument(
      '--output_name',
      type=str,
      default='labels_softmax:0',
      help='Name of node outputting a prediction in the model.')
  parser.add_argument(
      '--how_many_labels',
      type=int,
      default=3,
      help='Number of results to show.')

  FLAGS, unparsed = parser.parse_known_args()
  tf.compat.v1.app.run(main=main, argv=[sys.argv[0]] + unparsed)
