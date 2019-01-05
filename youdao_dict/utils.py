#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
from lxml import html
import sys
import time
import urllib

try:
    import vlc
except:
    pass  # `pip install python-vlc` needed

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
    print("=" * 49)

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

    xpath = '//div[@id="tWebTrans"]/div[not(@id)]//div[@class="title"]//span/text()'
    results = tree.xpath(xpath)
    if results:
        print("网络释义：")
        for r in results:
            print(r.strip())

    xpath = '//*[@id="fanyiToggle"]/div/p[2]/text()'
    results = tree.xpath(xpath)
    # Print results for sentence
    if results:
        print("有道机器翻译：")
        for r in results:
            print(r)

    print("=" * 49)

    play_voice(source)


#######################
#     Play Voice      #
#######################
def play_voice(source, type=2):
    """
    Args:
        source: percent-encoded string
        type: 1 for English, 2 for American
    """
    if "vlc" in sys.modules:
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
