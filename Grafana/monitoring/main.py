from functools import reduce

from GrafanaClient import GrafanaClient

new_site = GrafanaClient()

contact_points = new_site.find_contact_points()

new_site.generate_ContactPoints_py()

