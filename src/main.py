import json
import os

# noinspection PyPackageRequirements
from actions import core
from github import Auth, Github, GithubException

from retard import GitHubContext

version = core.get_version()
print(f"🏳️ Starting Python Test Action - \033[32;1m{version}")


# Debug

print(f"GITHUB_ACTION: {os.environ.get('GITHUB_ACTION')}")
print(f"GITHUB_ACTION_REPOSITORY: {os.environ.get('GITHUB_ACTION_REPOSITORY')}")
print(f"GITHUB_REF: {os.environ.get('GITHUB_REF')}")
print(f"GITHUB_REF_NAME: {os.environ.get('GITHUB_REF_NAME')}")


# Inputs

tag = core.get_input("tag")
print(f"tag: \033[36;1m{tag}")
summary: bool = core.get_bool("summary")
print(f"summary: \033[33;1m{summary}")
token: str = core.get_input("token")
print(f"token: \033[36;1m{token}")
data: dict = core.get_data("data")
print(f"data: \033[35;1m{data}")


event: dict = core.get_event()
print("::group::GitHub Event Data")
print(json.dumps(event, indent=4))
print("::endgroup::")

repository: dict = event.get("repository", {})
full_name: str = repository.get("full_name", "")
print(f"full_name: {full_name}")
# owner: str = full_name.split("/")[0]
# print(f"owner: {owner}")
# repo: str = full_name.split("/")[1]
# print(f"repo: {repo}")

sha: str = os.environ.get("GITHUB_SHA", "")
print(f"sha: {sha}")


# Action


# context = {}
# for ctx in contexts:
#     context[ctx] = os.environ.get(f"GITHUB_{ctx}".upper())

context = GitHubContext()
print(f"context.sha: {context.sha}")
print(f"context.repository: {context.repository}")

print("::group::GitHub Context Data")
print(vars(context))
print("::endgroup::")


g = Github(auth=Auth.Token(token))
r = g.get_repo(f"{full_name}")
print(f"repo.name: {r.name}")
print(f"repo.full_name: {r.full_name}")

try:
    ref = r.get_git_ref(f"tags/{tag}")
    if ref.object.sha != sha:
        print(f"Updating: {tag} -> {ref.object.sha}")
        ref.edit(sha, True)
        result = "Updated"
    else:
        print(f"Unchanged: {tag} -> {ref.object.sha}")
        result = "Unchanged"

except GithubException:
    ref = r.create_git_ref(f"refs/tags/{tag}", sha)
    print(f"Created: {ref.ref} -> {ref.object.sha}")
    result = "Created"

g.close()

print(f"ref.ref: {ref.ref}")
print(f"ref.object.sha: {ref.object.sha}")


# Outputs
# https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    print(f"sha={sha}", file=f)  # type: ignore


# Summary
# https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions#adding-a-job-summary

if summary:
    inputs_table = ["<table><tr><th>Input</th><th>Value</th></tr>"]
    for x in ["tag", "summary"]:
        value = globals()[x]
        inputs_table.append(f"<tr><td>{x}</td><td>{value or '-'}</td></tr>")
    inputs_table.append("</table>")

    with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
        print("### Python Test Action", file=f)  # type: ignore
        print(f"{result}: [{ref.ref}]({r.html_url}/releases/tag/{tag}) ➡️ `{sha}`", file=f)  # type: ignore
        print(f"<details><summary>Inputs</summary>{''.join(inputs_table)}</details>\n", file=f)  # type: ignore
        print(f"[Report an issue or request a feature]({r.html_url}/issues)", file=f)  # type: ignore


print("✅ \u001b[32;1mFinished Success")
