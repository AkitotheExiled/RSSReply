import logging
import static

class Logger:
    def __init__(self):
        logging.basicConfig()
        self.log = logging.getLogger(__name__)
        self.log.setLevel(logging.INFO)
        self.handler = logging.FileHandler(static.LOGGER_NAME)
        self.handler.setLevel(logging.INFO)

        self.formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        self.handler.setFormatter(self.formatter)
        self.log.addHandler(self.handler)