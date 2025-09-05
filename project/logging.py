import os
import sys
from loguru import logger
from config.config import Appconfig


class CustomLogger:
    def __init__(self, cfg: Appconfig) -> None:
        self.logger = logger
        self.config = cfg

    def setup_logging(self):
        logs_dir = self.config.logs_dir
        error_logs_dir = os.path.join(logs_dir, "error")
        info_logs_dir = os.path.join(logs_dir, "info")
        success_logs_dir = os.path.join(logs_dir, "success")

        for path in [error_logs_dir, info_logs_dir, success_logs_dir]:
            os.makedirs(path, exist_ok=True)

        self.logger.add(
            sys.stderr,
            format="<green>{time}</green> <level>{message}</level>",
            enqueue=True,
        )
        self.logger.add(f"{error_logs_dir}/error.log", level="ERROR", enqueue=True, rotation="10 MB")
        self.logger.add(f"{info_logs_dir}/info.log", level="INFO", enqueue=True, rotation="10 MB")
        self.logger.add(
            f"{success_logs_dir}/success.log", level="SUCCESS", enqueue=True, rotation="10 MB"
        )
