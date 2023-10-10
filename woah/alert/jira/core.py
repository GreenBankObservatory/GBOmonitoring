from __future__ import annotations
import re
from getpass import getuser
from pathlib import Path
import environ
import os
import pprint
import json
pp = pprint.PrettyPrinter(indent=4)

from jira import JIRA

class JIRAServer:
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
        self.object_type = "JIRA Server"
        self.server_name = "GBO Jira"
        self.load_environment()
        self.connect(self.env)

    def load_environment(self):
        self.JIRA_SETTINGS_DIR = Path(__file__).resolve().parent
        self.env = environ.Env()
        _env_file_template_path = Path(self.JIRA_SETTINGS_DIR, "jira.env.template")
        _default_env_file_path = Path(self.JIRA_SETTINGS_DIR, "jira.env")
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
        JIRA_SERVER = self.env("JIRA_SERVER")        
        JIRA_EMAIL = self.env("JIRA_EMAIL")
        JIRA_API_KEY = self.env("JIRA_API_KEY")
        self.jira_connect = JIRA(server=JIRA_SERVER, basic_auth=(JIRA_EMAIL, JIRA_API_KEY))

    def info(self):
        # [TODO] Make a return, not a print statement
        pp.pprint(vars(self))

class JIRAProject(JIRAServer):
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
        JIRAServer.__init__(self)
        self.object_type = "JIRA Project"
        self.project_name = "WOAH"


class JIRAIssueList(JIRAProject):
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
        JIRAProject.__init__(self)
        self.object_type = "JIRA Issue List"
        self.get_project_id()
        self.load_all()

    def get_project_id(self):
        self.JIRA_PROJECT_ID = int(self.env("JIRA_PROJECT_ID"))

    def load_all(self):
        self.all_issues = self.jira_connect.search_issues(f'project={self.JIRA_PROJECT_ID}')

    def info_fields(self):
        fpath = Path(self.JIRA_SETTINGS_DIR, "_static/issue_info.json")
        print(fpath)
        f = open(fpath)
        fdata = json.load(f)
        print("These are the following fields an issue can have:")
        pp.pprint(fdata)
        f.close()

class JIRAIssue(JIRAIssueList):
    '''
    Description

    Parameters
    ----------
        None

    Returns
    -------
        None
    
    '''
    def __init__(self, issue_type=None, issue_id=None):
        # [TODO] Make sure issue is selected/created before adding/editing fields
        JIRAIssueList.__init__(self)
        self.object_type = "JIRA Issue"
        self._init_issue(issue_type, id)

    def _init_issue(self, issue_type, issue_id):
        if issue_type == "new":
            self.create_issue()
            self.new_issue = True
        else:
            self.select_issue(issue_id)
            self.new_issue = False

    def select_issue(self, issue_id):
        self.selected_issue = self.jira_connect.issue(issue_id)
        self._init_fields()

    def edit_field(self, field_name, field_contents, overwrite=False):
        # [TODO] Add logic for overwriting vs. keeping old
        self.fields[field_name] = field_contents

    def create_issue(self):
        self._init_fields()

    def _init_fields(self):
        self.fields = {
            "project":{"id":self.JIRA_PROJECT_ID},
            'issuetype': {'name': 'Bug'},
            }
        self.new_issue = True
        self.published = False

    def add_field(self, field_name, field_contents):
        self.fields[field_name] = field_contents

    def assign_to(self, full_name):
        # [TODO] The "self" doesn't work. Needs the issue ID
        # self.jira_connect.assign_issue(self, full_name)
        pass

    def publish(self):
        if self.new_issue:
            self.jira_connect.create_issue(fields=self.fields)
            self.new_issue = False
        else:
            self.selected_issue.update(fields=self.fields)
        self.published = True