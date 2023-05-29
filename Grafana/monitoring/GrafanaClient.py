import json
import os

import requests


class GrafanaClient:

    def __init__(self):
        self.grafana_host = "https://grafana-gig.int.kn"
        self.grafana_api_key = os.environ.get("GRAFANA_API_KEY")
        self.grafana_header = {
            'Authorization': f"Bearer {self.grafana_api_key}",
            'Content-Type': 'application/json'
        }
        self.package_dir = "../generated"

    def generated(self):
        self.generate_Folders_py()

    def get(self, url):
        resp = requests.get(f"{self.grafana_host}/{url}", headers=self.grafana_header, verify=True)
        return resp

    def pos(self, url, json_data):
        resp = requests.post(f"{self.grafana_host}/{url}", headers=self.grafana_header, verify=True)
        return resp

    def find_folders(self):
        resp = self.get("api/folders")
        return resp.json()

    def find_contact_points(self):
        resp = self.get("api/v1/provisioning/contact-points")
        return resp.json()

    def generate_ContactPoints_py(self):
        file_path = self.package_dir
        contact_points = self.find_contact_points()

        with open(f"{file_path}/ContactPoints.py", "w") as f:
            f.write("# wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n")
            f.write("# wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n")
            f.write("# wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n")
            f.write("# wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n")
            f.write("# wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n")
            f.write("# wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n")
            f.write("# wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww\n")
            f.write("\n")
            f.write("from Grafana.monitoring.util.ContactPoint import ContactPoint\n")
            f.write("\n")
            f.write("\n")
            f.write("class ContactPoints:\n")
            names = [x['name'] for x in contact_points]
            unique_names = []
            for name in names:
                if name not in unique_names:
                    unique_names.append(name)

            for name in unique_names:
                f.write(f"    {self.convert_to_var_name(name)} = ContactPoint(\"{name}\")\n")

    def generate_Folders_py(self):
        file_path = self.package_dir
        folders = self.find_folders()

        with open(f"{file_path}/generated.py", "w") as f:
            f.write("# auhahauhahuuhhuadhaudhauh\n")
            f.write("# auhahauhahuuhhuadhaudhauh\n")
            f.write("# auhahauhahuuhhuadhaudhauh\n")
            f.write("# auhahauhahuuhhuadhaudhauh\n")
            f.write("# auhahauhahuuhhuadhaudhauh\n")
            f.write("from Grafana.monitoring.util.Folder import Folder\n")
            f.write("\n")
            f.write("\n")
            f.write("class generated:\n")
            f.write("\n")
            f.write("\n")

            for ds in folders:
                f.write(f"    {self.convert_to_var_name(ds['title'])} = Folder(\"{ds['uid']}\", \"{ds['title']}\")\n")

    def convert_to_var_name(self, str):
        return str.upper() \
            .strip() \
            .replace(' ', '_') \
            .replace(')', '') \
            .replace('(', '') \
            .replace('/', '') \
            .replace('-', '_')
