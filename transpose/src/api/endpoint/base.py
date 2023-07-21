import urllib.parse


class Endpoint:
    def __init__(self, base_class) -> None:
        self.super = base_class

    # Performs the given custom endpoint query
    # https://docs.transpose.io/custom-endpoints/integrate/
    def query(self, endpoint: str, parameters: dict = {}) -> dict:
        # save json preference
        temp = self.super.json
        self.super.json = True

        # normalize the endpoint
        endpoint = (
            endpoint.replace("https://api.transpose.io/endpoint/", "")
            .replace("https://api.transpose.io/", "")
            .split("?")[0]
        )

        # remove the / if it ends the string
        endpoint = endpoint[:-1] if endpoint.endswith("/") else endpoint

        # convert parameters to URI
        uri_params = urllib.parse.urlencode(parameters)

        # build final endpoint
        endpoint = "https://api.transpose.io/endpoint/{}{}{}".format(
            endpoint, "?" if len(parameters) >= 1 else "", uri_params
        )

        # make request
        response = self.super.perform_authorized_request(None, endpoint)

        # update pref
        self.super.json = temp

        return response
