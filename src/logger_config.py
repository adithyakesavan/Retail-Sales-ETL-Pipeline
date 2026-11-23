
import logging
from pathlib import Path

# Find project root
BASE_DIR = Path(__file__).resolve().parents[1]

# Create logs directory automatically
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "pipeline.log"


def setup_logger():
    logger = logging.getLogger("retail_pipeline")
    logger.setLevel(logging.INFO)

    # Avoid adding duplicate handlers
    if logger.handlers:
        return logger

    formatter = logging.Formatter(
        "%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    # Save logs to file
    file_handler = logging.FileHandler(
        LOG_FILE, encoding="utf-8"
    )
    file_handler.setFormatter(formatter)

    # Display logs in terminal
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger
