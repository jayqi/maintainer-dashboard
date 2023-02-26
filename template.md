# Markdown Table Template

Template rows to copy and paste into the table.
- Regular project: find-and-replace `reponame`
- conda-forge feedstock: find-and-replace `packagename` and `packageid`

```
| Repo | Build | Issues | PRs |
|---|:---:|:---:|:---:|
| [username/reponame](https://github.com/username/reponame) | [![tests](https://github.com/username/reponame/workflows/tests/badge.svg?branch=main)](https://github.com/username/reponame/actions?query=workflow%3Atests+branch%3Amain) | [![GitHub issues](https://img.shields.io/github/issues-raw/username/reponame?color=3fb950&label=issues%20open)](https://github.com/username/reponame/issues) | [![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/username/reponame?color=3fb950&label=pull%20requests%20open)](https://github.com/username/reponame/pulls) |
| [conda-forge/packagename-feedstock](https://github.com/conda-forge/packagename-feedstock) | [![tests](https://dev.azure.com/conda-forge/feedstock-builds/_apis/build/status/packagename-feedstock?branchName=main)](https://dev.azure.com/conda-forge/feedstock-builds/_build/latest?definitionId=packageid&branchName=main) | [![GitHub issues](https://img.shields.io/github/issues-raw/conda-forge/packagename-feedstock?color=3fb950&label=issues%20open)](https://github.com/conda-forge/packagename-feedstock/issues) | [![GitHub pull requests](https://img.shields.io/github/issues-pr-raw/conda-forge/packagename-feedstock?color=3fb950&label=pull%20requests%20open)](https://github.com/conda-forge/packagename-feedstock/pulls) |
```
