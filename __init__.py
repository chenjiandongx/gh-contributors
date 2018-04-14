import requests


class Contributor:

    def __init__(self, contributor):
        self.contributor = contributor

    @property
    def avatar(self):
        return '<img src="{src}" alt="{alt}" width="{size}px" height="{size}px"/> |'.format(
            alt=self.contributor["login"],
            src=self.contributor["avatar_url"],
            size=100
        )

    @property
    def guy(self):
        return "[{name}]({url}) |".format(
            name=self.contributor["login"],
            url=self.contributor["html_url"],
        )


def get_res(res, avatars, guys, split):
    avatars.append("\n")
    split.append("\n")
    res += "".join(avatars + split + guys) + "\n\n"
    return res


def save(url, cnt=6):

    req = requests.get(url).json()
    avatars, guys, split = ["| "], ["| "], ["| "]
    res = ""

    for index, r in enumerate(req):
        c = Contributor(r)
        avatars.append(c.avatar)
        split.append(":----: |")
        guys.append(c.guy)

        if (index + 1) % cnt == 0:
            res = get_res(res, avatars, guys, split)
            avatars, guys, split = ["| "], ["| "], ["| "]

    res = get_res(res, avatars, guys, split)
    with open("README.md", mode="w+", encoding="utf8") as f:
        f.write(res)

save("https://api.github.com/repos/pyecharts/pyecharts/contributors")
