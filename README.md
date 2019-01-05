
# 有道词典命令行查询工具

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

## Install

```
$ pip install youdao-dict
```
