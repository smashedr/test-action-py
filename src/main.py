import json

# noinspection PyPackageRequirements
from actions import context, core

# noinspection PyPackageRequirements
from github import GithubException

import functions


version: str = core.get_version()
core.info(f"🏳️ Starting Python Test Action - \033[32;1m{version}")


# Inputs

tag: str = core.get_input("tag", True)
core.info(f"tag: \033[36;1m{tag}")
data: dict = core.get_dict("data")
core.info(f"data: \033[35;1m{data}")
summary: bool = core.get_bool("summary")
core.info(f"summary: \033[33;1m{summary}")
token: str = core.get_input("token", True)
core.info(f"token: \033[36;1m{token}")


# Debug


with core.group("which python"):
    core.info(functions.check_output(["which", "python"]))
with core.group("which uv"):
    core.info(functions.check_output(["which", "uv"]))


event: dict = core.get_event()
with core.group("GitHub Event Data"):
    core.info(json.dumps(event, indent=4))


ctx = {k: v for k, v in vars(context).items() if not k.startswith("__")}
del ctx["os"]
with core.group("GitHub Context Data"):
    core.info(json.dumps(ctx, indent=4))


core.start_indent()
repository: dict = event.get("repository", {})
html_url: str = repository.get("html_url", "")
core.info(f"repository.html_url: {html_url}")
full_name: str = repository.get("full_name", "")
core.info(f"repository.full_name: {full_name}")

core.start_indent(4)
core.info(f"context.repository_owner: {context.repository_owner}")
core.info(f"context.repository_name: {context.repository_name}")

core.info(f"context.repository: {context.repository}")
core.info(f"context.sha: {context.sha}")
core.end_indent()


# Action
# https://github.com/PyGithub/PyGithub

# g = Github(auth=Auth.Token(token))
g = core.get_github(token)
repo = g.get_repo(f"{context.repository}")
core.info(f"repo.name: {repo.name}")
core.info(f"repo.full_name: {repo.full_name}")

try:
    ref = repo.get_git_ref(f"tags/{tag}")
    if ref.object.sha != context.sha:
        core.info(f"Updating: {tag} -> {ref.object.sha}")
        ref.edit(context.sha, True)
        result = "Updated"
    else:
        core.info(f"Unchanged: {tag} -> {ref.object.sha}")
        result = "Unchanged"

except GithubException:
    ref = repo.create_git_ref(f"refs/tags/{tag}", context.sha)
    core.info(f"Created: {ref.ref} -> {ref.object.sha}")
    result = "Created"

g.close()

core.info(f"ref.ref: {ref.ref}")
core.info(f"ref.object.sha: {ref.object.sha}")


# Outputs
# https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter

core.set_output("sha", ref.object.sha)


# Summary
# https://docs.github.com/en/actions/writing-workflows/choosing-what-your-workflow-does/workflow-commands-for-github-actions#adding-a-job-summary

if summary:
    inputs_table = ["<table><tr><th>Input</th><th>Value</th></tr>"]
    for x in ["tag", "summary"]:
        value = globals()[x]
        inputs_table.append(f"<tr><td>{x}</td><td>{value or '-'}</td></tr>")
    inputs_table.append("</table>")

    core.summary("### Python Test Action")
    core.summary(f"{result}: [{ref.ref}]({html_url}/releases/tag/{tag}) ➡️ `{context.sha}`")
    core.summary(f"<details><summary>Inputs</summary>{''.join(inputs_table)}</details>\n")
    core.summary(f"[Report an issue or request a feature]({html_url}/issues)")


print("✅ \u001b[32;1mFinished Success")
