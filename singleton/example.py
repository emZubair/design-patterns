class Logger(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('***** Creating the object ***** ')
            cls._instance = super(Logger, cls).__new__(cls)
            # Put any initialization here.
        return cls._instance

    @staticmethod
    def printer(message):
        print(f"\n Message via logger \n{message}\n")


logger = Logger()
logger.printer("Sunday")

logger = Logger()
logger.printer("Monday")

