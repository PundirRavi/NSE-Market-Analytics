from src.jobs.job_interface import JobInterface
from src.utils.logger import get_logger


class BaseJob(JobInterface):

    def __init__(self) -> None:
        self.logger = get_logger(self.__class__.__name__)