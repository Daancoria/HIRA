import logging

logger = logging.getLogger("app_logger")
logger.setLevel(logging.INFO)
handler = logging.FileHandler("logs/app.log")
formatter = logging.Formatter('[%(asctime)s] %(levelname)s in %(module)s: %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)