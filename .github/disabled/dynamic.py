import os

contexts = [
    "action",
    "action_ref",
    "action_repository",
    "actions",
    "actor",
    "actor_id",
    "api_url",
    "base_ref",
    "env",
    "event_name",
    "event_path",
    "graphql_url",
    "head_ref",
    "job",
    "output",
    "path",
    "ref",
    "ref_name",
    "ref_protected",
    "ref_type",
    "repository",
    "repository_id",
    "repository_owner",
    "repository_owner_id",
    "retention_days",
    "run_attempt",
    "run_id",
    "run_number",
    "server_url",
    "sha",
    "step_summary",
    "triggering_actor",
    "workflow",
    "workflow_ref",
    "workflow_sha",
    "workspace",
]


class GitHubContext:
    def __init__(self):
        for ctx in contexts:
            setattr(self, ctx, os.environ.get(f"GITHUB_{ctx}".upper()))
