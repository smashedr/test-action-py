import os


class GitHubContext:
    action: str | None
    action_ref: str | None
    action_repository: str | None
    actions: str | None
    actor: str | None
    actor_id: str | None
    api_url: str | None
    base_ref: str | None
    env: str | None
    event_name: str | None
    event_path: str | None
    graphql_url: str | None
    head_ref: str | None
    job: str | None
    output: str | None
    path: str | None
    ref: str | None
    ref_name: str | None
    ref_protected: str | None
    ref_type: str | None
    repository: str | None
    repository_id: str | None
    repository_owner: str | None
    repository_owner_id: str | None
    retention_days: str | None
    run_attempt: str | None
    run_id: str | None
    run_number: str | None
    server_url: str | None
    sha: str | None
    step_summary: str | None
    triggering_actor: str | None
    workflow: str | None
    workflow_ref: str | None
    workflow_sha: str | None
    workspace: str | None

    def __init__(self):
        self.action = os.environ.get("GITHUB_ACTION")
        self.action_ref = os.environ.get("GITHUB_ACTION_REF")
        self.action_repository = os.environ.get("GITHUB_ACTION_REPOSITORY")
        self.actions = os.environ.get("GITHUB_ACTIONS")
        self.actor = os.environ.get("GITHUB_ACTOR")
        self.actor_id = os.environ.get("GITHUB_ACTOR_ID")
        self.api_url = os.environ.get("GITHUB_API_URL")
        self.base_ref = os.environ.get("GITHUB_BASE_REF")
        self.env = os.environ.get("GITHUB_ENV")
        self.event_name = os.environ.get("GITHUB_EVENT_NAME")
        self.event_path = os.environ.get("GITHUB_EVENT_PATH")
        self.graphql_url = os.environ.get("GITHUB_GRAPHQL_URL")
        self.head_ref = os.environ.get("GITHUB_HEAD_REF")
        self.job = os.environ.get("GITHUB_JOB")
        self.output = os.environ.get("GITHUB_OUTPUT")
        self.path = os.environ.get("GITHUB_PATH")
        self.ref = os.environ.get("GITHUB_REF")
        self.ref_name = os.environ.get("GITHUB_REF_NAME")
        self.ref_protected = os.environ.get("GITHUB_REF_PROTECTED")
        self.ref_type = os.environ.get("GITHUB_REF_TYPE")
        self.repository = os.environ.get("GITHUB_REPOSITORY")
        self.repository_id = os.environ.get("GITHUB_REPOSITORY_ID")
        self.repository_owner = os.environ.get("GITHUB_REPOSITORY_OWNER")
        self.repository_owner_id = os.environ.get("GITHUB_REPOSITORY_OWNER_ID")
        self.retention_days = os.environ.get("GITHUB_RETENTION_DAYS")
        self.run_attempt = os.environ.get("GITHUB_RUN_ATTEMPT")
        self.run_id = os.environ.get("GITHUB_RUN_ID")
        self.run_number = os.environ.get("GITHUB_RUN_NUMBER")
        self.server_url = os.environ.get("GITHUB_SERVER_URL")
        self.sha = os.environ.get("GITHUB_SHA")
        self.step_summary = os.environ.get("GITHUB_STEP_SUMMARY")
        self.triggering_actor = os.environ.get("GITHUB_TRIGGERING_ACTOR")
        self.workflow = os.environ.get("GITHUB_WORKFLOW")
        self.workflow_ref = os.environ.get("GITHUB_WORKFLOW_REF")
        self.workflow_sha = os.environ.get("GITHUB_WORKFLOW_SHA")
        self.workspace = os.environ.get("GITHUB_WORKSPACE")
