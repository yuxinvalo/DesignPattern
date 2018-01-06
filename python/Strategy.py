import abc

''' A web page can be shown in different way according to visitor's id '''
''' like developer, editor, admin, client etc '''

class AbsShow(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def show(self):
        pass

class DeveloperPage(AbsShow):
    def show(self):
        return "show [developer page]"

class AdminPage(AbsShow):
    def show(self):
        return "show [admin page]"

class Visit(object):
    def __init__(self, show_page):
        self.show_page = show_page
    def show(self):
        return self.show_page.show()

v = Visit(show_page = DeveloperPage())
print(v.show())
'''exchange page'''
v.show_page = AdminPage()
print(v.show())
