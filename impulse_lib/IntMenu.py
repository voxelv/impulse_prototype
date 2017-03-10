

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

    def show(self):
        while True:
            print self
            raw = raw_input()
            if raw.isdigit():
                choice = int(raw)
            else:
                return

            if isinstance(choice, int) and choice in self.options.keys():
                choice = int(choice)
                self.options[choice]['action'](*self.options[choice]['args'])
                break
