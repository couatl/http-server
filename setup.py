"""
Respond to GET with status code in {200,404}
Respond to HEAD with status code in {200,404}
Respond to all other request methods with status code 405
Directory index file name index.html
Respond to requests for /<file>.html with the contents of DOCUMENT_ROOT/<file>.html
Requests for /<directory>/ should be interpreted as requests for DOCUMENT_ROOT/<directory>/index.html

"""

import argparse
import asyncio
import configparser
import os

from server import Server

parser = argparse.ArgumentParser(description='Http server.')
parser.add_argument('-c', '--config', type=str, default='/etc/httpd.conf',
                               help='Configuration file, defaults at /etc/httpd.conf')

if __name__ == '__main__':

    args = parser.parse_args()
    config = configparser.ConfigParser()

    if not os.path.exists(args.config):
        raise Exception('Check your configuration file!')

    config.read(args.config)

    loop = asyncio.get_event_loop()
    server = Server(port = config['DEFAULT']['port'],
                    document_root = config['DEFAULT']['document_root'],
                    cpu_limit = config['DEFAULT']['document_root'],
                    thread_limit = config['DEFAULT']['document_root'])

    server.start()