from exceptions import InvalidRequests


class Request:
    def __init__(self, request: str):
        split_request = request.lower().split(' ')
        if len(split_request) != 7:
            raise InvalidRequests

        self.amount = int(split_request[1])
        self.product = split_request[2]
        self.departure = split_request[4]
        self.destination = split_request[6]
