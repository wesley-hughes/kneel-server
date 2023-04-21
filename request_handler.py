import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
# Metals
from views import (
    get_all_metals, 
    get_single_metal, 
    create_metal, 
    delete_metal, 
    update_metal, 
)
# Styles
from views import (
    get_all_styles, 
    get_single_style, 
    create_style, 
    delete_style, 
    update_style, 
)
# Sizes
from views import (
    get_all_sizes, 
    get_single_size, 
    create_size, 
    delete_size, 
    update_size, 
)
# Orders
from views import (
    get_all_orders, 
    get_single_order, 
    create_order, 
    delete_order, 
    update_order,
)


class HandleRequests(BaseHTTPRequestHandler):
    """Controls the functionality of any GET, PUT, POST, DELETE requests to the server
    """

    def do_GET(self):
        """Handles GET requests to the server """
        self._set_headers(200)
        response = {}
        

        (resource, id, query_params) = self.parse_url(self.path)
        if resource == "metals":
            if id is not None:
                response = get_single_metal(id)
            else:
                response = get_all_metals(query_params)
            
        elif resource == "styles":
            if id is not None:
                response = get_single_style(id)
            else:
                response = get_all_styles(query_params)
    
        elif resource == "sizes":
            if id is not None:
                response = get_single_size(id)
            else:
                response = get_all_sizes(query_params)
            
        elif resource == "orders":
            if id is not None:
                response = get_single_order(id)
            else:
                response = get_all_orders()


        self.wfile.write(json.dumps(response).encode())

    def do_POST(self):
        """Handles POST requests to the server """
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        (resource, id, query_params) = self.parse_url(self.path)
        new_resource = None
        
        if resource == "metals":
            new_resource = create_metal(post_body)
        elif resource == "styles":
            new_resource = create_style(post_body)
        elif resource == "sizes":
            new_resource = create_size(post_body)
        elif resource == "orders":
            new_resource = create_order(post_body)
                
        self.wfile.write(json.dumps(new_resource).encode())

    def do_PUT(self):
        """Handles PUT requests to the server """
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)
        
        (resource, id, query_params) = self.parse_url(self.path)
        
        if resource == "metals":
            update_metal(id, post_body)
        elif resource == "styles":
            update_style(id, post_body)
        elif resource == "sizes":
            update_size(id, post_body)
        elif resource == "orders":
            update_order(id, post_body)
            
        self.wfile.write("".encode())
        
    def do_DELETE(self):
        self._set_headers(204)
        (resource, id, query_params) = self.parse_url(self.path)
        
        if resource == "metals":
            delete_metal(id)
        elif resource == "styles":
            delete_style(id)
        elif resource == "sizes":
            delete_size(id)
        elif resource == "orders":
            delete_order(id)
            
        self.wfile.write("".encode())

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
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers', 'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def parse_url(self, path):
        url_components = urlparse(path)
        path_params = url_components.path.strip("/").split("/")
        query_params = []

        if url_components.query != '':
            query_params = url_components.query.split("&")

        resource = path_params[0]
        id = None

        try:
            id = int(path_params[1])
        except IndexError:
            pass  # No route parameter exists: /animals
        except ValueError:
            pass  # Request had trailing slash: /animals/

        return (resource, id, query_params)

# point of this application.
def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()