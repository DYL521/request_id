
import threading



local = threading.local()


REQUEST_ID_HEADER_SETTING = 'LOG_REQUEST_ID_HEADER'

LOG_REQUESTS_SETTING = 'LOG_REQUESTS'
LOG_REQUESTS_NO_SETTING = 'NO_REQUEST_ID'
LOG_USER_ATTRIBUTE_SETTING = 'LOG_USER_ATTRIBUTE'
DEFAULT_NO_REQUEST_ID = "none"
REQUEST_ID_RESPONSE_HEADER_SETTING = 'REQUEST_ID_RESPONSE_HEADER'
OUTGOING_REQUEST_ID_HEADER_SETTING = 'OUTGOING_REQUEST_ID_HEADER'
GENERATE_REQUEST_ID_IF_NOT_IN_HEADER_SETTING = 'GENERATE_REQUEST_ID_IF_NOT_IN_HEADER'