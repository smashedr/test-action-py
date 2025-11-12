import json
import os

# noinspection PyPackageRequirements
from actions import core, context
from github import Auth, Github, GithubException


version = core.get_version()
core.info(f"🏳️ Starting Python Test Action - \033[32;1m{version}")


# Inputs

tag = core.get_input("tag")
core.info(f"tag: \033[36;1m{tag}")
summary: bool = core.get_bool("summary")
core.info(f"summary: \033[33;1m{summary}")
token: str = core.get_input("token")
core.info(f"token: \033[36;1m{token}")
data: dict = core.get_dict("data")
core.info(f"data: \033[35;1m{data}")


# Debug

event: dict = core.get_event()
core.info("::group::GitHub Event Data")
core.info(json.dumps(event, indent=4))
core.info("::endgroup::")


ctx = {k: v for k, v in vars(context).items() if not k.startswith("__")}
del ctx["os"]
core.info("::group::GitHub Context Data")
core.info(json.dumps(ctx, indent=4))
core.info("::endgroup::")


# repository: dict = event.get("repository", {})
# full_name: str = repository.get("full_name", "")
# core.info(f"full_name: {full_name}")
# owner: str = full_name.split("/")[0]
# core.info(f"owner: {owner}")
# repo: str = full_name.split("/")[1]
# core.info(f"repo: {repo}")


# Action

core.info(f"context.repository: {context.repository}")
core.info(f"context.sha: {context.sha}")

g = Github(auth=Auth.Token(token))
r = g.get_repo(f"{context.repository}")
core.info(f"repo.name: {r.name}")
core.info(f"repo.full_name: {r.full_name}")

try:
    ref = r.get_git_ref(f"tags/{tag}")
    if ref.object.sha != context.sha:
        core.info(f"Updating: {tag} -> {ref.object.sha}")
        ref.edit(context.sha, True)
        result = "Updated"
    else:
        core.info(f"Unchanged: {tag} -> {ref.object.sha}")
        result = "Unchanged"

except GithubException:
    ref = r.create_git_ref(f"refs/tags/{tag}", context.sha)
    core.info(f"Created: {ref.ref} -> {ref.object.sha}")
    result = "Created"

g.close()

core.info(f"ref.ref: {ref.ref}")
core.info(f"ref.object.sha: {ref.object.sha}")


# Outputs
# https://docs.github.com/en/actions/using-workflows/workflow-commands-for-github-actions#setting-an-output-parameter

with open(os.environ["GITHUB_OUTPUT"], "a") as f:
    print(f"sha={context.sha}", file=f)  # type: ignore


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
        print(f"{result}: [{ref.ref}]({r.html_url}/releases/tag/{tag}) ➡️ `{context.sha}`", file=f)  # type: ignore
        print(f"<details><summary>Inputs</summary>{''.join(inputs_table)}</details>\n", file=f)  # type: ignore
        print(f"[Report an issue or request a feature]({r.html_url}/issues)", file=f)  # type: ignore


print("✅ \u001b[32;1mFinished Success")
