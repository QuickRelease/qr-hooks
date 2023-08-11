import pytest


@pytest.fixture
def missing_trailing_slash(pygrep_hook):
    return pygrep_hook("django-url-trailing-slash")


@pytest.mark.parametrize(
    "s",
    (
        'path("my-url", my_view)',
        '    path("my-url", my_view)',
        'path("accounts/login", LoginView.as_view(), name="login"),',
        """\
        path(
            "accounts/change_password",
            CustomPasswordChangeView.as_view(),
            name="password_change",
        ),
        """,
    ),
)
def test_path_fail(missing_trailing_slash, s):
    assert missing_trailing_slash.search(s)


@pytest.mark.parametrize(
    "s",
    (
        'path("my-url/", my_view)',
        '    path("my-url/", my_view)',
        'path("accounts/login/", LoginView.as_view(), name="login"),',
        'path("", include("core.urls")),',
        """\
        path(
            "accounts/change_password/",
            CustomPasswordChangeView.as_view(),
            name="password_change",
        ),
        """,
    ),
)
def test_path_pass(missing_trailing_slash, s):
    assert not missing_trailing_slash.search(s)


@pytest.mark.parametrize(
    "s",
    (
        '(r"^accounts/logout$", signout),',
        '("^accounts/logout$", signout),',
        '(r"^accounts/logout", signout),',
        """(
            r"^my-view$",
            my_view,
        ),""",
    ),
)
@pytest.mark.parametrize("url_func", ("url", "re_path"))
@pytest.mark.parametrize("indent", ("", "\t"))
def test_url_fail(missing_trailing_slash, url_func, indent, s):
    assert missing_trailing_slash.search(f"{indent}{url_func}{s}")


@pytest.mark.parametrize(
    "s",
    (
        '(r"^accounts/logout/$", signout),',
        '("", include("core.urls")),',
        '("^accounts/logout/$", signout),',
        '(r"^accounts/logout/", signout),',
        '(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT})',
        '(r"^user-guide/(?P<path>.*)$", serve_user_guide)',
        """(
            r"^my-view/$",
            my_view,
        ),""",
    ),
)
@pytest.mark.parametrize("url_func", ("url", "re_path"))
@pytest.mark.parametrize("indent", ("", "\t"))
def test_url_pass(missing_trailing_slash, url_func, indent, s):
    assert not missing_trailing_slash.search(f"{indent}{url_func}{s}")
