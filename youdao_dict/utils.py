#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import platform
import re
import sys
import time
import urllib

import requests
from lxml import html

from . import spellcheck

try:
    import vlc
except ImportError:
    pass
except OSError:
    pass  # `pip install python-vlc` needed

try:
    import pyttsx3
except ImportError:
    pass

LOGO = """
                       _                       _ _      _
 _   _  ___  _   _  __| | __ _  ___         __| (_) ___| |_
| | | |/ _ \| | | |/ _` |/ _` |/ _ \ _____ / _` | |/ __| __|
| |_| | (_) | |_| | (_| | (_| | (_) |_____| (_| | | (__| |_
 \__, |\___/ \__,_|\__,_|\__,_|\___/       \__,_|_|\___|\__|
 |___/
"""


def translate(source):
    print("=" * 49)
    print(source)
    print()

    #######################
    #     Parse Text      #
    #######################
    source = urllib.parse.quote(source)
    url = "https://www.youdao.com/w/{}/#keyfrom=dict2.top".format(source)
    page = requests.get(url)
    tree = html.fromstring(page.content)

    xpath = '//*[@id="phrsListTab"]//div[@class="trans-container"]/ul/li/text()'
    results = tree.xpath(xpath)
    # Print results for word
    if results:
        print("有道翻译：")
        for r in results:
            print(r)
        print()

    xpath = '//div[@id="tWebTrans"]/div[not(@id)]//div[@class="title"]//span/text()'
    results = tree.xpath(xpath)
    if results:
        print("网络释义：")
        for r in results:
            print(r.strip())
        print()

    xpath = '//*[@id="fanyiToggle"]/div/p[2]/text()'
    results = tree.xpath(xpath)
    # Print results for sentence
    if results:
        print("有道机器翻译：")
        for r in results:
            print(r)
        print()

    if len(re.findall(r'\w+', source)) == 1:
        print("拼写相似单词：")
        corrs = spellcheck.spell.n_correction(source)
        print(", ".join(corrs))

    print("=" * 49)
    play_voice(source)


#######################
#     Play Voice      #
#######################
def play_voice(source, type=2, backend="say"):
    """
    Args:
        source: percent-encoded string
        type: 1 for English, 2 for American
        backend: vlc, say, pyttsx3
    """
    if platform.system() == "Darwin" and backend == "say": #
        os.system("say {}".format(source))
    elif "pyttsx3" in sys.modules and backend == "pyttsx3":
        import pyttsx3
        engine = pyttsx3.init()
        engine.say(source)
        engine.runAndWait()
    elif "vlc" in sys.modules and backend == "vlc":
        voice_url = "http://dict.youdao.com/dictvoice?audio={}&type={}"
        voice = vlc.MediaPlayer(voice_url.format(source, type))
        voice.play()
        # Play for a while then exit main program
        # https://stackoverflow.com/questions/49141463/how-to-wait-until-a-sound-file-ends-in-vlc-in-python-3-6
        time.sleep(0.6)
        duration = max(voice.get_length() / 1000 - 0.6, 0)
        time.sleep(duration)


if __name__ == "__main__":
    #######################
    #     Print Logo      #
    #######################
    print(LOGO)

    source = sys.argv[1:]

    if len(source) == 1:
        translate(source[0])
    elif len(source) > 1:
        translate(" ".join(source))
