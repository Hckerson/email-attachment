from imaplib import IMAP4_SSL
from typing import Optional


class EmailClientError(Exception):
    def __init__(
        self, message: str, code: Optional[int] = None, username: Optional[str] = None
    ):
        super().__init__(message)
        self.code = code
        self.username = username


class EmailClient:
    def __init__(self, host: str, port: int) -> None:
        self.host = host
        self.port = port
        self.server: Optional[IMAP4_SSL] = None

    def initialize(self, user: str, password: str):
        try:
            self.server = IMAP4_SSL(self.host, self.port)
            self.server.login(user, password)
        except Exception as e:
            raise EmailClientError(message="Failed to initialize email client") from e

    def download_attachments(self):
        if self.server is None:
            raise EmailClientError(message="Email client is not initialized")
        try:
            typ, msg, = self.server.search(None, "INBOX")
            print(typ, msg)
        except:
            pass
