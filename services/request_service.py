import requests

class RequestService:
    def __init__(self, URL):
        """
            This class first creates a session object and then makes an HTTP request to an url that was passed as an argument.
            In case of failure, the error is raised.
        """
        try:
            self.session = requests.Session()
            self.res = self.session.get(URL)
            self.res.raise_for_status()
        except Exception as err:
            raise err

    def get_json_request(self, api_endpoint):
        """
            This method makes an HTTP GET request to an API endpoint that is sent as an argument.
            It returns a JSON with the response.
            In case of failure, an error is raised.
        """
        try:
            res = self.session.get(api_endpoint)
            res.raise_for_status()
            data = res.json()
            
            if not 'RECOMMENDED' in api_endpoint:
                return data["result"]["results"]
            return data["results"]

        except Exception as err:
            raise err

