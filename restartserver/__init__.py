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
    server.register_help_message('!!restartserver', server.rtr("restartserver.Help"))
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


def restart(server: CommandSource, context: CommandContext, plg: PluginServerInterface):
    if server.get_permission_level() < config['permission']:
        text = RText(plg.rtr("restartserver.Perm"), color=RColor.red)
        server.reply(text)
    else:
        if context['server_name'] in config['ServerFileAddress']:
            os.system(
                'start cmd /k "cd /d {0} && title {2} && {1} -m mcdreforged"'.format(
                    config['ServerFileAddress'][context['server_name']],
                    config['python'],
                    context['server_name']
                )
            )
            server.reply(RText(plg.rtr("restartserver.success"), color=RColor.green))
            server.reply(RText(plg.rtr("restartserver.SuccessNext"), color=RColor.red))
        else:
            server.reply(RText(plg.rtr("restartserver.Fail"), color=RColor.red))


"""
一些帮助
"""


def sth(server: CommandSource, plg: PluginServerInterface):
    server.reply(plg.rtr("restartserver.HelpMessage_1"))
    server.reply(plg.rtr("restartserver.HelpMessage_2"))


"""
可用服务器列表
"""


@new_thread
def restart_list(server: CommandSource, plg: PluginServerInterface):
    server.reply(RText(plg.rtr("restartserver.ServerList"), color=RColor.green))
    for i in config['ServerFileAddress']:
        server.reply(str(i))
        time.sleep(0.1)
