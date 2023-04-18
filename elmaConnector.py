import requests


class elmaConnector:
    def __init__(self, config, namespace, code):
        address = config['address']
        token = config['token']
        self.address = '{}/pub/v1/app/{}/{}/'.format(address, namespace, code)
        self.headers = {"Authorization": "Bearer {}".format(token)}
        self.column_names = self.get_column_names()

    def api_request(self, method, payload=None):
        if payload is None:
            payload = {}
        url = self.address + method
        response = requests.post(url, json=payload, headers=self.headers, verify=False)
        return response

    def get_column_names(self):
        payload = {"size": 1, "active": True}
        response = self.api_request('list', payload)
        column_names = [x for x in response.json()["result"]["result"][0].keys()]
        return column_names

    def get_data(self):
        payload = {"size": 100, "active": True}
        response = self.api_request('list', payload)
        #column_names = [x for x in response.json()["result"]["result"][0].keys()]
        data = [x for x in response.json()["result"]["result"]]
        return data  # pd.DataFrame.from_dict(data, orient='columns')

    def create_element(self, fields):
        # pass
        payload = {'Context':fields}
        response = self.api_request('create', payload)
