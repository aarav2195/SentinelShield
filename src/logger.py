import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/requests.log",
    level=logging.INFO,
    format="%(asctime)s | %(message)s"
)

logger = logging.getLogger(__name__)


def log_request(request_info):
    logger.info(
        f"IP={request_info['ip']} | "
        f"Method={request_info['method']} | "
        f"Path={request_info['path']} | "
        f"URL={request_info['url']} | "
        f"Query={request_info['query_parameters']}"
    )