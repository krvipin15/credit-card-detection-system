from loguru import logger
from pathlib import Path
from datetime import datetime

# Create logs directory if it doesn't exist
log_dir_path = Path("logs")
log_dir_path.mkdir(exist_ok=True)

# Define log file path with timestamp
log_file_path = log_dir_path / f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Configure loguru to write to the log file
logger.add(
    log_file_path,
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {name}:{line} - {message}",
    level="INFO",
    rotation="10 MB",    # optional: rotate logs after 10 MB
    retention="7 days",  # optional: keep logs for 7 days
    compression="zip"    # optional: compress old logs
)

if __name__ == "__main__":
    logger.info("Logging has started")
