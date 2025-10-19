import logging
import datetime
import os

def init_logger() -> None:
    """Initialize timestamped file logger in artifacts/YYYY-MM-DD/."""
    day = datetime.date.today().isoformat()
    os.makedirs(f"artifacts/{day}", exist_ok=True)
    logfile = f"artifacts/{day}/run.log"
    logging.basicConfig(
        filename=logfile,
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
    )
    logging.getLogger().addHandler(logging.StreamHandler())
    logging.info("Logger initialized")