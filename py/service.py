#!/bin/python3

import http.server
import socketserver
import config

class WebHookHandler(http.server.BaseHTTPRequestHandler):
    """
    Simple webhook handler.
    """

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

    def do_POST(self):
        """Serve a POST request.
        Gitlab sends POST request for webhooks.
        """

        if self.headers['X-Gitlab-Token'] != config.GITLAB_SECRET:
            self.send_error(
                    HTTPStatus.NOT_IMPLEMENTED,
                    "Wrong Token")
            return

        if self.headers['X-Gitlab-Event'] == "Push Hook":
            # git after-post hook
            print('post')
            pass
        else:
            self.send_error(
                    HTTPStatus.NOT_IMPLEMENTED,
                    "Can only POST to CGI scripts")


server_address = (config.ADDR, config.PORT)
httpd = http.server.HTTPServer(server_address, WebHookHandler)
print(" Server listening: %s:%s" % (config.ADDR, config.PORT))

httpd.serve_forever()

