from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
import json
import api.cars as cars


class RestHandler(BaseHTTPRequestHandler):
    def respond(self, status_code, message=None):
        """
        Sends response back to client
        :param status_code: response HTTP status code
        :param message: optional response message (example: JSON)
        """
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        if message is not None:
            self.wfile.write(bytes(message, "utf8"))

    def is_body_valid(self, _body, _keys):
        """
        Checks if body contains all attributes necessary for a "Car" object.
        :param _body: dictionary object to be checked
        :param _keys: keys required to be in dictionary
        :return: True if body contains all _keys and only those, False otherwise
        """
        # check number of keys
        body_keys = set(_body.keys())
        if len(body_keys) != len(_keys):
            return False

        # check if body keys match required keys
        if len([key for key in _keys if key not in _body]) > 0:
            return False

        return True

    def do_GET(self):
        if self.path == "/cars":
            self.respond(HTTPStatus.OK, cars.get_cars())
            return

        try:
            command, resource = self.path[1:].split("/", 1)
        except ValueError:  # bad syntax
            self.respond(HTTPStatus.BAD_REQUEST)
            return

        if command != "car" or resource == "":  # bad syntax
            self.respond(HTTPStatus.BAD_REQUEST)
            return

        car = cars.get_car(resource)
        if car is None:  # car not found
            self.respond(HTTPStatus.NOT_FOUND)
            return

        self.respond(HTTPStatus.OK, car)

    def do_POST(self):
        if self.path != "/cars":  # bad syntax
            self.respond(HTTPStatus.BAD_REQUEST)
            return

        # get POST body
        content_len = int(self.headers.get("content-length", 0))
        post_body = self.rfile.read(content_len)

        # load post body into a dictionary object
        try:
            body = json.loads(post_body)
        except json.JSONDecodeError:
            self.respond(HTTPStatus.BAD_REQUEST)
            return

        # check validity of body
        required_keys = ("id", "make", "model", "year", "price")
        if self.is_body_valid(body, required_keys) is False:
            self.respond(HTTPStatus.UNPROCESSABLE_ENTITY)
            return

        # check for duplicate ids
        car = cars.get_car(body["id"])
        if car is not None:
            self.respond(HTTPStatus.CONFLICT)
            return

        # all good, add car
        cars.insert(body)
        self.respond(HTTPStatus.ACCEPTED)

    def do_PUT(self):
        try:
            command, resource = self.path[1:].split("/", 1)
        except ValueError:  # bad request syntax
            self.respond(HTTPStatus.BAD_REQUEST)
            return

        if command != "car" or resource == "":  # bad syntax
            self.respond(HTTPStatus.BAD_REQUEST)
            return

        car = cars.get_car(resource)
        if car is None:  # car not found
            self.respond(HTTPStatus.NOT_FOUND)
            return

        # get PUT body
        content_len = int(self.headers.get("content-length", 0))
        post_body = self.rfile.read(content_len)

        # load PUT body into a dictionary object
        try:
            body = json.loads(post_body)
        except json.JSONDecodeError:
            self.respond(HTTPStatus.BAD_REQUEST)
            return

        # check validity of body
        required_keys = ("make", "model", "year", "price")
        if self.is_body_valid(body, required_keys) is False:
            self.respond(HTTPStatus.UNPROCESSABLE_ENTITY)
            return

        # all good, update car
        cars.update(resource, body)
        self.respond(HTTPStatus.ACCEPTED)

    def do_DELETE(self):
        try:
            command, resource = self.path[1:].split("/", 1)
        except ValueError:  # bad request syntax
            self.respond(HTTPStatus.BAD_REQUEST)
            return

        if command != "car" or resource == "":  # bad syntax
            self.respond(HTTPStatus.BAD_REQUEST)
            return

        car = cars.get_car(resource)
        if car is None:  # car not found
            self.respond(HTTPStatus.NOT_FOUND)
            return

        # delete car
        cars.delete(resource)
        self.respond(HTTPStatus.ACCEPTED)


if __name__ == "__main__":
    # Server settings
    ip = "127.0.0.1"
    port = 8081

    # start HTTP server
    server_address = (ip, port)
    httpd = HTTPServer(server_address, RestHandler)
    print("Server running at {}:{}".format(ip, port))
    httpd.serve_forever()

# TODO: update README.md
