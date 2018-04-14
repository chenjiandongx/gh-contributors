import requests


class Contributor:

    def __init__(self, contributor):
        self.contributor = contributor

    @property
    def avatar(self):
        return "![{name}]({url}) |".format(
            name=self.contributor["login"],
            url=self.contributor["avatar_url"]
        )

    @property
    def guy(self):
        return "[{name}]({url}) |".format(
            name=self.contributor["login"],
            url=self.contributor["html_url"],
        )


def save(url):
    req = requests.get(url).json()
    avatars, guys, split = ["| "], ["| "], ["| "]

    for r in req:
        c = Contributor(r)
        avatars.append(c.avatar)
        split.append(":----: |")
        guys.append(c.guy)

    avatars.append("\n")
    split.append("\n")

    res = "".join(avatars + split + guys)
    with open("README.md", mode="w+", encoding="utf8") as f:
        f.write(res)