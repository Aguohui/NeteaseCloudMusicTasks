from push import *


class Pusher():
    def __init__(self):
        self.datas = {}
        self.separator = '-------------------------'

    def append(self, data):
        config = data['config']
        # 是否开启推送
        if not config['enable']:
            return
        # 是否合并推送
        if not config['merge']:
            exec('%s.push(data["title"], data["msg"], config)'.format(config['module']))
            return

        # 配置相同才会合并推送
        key = None
        exec('key=%s.getKey(data)'.format(config['module']))
        if key is not None:
            if key in self.datas:
                self.datas[key]['msg'] += self.separator
                self.datas[key]['msg'] += data['msg']
            else:
                self.datas[key] = data

    def push(self):
        for data in self.datas.values():
            exec('%s.push(data["title"], data["msg"], data["config"])'.format(data['config']['module']))
