import os


class Context:
    @property
    def action(self):
        return os.environ.get("GITHUB_ACTION")

    @property
    def action_ref(self):
        return os.environ.get("GITHUB_ACTION_REF")

    @property
    def action_repository(self):
        return os.environ.get("GITHUB_ACTION_REPOSITORY")

    @property
    def actions(self):
        return os.environ.get("GITHUB_ACTIONS")

    @property
    def actor(self):
        return os.environ.get("GITHUB_ACTOR")

    @property
    def actor_id(self):
        return os.environ.get("GITHUB_ACTOR_ID")

    @property
    def api_url(self):
        return os.environ.get("GITHUB_API_URL")

    @property
    def base_ref(self):
        return os.environ.get("GITHUB_BASE_REF")

    @property
    def env(self):
        return os.environ.get("GITHUB_ENV")

    @property
    def event_name(self):
        return os.environ.get("GITHUB_EVENT_NAME")

    @property
    def event_path(self):
        return os.environ.get("GITHUB_EVENT_PATH")

    @property
    def graphql_url(self):
        return os.environ.get("GITHUB_GRAPHQL_URL")

    @property
    def head_ref(self):
        return os.environ.get("GITHUB_HEAD_REF")

    @property
    def job(self):
        return os.environ.get("GITHUB_JOB")

    @property
    def output(self):
        return os.environ.get("GITHUB_OUTPUT")

    @property
    def path(self):
        return os.environ.get("GITHUB_PATH")

    @property
    def ref(self):
        return os.environ.get("GITHUB_REF")

    @property
    def ref_name(self):
        return os.environ.get("GITHUB_REF_NAME")

    @property
    def ref_protected(self):
        return os.environ.get("GITHUB_REF_PROTECTED")

    @property
    def ref_type(self):
        return os.environ.get("GITHUB_REF_TYPE")

    @property
    def repository(self):
        return os.environ.get("GITHUB_REPOSITORY")

    @property
    def repository_id(self):
        return os.environ.get("GITHUB_REPOSITORY_ID")

    @property
    def repository_owner(self):
        return os.environ.get("GITHUB_REPOSITORY_OWNER")

    @property
    def repository_owner_id(self):
        return os.environ.get("GITHUB_REPOSITORY_OWNER_ID")

    @property
    def retention_days(self):
        return os.environ.get("GITHUB_RETENTION_DAYS")

    @property
    def run_attempt(self):
        return os.environ.get("GITHUB_RUN_ATTEMPT")

    @property
    def run_id(self):
        return os.environ.get("GITHUB_RUN_ID")

    @property
    def run_number(self):
        return os.environ.get("GITHUB_RUN_NUMBER")

    @property
    def server_url(self):
        return os.environ.get("GITHUB_SERVER_URL")

    @property
    def sha(self):
        return os.environ.get("GITHUB_SHA")

    @property
    def step_summary(self):
        return os.environ.get("GITHUB_STEP_SUMMARY")

    @property
    def triggering_actor(self):
        return os.environ.get("GITHUB_TRIGGERING_ACTOR")

    @property
    def workflow(self):
        return os.environ.get("GITHUB_WORKFLOW")

    @property
    def workflow_ref(self):
        return os.environ.get("GITHUB_WORKFLOW_REF")

    @property
    def workflow_sha(self):
        return os.environ.get("GITHUB_WORKFLOW_SHA")

    @property
    def workspace(self):
        return os.environ.get("GITHUB_WORKSPACE")
