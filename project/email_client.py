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

    def initialize(self, user: str, password: str):
        try:
            with IMAP4_SSL(host=self.host, port=self.port) as server:
                server.login(user, password)
                return server
        except Exception as e:
            raise EmailClientError(message="Failed to initialize email client")
