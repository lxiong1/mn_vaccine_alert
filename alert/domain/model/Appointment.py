class Appointment:
    def __init__(
        self, provider=None, url=None, location=None, vaccine_types=None,
    ):
        self.provider = provider
        self.url = url
        self.location = location
        self.vaccine_types = vaccine_types
