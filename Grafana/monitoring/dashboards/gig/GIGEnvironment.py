from Grafana.monitoring.util import ContactPoint


class GIGEnvironment:

    def __init__(self, contact_point):
        self.contact_point: ContactPoint = contact_point
