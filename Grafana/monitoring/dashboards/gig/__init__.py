from Grafana.monitoring.dashboards.gig.GIGEnvironment import GIGEnvironment
from Grafana.generated import ContactPoints

environments = [
    GIGEnvironment(
        contact_point=ContactPoints.ContactPoints.GIG_INFRASTRUCTURE_ALERTS,
    )
]