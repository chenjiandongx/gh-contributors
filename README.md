# gh-contributors [![PyPI version](https://badge.fury.io/py/gh-contributors.svg)](https://badge.fury.io/py/gh-contributors) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

Github 项目贡献者 Markdown 文档表格生成工具


### 安装

``` bash
$ pip install gh-contributors
```

### 用法

``` bash
$ gh-c --help
usage: gh-c [-h] [-p PATH] [-c COUNT] [-v] REPO

Generate contributors.md via the command line

positional arguments:
  REPO                  the github repo.(:owner/:repo)

optional arguments:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  the output file path.(default CONTRIBUTORS.md)
  -c COUNT, --count COUNT
                        the columns count in one row.(default 6)
  -v, --version         displays the current version of gh-c
```

### 示例

以 pyecharts 这个项目为例子

``` bash
$ gh-c pyecharts/pyecharts
```

*CONTRIBUTORS.md*

| <img src="https://avatars2.githubusercontent.com/u/19553554?v=4" alt="chenjiandongx" width="100px" height="100px"/> |<img src="https://avatars0.githubusercontent.com/u/4280312?v=4" alt="chfw" width="100px" height="100px"/> |<img src="https://avatars0.githubusercontent.com/u/9875406?v=4" alt="kinegratii" width="100px" height="100px"/> |<img src="https://avatars3.githubusercontent.com/u/1425636?v=4" alt="crispgm" width="100px" height="100px"/> |<img src="https://avatars3.githubusercontent.com/u/5152516?v=4" alt="muxuezi" width="100px" height="100px"/> |<img src="https://avatars1.githubusercontent.com/u/7701324?v=4" alt="landpack" width="100px" height="100px"/> |
| :----: |:----: |:----: |:----: |:----: |:----: |
| [chenjiandongx](https://github.com/chenjiandongx) |[chfw](https://github.com/chfw) |[kinegratii](https://github.com/kinegratii) |[crispgm](https://github.com/crispgm) |[muxuezi](https://github.com/muxuezi) |[landpack](https://github.com/landpack) |

| <img src="https://avatars3.githubusercontent.com/u/15723603?v=4" alt="647-coder" width="100px" height="100px"/> |<img src="https://avatars3.githubusercontent.com/u/3361029?v=4" alt="sd8089730" width="100px" height="100px"/> |<img src="https://avatars2.githubusercontent.com/u/30370926?v=4" alt="MiracleXYZ" width="100px" height="100px"/> |<img src="https://avatars1.githubusercontent.com/u/25895405?v=4" alt="Zeroto521" width="100px" height="100px"/> |<img src="https://avatars1.githubusercontent.com/u/17876968?v=4" alt="mowujilun" width="100px" height="100px"/> |<img src="https://avatars2.githubusercontent.com/u/15907728?v=4" alt="shkey" width="100px" height="100px"/> |
| :----: |:----: |:----: |:----: |:----: |:----: |
| [647-coder](https://github.com/647-coder) |[sd8089730](https://github.com/sd8089730) |[MiracleXYZ](https://github.com/MiracleXYZ) |[Zeroto521](https://github.com/Zeroto521) |[mowujilun](https://github.com/mowujilun) |[shkey](https://github.com/shkey) |

| <img src="https://avatars1.githubusercontent.com/u/30023826?v=4" alt="xbanke" width="100px" height="100px"/> |
| :----: |
| [xbanke](https://github.com/xbanke) |


**指定每行列数**

``` bash
$ gh-c pyecharts/pyecharts -c 7 -p 贡献者列表.md
```

*贡献者列表.md*

| <img src="https://avatars2.githubusercontent.com/u/19553554?v=4" alt="chenjiandongx" width="100px" height="100px"/> |<img src="https://avatars0.githubusercontent.com/u/4280312?v=4" alt="chfw" width="100px" height="100px"/> |<img src="https://avatars0.githubusercontent.com/u/9875406?v=4" alt="kinegratii" width="100px" height="100px"/> |<img src="https://avatars3.githubusercontent.com/u/1425636?v=4" alt="crispgm" width="100px" height="100px"/> |<img src="https://avatars3.githubusercontent.com/u/5152516?v=4" alt="muxuezi" width="100px" height="100px"/> |<img src="https://avatars1.githubusercontent.com/u/7701324?v=4" alt="landpack" width="100px" height="100px"/> |<img src="https://avatars3.githubusercontent.com/u/15723603?v=4" alt="647-coder" width="100px" height="100px"/> |
| :----: |:----: |:----: |:----: |:----: |:----: |:----: |
| [chenjiandongx](https://github.com/chenjiandongx) |[chfw](https://github.com/chfw) |[kinegratii](https://github.com/kinegratii) |[crispgm](https://github.com/crispgm) |[muxuezi](https://github.com/muxuezi) |[landpack](https://github.com/landpack) |[647-coder](https://github.com/647-coder) |

| <img src="https://avatars3.githubusercontent.com/u/3361029?v=4" alt="sd8089730" width="100px" height="100px"/> |<img src="https://avatars2.githubusercontent.com/u/30370926?v=4" alt="MiracleXYZ" width="100px" height="100px"/> |<img src="https://avatars1.githubusercontent.com/u/25895405?v=4" alt="Zeroto521" width="100px" height="100px"/> |<img src="https://avatars1.githubusercontent.com/u/17876968?v=4" alt="mowujilun" width="100px" height="100px"/> |<img src="https://avatars2.githubusercontent.com/u/15907728?v=4" alt="shkey" width="100px" height="100px"/> |<img src="https://avatars1.githubusercontent.com/u/30023826?v=4" alt="xbanke" width="100px" height="100px"/> |
| :----: |:----: |:----: |:----: |:----: |:----: |
| [sd8089730](https://github.com/sd8089730) |[MiracleXYZ](https://github.com/MiracleXYZ) |[Zeroto521](https://github.com/Zeroto521) |[mowujilun](https://github.com/mowujilun) |[shkey](https://github.com/shkey) |[xbanke](https://github.com/xbanke) |



### LICNESE

MIT [@chenjiandongx](https://github.com/chenjiandongx)
