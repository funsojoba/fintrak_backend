from .tasks import send_email_async
from typing import List, Dict

class EmailServices:
    @classmethod
    def send_async(
        cls, template: str, subject: str, recipients: List[str], context: Dict
    ):
        send_email_async.delay(
            template=template, subject=subject, recipients=recipients, context=context
        )
