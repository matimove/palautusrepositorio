from urllib import request
from project import Project
import toml

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = toml.loads(request.urlopen(self._url).read().decode("utf-8"))

        name = content["tool"]["poetry"]["name"]
        desc = content["tool"]["poetry"]["description"]
        license = content["tool"]["poetry"]["license"]

        authors = content["tool"]["poetry"]["authors"]

        deps = content["tool"]["poetry"]["dependencies"]
        dev_deps = content["tool"]["poetry"]["group"]["dev"]["dependencies"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, desc, license, authors, deps, dev_deps)

#{'tool': {'poetry': {'name': 'Ohtutesting app', 'version': '0.0.1', 'description': 'Sovellus joka toimii testisyötteenä ohtun viikon 2 laskareihin', 
#'authors': ['Matti Luukkainen', 'Kalle Ilves'], 'license': 'MIT', 'dependencies': {'python': '^3.10', 'Flask': '^3.0.0', 'editdistance': '^0.6.2'}, 
#'group': {'dev': {'dependencies': {'coverage': '^7.3.2', 'robotframework': '^6.1.1', 'robotframework-seleniumlibrary': '^6.1.3', 'requests': '^2.31.0'}}}}}, 
#'build-system': {'requires': ['poetry-core'], 'build-backend': 'poetry.core.masonry.api'}}
