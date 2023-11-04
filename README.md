## 这是什么
这是一个mcdreforged插件,可以让你在一个服务器中启动另一个服务器,避免因为一些
原因导致的服务器崩溃无法重启
## 如何使用
将本插件放入mcdreforged插件文件夹中，生成配置文件后对配置文件修改并重载就
可以使用了
## 配置文件
```json
{
    "permission": 2,
    "ServerFileAddress": {},
    "python": "python"
}
```
这是默认生成的配置文件

permission是权限等级

ServerFileAddress是所要重启的服务器名称以及它的绝对位置

python是你的解释器绝对位置,如果你的mcdreforged没有改动解释器位置，一般不需要更改

下面是一个正确编写配置文件的示例

```json
{
    "permission": 2,
    "ServerFileAddress": {
      "survival": "D:\\Python\\mcdr",
      "creative": "D:\\Python\\mcdr1"
    },
    "python": "D:\\Python\\mcdr\\venv\\Scripts\\python.exe"
}
```
注意分割符是"\\"而不是"\"

剩下的帮助可以使用指令!!restartserver查看
