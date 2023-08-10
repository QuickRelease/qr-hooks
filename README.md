A collection of useful pre-commit hooks

## Hooks

### django-no-auto-migrations

Detect auto-named migrations eg. `0000_auto_202012251330.py`

### django-url-trailing-slash

Detect any URL paths in `urls.py` without a trailing slash

### django-invalid-perm

Detect `has_perm` or `@permission_required` usage with an invalid perm (eg. `has_perm("core:add_user")`)

## TODO

### django-invalid-perm

- Update regex for `permission_required` to account for multiple permissions eg. detect `@permission_required(["user.change_user", "user:add_user"])`


## Contributing

Create a virtual env and install the requirements:

```cmd
pip install -r requirements/test.txt
```

Run the tests:

```cmd
pytest
```
