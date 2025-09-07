import os
from loguru import logger
from .email_client import EmailClient

class Attachment_handler:
    def __init__(self, email_client:EmailClient) -> None:
        self.client = email_client

    def parse_attachments(self):
      
        attachment = self.client.download_attachments()
        
