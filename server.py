import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import get_all_metals, get_all_sizes, get_all_styles, get_single_metal, get_single_style, get_single_size, create_order, get_all_orders, get_single_order, delete_order, update_order
from repository import all, retrieve, update, create, delete
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
        self._set_headers(200)
        response = None
        (resource, id, query_params) = self.parse_url(self.path)
        if id is not None:
            response = retrieve(resource.upper(), id, query_params)
        else:
            response = all(resource.upper())
        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        '''docstring'''
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)
        new_order = None
        if resource.upper() == "ORDERS":
            self._set_headers(201)
            new_order = create(resource.upper(), post_body)
            self.wfile.write(json.dumps(new_order).encode())
        else:
            self._set_headers(405)
            response = {"message": "unable to create"}
            self.wfile.write(json.dumps(response).encode())


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
        (resource, id) = self.parse_url(self.path)
        self._set_headers(405)
        response = {"message": "unable to delete"}
        self.wfile.write(json.dumps(response).encode())
    def do_PUT(self):
        '''docstring'''
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id) = self.parse_url(self.path)
        metal_dict = retrieve(resource.upper(), id)
        if resource.upper() == "METALS":
            if metal_dict["metal"] == post_body["metal"]:
                self._set_headers(204)
                update(resource.upper(), post_body, id)
                self.wfile.write("".encode())
            else:
                self._set_headers(405)
                response = {"message": "unable to modify metal name"}
                self.wfile.write(json.dumps(response).encode())    
        else:
            self._set_headers(405)
            response = {"message": "unable to modify"}
            self.wfile.write(json.dumps(response).encode())

def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
