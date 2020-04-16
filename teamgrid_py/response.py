from .errors import ApiError


class TeamGridPyResponse():
    """Response object
    Returned response object.
    Json response is parsed into response object.
    """

    def __init__(self, response):
        self._response = response
        self.statusCode = response.status_code

        if len(self._response.text) > 0:
            try:
                self.json = self._response.json()

                for attr, value in self.json.items():
                    if value:
                        setattr(self, attr, value)
            except ValueError:
                print('Answer not JSON. Returning Requests response')

    def __len__(self):
        return len(getattr(self, 'data', ''))

    def raise_for_status(self):
        """Raises Exception
        Raises
        ------
        ApiError
        """
        if self._response.status_code == 200:
            pass
        else:
            raise ApiError(
                f"Status Code: {self._response.status_code}, \
                Error: {getattr(self, 'error', 'No Data')}, \
                Message: {getattr(self, 'message', 'No Data')}")

    def __repr__(self):
        return f'<TeamGrid Response [{self._response.status_code}]>'
