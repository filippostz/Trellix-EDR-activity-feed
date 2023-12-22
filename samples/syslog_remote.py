from mvision_edr_activity_feed import subscribe
from logging.handlers import SysLogHandler
import logging
import json


def logserverSetup():
    try:
        logger = logging.getLogger()
        handler = SysLogHandler(address=('server', port))#change server and port accordingly
        handler.setLevel(logging.WARNING)
        logger.addHandler(handler)
    except Exception as e:
        logging.error("***Error while setting up the SysLogHandler")


@subscribe(entity='threat')
def send_threat(event):
    logserverSetup()
    logging.warning(json.dumps(event))