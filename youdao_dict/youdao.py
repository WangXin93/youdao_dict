#!/usr/bin/env python
# -*- coding: utf-8 -*-

from youdao_dict.utils import LOGO, translate


def read_eval_print_loop():
    while True:
        try:
            src = input("youdao> ")
            translate(src)
        except KeyboardInterrupt:  # <Ctrl-C>
            print()
            print("KeyboardInterrupt")
        except EOFError:  # <Ctrl-D>
            print()
            return


def main(*argv):
    import argparse

    parser = argparse.ArgumentParser(description="Youdao Dictionary in Command Line")
    sh_group = parser.add_argument_group("Interactive Shell")
    sh_group.add_argument("--shell", "-s", action="store_true")

    words_group = parser.add_argument_group("Pass Words as Arguments")
    words_group.add_argument("words", nargs="*")

    args = parser.parse_args()

    if args.shell:
        print(LOGO)
        read_eval_print_loop()
    elif args.words:
        print(LOGO)
        translate(" ".join(args.words))
    else:
        parser.print_usage()


if __name__ == "__main__":
    main()
