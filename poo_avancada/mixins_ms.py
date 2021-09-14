# https://www.youtube.com/watch?v=zVFLBfqV-q0&list=PLlrxD0HtieHiXd-nEby-TMCoUNwhbLUnj&index=11

class Loggable:
    def __init__(self):
        self.title = ''

    def log(self):
        print('Log message from ' + self.title)


class Connection:
    def __init__(self):
        self.server = ''

    def connect(self):
        print('Connecting to database on ' + self.server)


# Use the framework
# Inherit from Connection and Loggable
class SqlDatabase(Connection, Loggable):
    def __init__(self):
        super().__init__()
        self.title = 'Sql Connection Demo'
        self.server = 'Some_Server'


def framework(item):
    if isinstance(item, Connection):
        item.connect()
    if isinstance(item, Loggable):
        item.log()


class JustLogging(Loggable):
    def __init__(self):
        self.title = 'Just logging'


if __name__ == '__main__':
    sql_connection = SqlDatabase()
    just_logging = JustLogging()
    framework(just_logging)
