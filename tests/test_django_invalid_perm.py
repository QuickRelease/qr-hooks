import pytest

@pytest.fixture
def invalid_perm(pygrep_hook):
    return pygrep_hook("django-invalid-perm")


@pytest.mark.parametrize(
    "s",
    (
        'request.user.has_perm("user:change_user")',
        'if request.user.has_perm("user:change_user")',
        '@permission_required("user:change_user")',
    ),
)
def test_path_fail(invalid_perm, s):
    assert invalid_perm.search(s)


@pytest.mark.parametrize(
    "s",
    (
        'request.user.has_perm("user.change_user")',
        'if request.user.has_perm("user.change_user")',
        '@permission_required("user.change_user")',
        "non_permission_line"
    ),
)
def test_path_pass(invalid_perm, s):
    assert not invalid_perm.search(s)
