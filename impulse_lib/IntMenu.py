

class IntMenu:
    def __init__(self, title, opts):
        self.title = title
        self.options = {}
        for opt_num, opt_info in enumerate(opts):
            self.options[opt_num] = opt_info

    def __str__(self):
        ret_str = list()
        ret_str.append(self.title)
        for opt_num, opt_info in self.options.iteritems():
            ret_str.append("{}. {}".format(opt_num, opt_info['text']))
        return "\n".join(ret_str)

    def query_user(self):
        print self
        while True:
            choice = int(raw_input())
            if isinstance(choice, int):
                if choice in self.options.keys():
                    self.options[choice]['action'](*self.options[choice]['args'])
                    break
