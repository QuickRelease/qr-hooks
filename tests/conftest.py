import re

import pytest
from pre_commit.clientlib import load_manifest
from pre_commit.constants import MANIFEST_FILE


@pytest.fixture(scope="session")
def pre_commit_manifest():
    return load_manifest(MANIFEST_FILE)


@pytest.fixture
def pygrep_hook(pre_commit_manifest):
    def _regex(hook_id):
        hook = next(filter(lambda hook: hook["id"] == hook_id, pre_commit_manifest))
        return re.compile(hook["entry"])

    return _regex
