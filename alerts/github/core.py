from pathlib import Path
import environ
import os, sys
import pprint
import json, requests
pp = pprint.PrettyPrinter(indent=4)

class GitHubServer:
    '''
    Description

    Parameters
    ----------
        None

    Returns
    -------
        None
    
    '''
    def __init__(self):
        self.object_type = "GitHub Server"
        self.load_environment()
        self.connect(self.env)

    def load_environment(self):
        self.GITHUB_SETTINGS_DIR = Path(__file__).resolve().parent
        self.env = environ.Env()
        _env_file_template_path = Path(self.GITHUB_SETTINGS_DIR, ".github-env.template")
        _default_env_file_path = Path(self.GITHUB_SETTINGS_DIR, ".github-env")
        _env_file_path = self.env.str("ENV_PATH", _default_env_file_path)
        if not Path(_env_file_path).exists():
            raise ValueError(
                f"You must create a .env file at {_default_env_file_path} "
                f"(use {_env_file_template_path} as a template), "
                "or specify another path via the ENV_PATH variable"
            )
        try:
            with open(_env_file_path):
                pass
        except PermissionError as error:
            raise PermissionError(
                f"You do not have permission to read {_env_file_path}. Please contact gbosdd@nrao.edu"
                "if this is in error"
            ) from error
        environ.Env.read_env(_env_file_path)

    def connect(self, env):
        GITHUB_USERNAME = self.env("GITHUB_USERNAME")        
        self.GITHUB_TOKEN = self.env("GITHUB_TOKEN")
        self.GITHUB_REPO_URL = self.env("GITHUB_REPO_URL")
        self.session = requests.sessions.Session()
        self.session.auth = (GITHUB_USERNAME, self.GITHUB_TOKEN)

class GitHubIssue(GitHubServer):
    '''
    Description

    Parameters
    ----------
        None

    Returns
    -------
        None
    
    '''
    def __init__(self):
        GitHubServer.__init__(self)
        self._init_contents()

    def _init_contents(self):
        self.issue_contents = {}

    def add_field(self, field_name, field_contents):
        self.issue_contents[field_name] = field_contents

    def prep_export(self):
        self.post_headers = {
        "Authorization": f"token {self.GITHUB_TOKEN}",
        "Accept": "application/vnd.github.golden-comet-preview+json"
        }
        post_data = {'issue': self.issue_contents}
        self.post_payload = json.dumps(post_data)

    def publish(self):
        self.prep_export()
        self.response = requests.request("POST", self.GITHUB_REPO_URL, data=self.post_payload, headers=self.post_headers)
        self.check_response()
    
    def check_response(self):
        print(f"Status Code: {self.response.status_code}")
    
if __name__ == "__main__":
    test_issue = GitHubIssue()
    test_issue.add_field('title', '[TEST] Issue Title')
    test_issue.add_field('body', 'Body text for the test issue')
    test_issue.add_field('labels', ['WOAH Auto'])
    test_issue.publish()