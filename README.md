
# 有道词典命令行查询工具


## Install

```
$ pip install youdao-dict
```

## Usages


```bash
$ youdao hello
                       _                       _ _      _
 _   _  ___  _   _  __| | __ _  ___         __| (_) ___| |_
| | | |/ _ \| | | |/ _` |/ _` |/ _ \ _____ / _` | |/ __| __|
| |_| | (_) | |_| | (_| | (_| | (_) |_____| (_| | | (__| |_
 \__, |\___/ \__,_|\__,_|\__,_|\___/       \__,_|_|\___|\__|
 |___/

=================================================
hello
=================================================
有道翻译：
int. 喂；哈罗
n. 表示问候， 惊奇或唤起注意时的用语
n. (Hello)人名；(法)埃洛
网络释义：
你好
您好
哈啰
喂
=================================================
$ youdao hello world
$ youdao --shell
```

具体参数:

```
usage: youdao [-h] [--shell] [words [words ...]]

Youdao Dictionary in Command Line

optional arguments:
  -h, --help   show this help message and exit

Interactive Shell:
  --shell, -s

Pass Words as Arguments:
  words
```

## Unit Test

使用下面的代码进行单元测试：

```
python -m unittest discover -s tests
```

## DevLog

* 2020-11-10 19:45:37 +0800: 添加不同后端(say, vlc, pyttsx3)的英文发音功能
* 2020-11-10 16:01:17 +0800: 根据Edit Distance和Probability添加了拼写相似词推荐([参考](http://www.norvig.com/spell-correct.html))
