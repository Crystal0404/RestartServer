from mcdreforged.api.all import *
import os
import time

config = {
    'permission': 2,
    'ServerFileAddress': {},
    'python': 'python'
}
default_config = config.copy()

"""
在插件加载时注册!!help
读写配置文件
注册相关指令以及节点
"""


def on_load(server: PluginServerInterface, prev_module):
    global config
    server.register_help_message('!!restartserver', '重启指定服务器')
    config = server.load_config_simple('restartserver.json', default_config=default_config)
    command = SimpleCommandBuilder()
    command.command('!!restartserver', sth)
    command.command('!!restartserver <server_name>', restart)
    command.command('!!restartserver list', restart_list)
    command.arg('server_name', Text)
    command.register(server)


"""
重启相关逻辑
"""


def restart(server: CommandSource, context: CommandContext):
    if server.get_permission_level() < config['permission']:
        text = RText('权限不足', color=RColor.red)
        server.reply(text)
    else:
        if context['server_name'] in config['ServerFileAddress']:
            os.system(
                'start cmd /k "cd /{0} {1} && title {3} && {2} -m mcdreforged"'.format(
                    config['ServerFileAddress'][context['server_name']][0],
                    config['ServerFileAddress'][context['server_name']],
                    config['python'],
                    context['server_name']
                )
            )
            server.reply(RText('执行成功', color=RColor.green))
            server.reply(RText('如果没有成功启动,可能出现未知问题,及时联系物理服主,不要多次使用本插件启动', color=RColor.red))
        else:
            server.reply(RText('找不到指定服务器', color=RColor.red))


"""
一些帮助
"""


def sth(server: CommandSource):
    server.reply('输入!!restartserver <服务器名字> 重启指定服务器\n输入!!restartserver list 查看可用服务器列表')


"""
可用服务器列表
"""


@new_thread
def restart_list(server: CommandSource):
    server.reply(RText('有以下可用服务器:', color=RColor.green))
    for i in config['ServerFileAddress']:
        server.reply(str(i))
        time.sleep(0.1)
