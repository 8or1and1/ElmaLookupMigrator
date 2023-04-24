from elmaConnector import elmaConnector


class LookupMigrator:
    def __init__(self, elma_namespace, elma_code, elma_from_config, elma_to_config):
        self.elma_columns = None
        self.data = None
        self.elma_from = elmaConnector(elma_from_config, elma_namespace, elma_code)
        self.elma_to = elmaConnector(elma_to_config, elma_namespace, elma_code)

    def get_data_from_source(self):
        self.data = self.elma_from.get_data()

    def filter_data(self, field_name, values):
        new_data = []
        for value in values:
            for data_unit in self.data:
                if field_name not in data_unit:
                    raise NameError("Таблица не имеет колонки {}".format(field_name))
                if value in data_unit[field_name]:
                    new_data.append(data_unit)
        self.data = new_data

    def clean_data(self, field_name, value=''):
        new_data = []
        for data_unit in self.data:
            if field_name not in data_unit:
                raise NameError("Таблица не имеет колонки {}".format(field_name))
            data_unit[field_name] = value
            new_data.append(data_unit)
        self.data = new_data

    def put_data_in_destination(self):
        for element in self.data:
            print(element)
            self.elma_to.create_element(element)
