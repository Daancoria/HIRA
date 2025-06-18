import logging
import os
from logging.handlers import SMTPHandler

def setup_logging(app):
    # Only enable logging when not in debug mode (i.e., production)
    if not app.debug:
        mail_host = os.getenv("MAIL_SERVER")
        mail_port = int(os.getenv("MAIL_PORT", 587))
        from_addr = os.getenv("MAIL_FROM")
        to_addrs = os.getenv("MAIL_TO", "").split(",")
        username = os.getenv("MAIL_USERNAME")
        password = os.getenv("MAIL_PASSWORD")

        # Only configure email handler if all necessary settings are provided
        if mail_host and from_addr and to_addrs and username and password:
            mail_handler = SMTPHandler(
                mailhost=(mail_host, mail_port),
                fromaddr=from_addr,
                toaddrs=to_addrs,
                subject='[HIRA] Critical System Failure',
                credentials=(username, password),
                secure=()
            )
            mail_handler.setLevel(logging.CRITICAL)  # Only email on CRITICAL issues
            app.logger.addHandler(mail_handler)
