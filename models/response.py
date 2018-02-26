import datetime


class Response(object):
    def __init__(self, status_code, server_name, http_version,
                 content_type='', content_length=0, content=b''):
        self.status_code = status_code
        self.content_type = content_type
        self.content_length = content_length
        self.content = content
        self.server_name = server_name
        self.http_version = http_version

        self.date = datetime.utcnow()

    def resolve(self):
        return ('HTTP/{http_version} {http_status}\r\n'
                'Server: {server_name}\r\n'
                'Date: {date}\r\n'
                'Connection: Closed\r\n'
                'Content-Length: {content_length}\r\n'
                'Content-Type: {content_type}\r\n\r\n') \
                   .format(http_version = self.http_version,
                           http_status = self.status_code,
                           server_name = self.server_name,
                           date = self.date,
                           content_length = self.content_length,
                           content_type = self.content_type).encode() + self.content

