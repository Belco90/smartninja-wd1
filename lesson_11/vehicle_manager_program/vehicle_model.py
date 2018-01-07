class Vehicle(object):
    def __init__(self, brand, model, kilometers, service_date):
        self.brand = brand
        self.model = model
        self.kilometers = kilometers  # float
        self.service_date = service_date  # datetime

    def __str__(self):
        return "{} {}".format(self.brand, self.model)

    def get_service_date_formatted(self):
        return self.service_date.strftime('%d/%m/%Y')

    def get_str_data(self):
        return "{} with {} km driven so far. Last service date: {}".format(
            self,
            self.kilometers,
            self.get_service_date_formatted(),
        )

    def get_csv_data(self):
        return ",".join([self.brand, self.model, str(self.kilometers), self.get_service_date_formatted()])

    def add_kilometers(self, km):
        self.kilometers += km

    def update_service_date(self, new_date):
        self.service_date = new_date
