from enum import Enum

ServerName = 'Http Technopark Highload server'
HttpVersion = '1.1'

class ContentTypes(Enum):

    html = 'text/html'
    css = 'text/css'
    js = 'text/javascript'
    txt = 'text/txt'
    plain = 'text/plain'
    jpg = 'image/jpeg'
    jpeg = 'image/jpeg'
    png = 'image/png'
    gif = 'image/gif'
    swf = 'application/x-shockwave-flash'

class ResponseStatus(Enum):

    Ok = '200 Ok'
    NotFound = '404 Not Found'
    NotAllowed = '405 Method Not Allowed'
    Forbidden = '403 Forbidden'

