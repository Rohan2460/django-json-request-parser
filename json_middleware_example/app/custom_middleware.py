import json


class JsonRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Return values Default: None, Success: dict, Error: Empty dict
        request.json = None
        if request.META["CONTENT_TYPE"] == "application/json":
            if request.method == "POST":
                try:
                    request.json = json.loads(request.body)

                except json.JSONDecodeError as e:
                    request.json = {}
                    print("JSONDecodeError: ", e)

        response = self.get_response(request)
        return response
