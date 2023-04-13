import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_metals, get_all_sizes, get_all_styles, get_single_metal, get_single_style, get_single_size, create_order, get_all_orders, get_single_order, delete_order, update_order
from urllib.parse import urlparse

class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    # Replace existing function with this
    def parse_url(self, path):
        url_components = urlparse(path)
        path_params = url_components.path.strip("/").split("/")
        query_params = url_components.query.split("&")
        resource = path_params[0]
        id = None

        try:
            id = int(path_params[1])
        except IndexError:
            pass
        except ValueError:
            pass

        return (resource, id, query_params)

    def do_GET(self):
        """Handles GET requests to the server """
        response = {}
        (resource, id) = self.parse_url(self.path)
        if resource == "metals":
            if id is not None:
                response = get_single_metal(id)
                if response is not None:
                    self._set_headers(200)
                else:
                    self._set_headers(404)
                    response = { "message": "That metal is not currently in stock"}
            else:
                self._set_headers(200)
                response = get_all_metals()
        if resource == "styles":
            if id is not None:
                response = get_single_style(id)
            else:
                response = get_all_styles()
        if resource == "sizes":
            if id is not None:
                response = get_single_size(id)
            else:
                response = get_all_sizes()
        if resource == "types":
            if id is not None:
                response = get_single_type(id)
            else:
                response = get_all_types()
        if resource == "orders":
            if id is not None:
                response = get_single_order(id)
                if response is not None:
                    self._set_headers(200)
                else:
                    self._set_headers(404)
                    response= { "message": "That order was never placed or was cancelled"}
            else:
                self._set_headers(200)
                response = get_all_orders()

        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        '''docstring'''
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)
        new_order = None
        if resource == "orders":
            new_order = create_order(post_body)
            if "metalId" in post_body and "sizeId" in post_body and "styleId" in post_body and "typeId" in post_body:
                self._set_headers(201)
                new_order = new_order(post_body)
            else:
                self._set_headers(400)
                new_order = {"message": f'{"metal required" if "metalId" not in post_body else ""} {"size required" if "sizeId" not in post_body else ""} {"style required" if "styleId" not in post_body else ""} {"type required" if "typeId" not in post_body else ""}'}
        self.wfile.write(json.dumps(new_order).encode())


    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the options headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_DELETE(self):
        '''docstring'''
        self._set_headers(204)
        (resource, id) = self.parse_url(self.path)
        if resource == "orders":
            delete_order(id)
        self.wfile.write("".encode())
    def do_PUT(self):
        '''docstring'''
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)
        if resource == "orders":
            self._set_headers(405)
            response = {"message": "unable to modify order once complete"}
            self.wfile.write(json.dumps(response).encode())
        self.wfile.write("".encode())

def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
