from collections import defaultdict
from pathlib import Path
import tomllib
from typing import Literal

from jinja2 import Environment, FileSystemLoader
from py_markdown_table.markdown_table import markdown_table
from pydantic import BaseModel, field_validator

env = Environment(loader=FileSystemLoader("templates"), autoescape=True)
template = env.get_template("README.md.jinja")


class GitHubActionsBadgeData(BaseModel):
    badge_type: Literal["github_actions"]
    repo: str
    branch: str = "main"
    workflow: str = "tests"

    _template = "[![tests](https://github.com/{repo}/workflows/{workflow}/badge.svg?branch={branch})](https://github.com/{repo}/actions?query=workflow%3A{workflow}+branch%3A{branch})"

    def render(self):
        return self._template.format(repo=self.repo, branch=self.branch, workflow=self.workflow)


class CondaForgePipelineBadgeData(BaseModel):
    badge_type: Literal["conda_forge_pipeline"]
    package_name: str
    package_id: int

    _template = "[![tests](https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/{package_name}-feedstock?branchName=main)](https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId={package_id}&branchName=main)"

    def render(self):
        return self._template.format(package_name=self.package_name, package_id=self.package_id)


class ProjectData(BaseModel):
    repo: str
    category: str
    badge_data: list[GitHubActionsBadgeData | CondaForgePipelineBadgeData]

    @field_validator("badge_data", mode="before")
    @classmethod
    def inject_repo(cls, v, info):
        for item in v:
            item["repo"] = info.data["repo"]
        return v


REPO_LINK_TEMPLATE = "[{repo}](https://github.com/{repo})"
ISSUES_BADGE_TEMPLATE = "[![GitHub issues](https://img.shields.io/github/issues-raw/{repo}?label=issues%20open)](https://github.com/{repo}/issues)"
PULL_REQUESTS_BADGE_TEMPLATE = "[![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/{repo}?label=pull%20requests%20open)](https://github.com/{repo}/pulls)"


def main():
    with Path("data.toml").open("rb") as fp:
        data = tomllib.load(fp)

    projects = [ProjectData.model_validate(item) for item in data["projects"]]

    table_data = defaultdict(list)
    for project_data in projects:
        row = {
            "Repo": REPO_LINK_TEMPLATE.format(repo=project_data.repo),
            "Builds": "<br>".join(badge.render() for badge in project_data.badge_data),
            "Issues": ISSUES_BADGE_TEMPLATE.format(repo=project_data.repo),
            "PRs": PULL_REQUESTS_BADGE_TEMPLATE.format(repo=project_data.repo),
        }
        table_data[project_data.category].append(row)

    tables = dict()
    for category, rows in table_data.items():
        tables[category] = markdown_table(rows)

    rendered = template.render(tables=tables)

    with Path("README.md").open("w") as fp:
        fp.write(rendered)


if __name__ == "__main__":
    main()
