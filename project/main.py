import os
from dotenv import find_dotenv, load_dotenv
from .logging import CustomLogger
from .email_client import EmailClient
from config.config import get_config
from .attachment_handler import Attachment_handler


def main():
    cfg = get_config()
    env_file = find_dotenv()
    load_dotenv(env_file)
    logger = CustomLogger(cfg)
    logger.setup_logging()
    IMAP_HOST = os.environ["IMAP_HOST"]
    IMAP_PORT = int(os.environ["IMAP_PORT"])
    GMAIL_ADDRESS = os.environ["GMAIL_ADDRESS"]
    GMAIL_APP_PASSWORD = os.environ["GMAIL_APP_PASSWORD"]

    email_client = EmailClient(IMAP_HOST, IMAP_PORT)
    email_client.initialize(GMAIL_ADDRESS, GMAIL_APP_PASSWORD)
    try:
        attachement_handler = Attachment_handler(email_client)
        attachement_handler.parse_attachments()
    except:
        pass
        


if __name__ == "__main__":
    main()
