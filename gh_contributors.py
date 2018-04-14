#!/usr/bin/env python
# coding=utf-8

import argparse

import requests


__VERSION__ = "0.1.0"


class Contributor:

    def __init__(self, contributor):
        self.contributor = contributor

    @property
    def avatar(self):
        """
        返回`avatar`包装字符串
        """
        return '<img src="{src}" alt="{alt}" width="{size}px" height="{size}px"/> |'.format(
            alt=self.contributor["login"],
            src=self.contributor["avatar_url"],
            size=100,
        )

    @property
    def guy(self):
        """
        返回`guy`包装字符串
        """
        return "[{name}]({url}) |".format(
            name=self.contributor["login"], url=self.contributor["html_url"]
        )


def get_res(res, avatars, guys, split):
    """
    返回存储结果字符串

    :param res: 存储结果
    :param avatars: 头像列表
    :param guys: 贡献者名字列表
    :param split: 分隔符列表
    """
    avatars.append("\n")
    split.append("\n")
    res += "".join(avatars + split + guys) + "\n\n"
    return res


def init_list():
    """
    初始化`avatars`, `split`, `guys`三个列表
    """
    return ["| "], ["| "], ["| "]


def save(url, cnt=6, path=None):
    """
    保存文件到本地

    :param url: github 项目地址
    :param cnt: 一行的列数
    :param path: 保存路径
    """
    req = requests.get(
        "https://api.github.com/repos/{}/contributors".format(url)
    ).json()

    # 检查项目仓库是否存在
    if not isinstance(req, list):
        print("REPO DOES NOT EXIST!")
        return

    avatars, guys, split = init_list()
    res = ""

    for index, r in enumerate(req):
        c = Contributor(r)
        avatars.append(c.avatar)
        split.append(":----: |")
        guys.append(c.guy)

        # 每 cnt 数重新生成一个表格
        if (index + 1) % cnt == 0:
            res = get_res(res, avatars, guys, split)
            avatars, guys, split = init_list()

    # 剩下的贡献者追加为一个新表格
    res = get_res(res, avatars, guys, split)
    with open(path, mode="w+", encoding="utf8") as f:
        f.write(res)


def get_parser():
    """
    解析命令行参数
    """
    parser = argparse.ArgumentParser(
        description="Generate contributors.md via the command line"
    )
    parser.add_argument(
        "repo", metavar="REPO", type=str, help="the github repo.(:owner/:repo)"
    )
    parser.add_argument(
        "-p",
        "--path",
        type=str,
        default="CONTRIBUTORS.md",
        help="the output file path.(default CONTRIBUTORS.md)",
    )
    parser.add_argument(
        "-c",
        "--count",
        type=int,
        default=6,
        help="the columns count in one row.(default 6)",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="store_true",
        help="displays the current version of gh-c",
    )
    return parser


def command_line_runner():
    """
    执行命令行操作
    """
    parser = get_parser()
    args = vars(parser.parse_args())

    if args["version"]:
        print(__VERSION__)
        return

    repo = args["repo"]

    if not repo:
        parser.print_help()
        return

    save(repo, cnt=args["count"], path=args["path"])


if __name__ == "__main__":
    command_line_runner()
