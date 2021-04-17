import logging

class myLogger():
    '''
    facilitates creating and working with loggers
    example:
        logger = myLogger("my_logger")
        logger.add_info_handler("info.log")
        logger.add_warn_handler("warn.log")
    '''

    def __init__(self, name='myLogger'):
        self.name = name

        # creating logger
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        
    def add_info_handler(self, logfilename, formatter_string='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
        
        # create file handler which logs time needed for actions
        fh = logging.FileHandler(logfilename)
        fh.setLevel(logging.INFO)

        # create formatter and add it to the handlers
        formatter = logging.Formatter(formatter_string)
        fh.setFormatter(formatter)

        # add the handlers to the logger
        self.logger.addHandler(fh)

    def add_warn_handler(self, logfilename, formatter_string='%(asctime)s - %(name)s - %(levelname)s - %(message)s'):
        
        raise NotImplementedError
        
        # create file handler which logs time needed for actions
        ch = logging.FileHandler(logfilename)
        ch.setLevel(logging.WARNING)

        # create formatter and add it to the handlers
        formatter = logging.Formatter(formatter_string)
        ch.setFormatter(formatter)

        # add the handlers to the logger
        self.logger.addHandler(ch)