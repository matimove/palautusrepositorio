class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_dependencies(self, dependencies):
        return ", ".join(dependencies) if len(dependencies) > 0 else "-"

    def __str__(self):
        result = (f"Name: {self.name}\n"
            f"Description: {self.description or '-'}\n"
            f"License: {self.license}\n\n"
            f"Authors:"
        )

        for author in self.authors:
            result += f"\n- {author}"

        result += f"\n"

        result += f"\nDependencies:"
        for dependency in self.dependencies.keys():
            result += f"\n - {dependency}"

        result += f"\n"

        result += f"\nDevelopment dependencies:"
        for dev_dependency in self.dev_dependencies.keys():
            result += f"\n - {dev_dependency}"

        return result
