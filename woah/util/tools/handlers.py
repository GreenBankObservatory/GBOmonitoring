# General imports
import logging
import sys
from datetime import datetime
import tqdm


class TqdmLoggingHandler(logging.Handler):
    def __init__(self, level=logging.NOTSET):
        super(self.__class__, self).__init__(level)

    def emit(self, record):
        try:
            msg = self.format(record)
            tqdm.tqdm.write(msg, file=sys.stderr)
            # self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception:
            self.handleError(record)


class QueryLoggingHandler(logging.Handler):
    def __init__(self, level=logging.NOTSET):
        super(self.__class__, self).__init__(level)

    def emit(self, record):
        try:
            msg = self.format(record)
            tqdm.tqdm.write(msg, file=sys.stderr)
            # self.flush()
        except (KeyboardInterrupt, SystemExit):
            raise
        except Exception:
            self.handleError(record)


# Modified from: https://stackoverflow.com/a/33492520/1883424
class DatestampFileHandler(logging.FileHandler):
    # Pass the file name and header string to the constructor.
    def __init__(self, filename, header=None, mode="a", encoding=None, delay=0):
        if not filename:
            raise ValueError("Must provide a filename!")

        # We want our filename to have a timestamp, so:
        parts = filename.split(".")
        # Insert the timestamp just before the extension
        parts.insert(-1, datetime.now().strftime("%Y-%m-%d_%H:%M:%S"))
        filename = ".".join(parts)

        # Call the parent __init__
        super(DatestampFileHandler, self).__init__(filename, mode, encoding, delay)