import logging
import sys
from pathlib import Path
from logging.handlers import RotatingFileHandler

from ingestion.context import RUN_ID


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "application.log"


class RunIdFormatter(logging.Formatter):

    def format(self, record):

        if not hasattr(record, "run_id"):
            record.run_id = RUN_ID

        return super().format(record)


def configure_logging():

    formatter = RunIdFormatter(
        "%(asctime)s | %(levelname)s | run_id=%(run_id)s | %(name)s | %(message)s"
    )

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)

    root_logger.handlers.clear()

    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=10_000_000,
        backupCount=5
    )
    file_handler.setFormatter(formatter)

    root_logger.addHandler(console_handler)
    root_logger.addHandler(file_handler)