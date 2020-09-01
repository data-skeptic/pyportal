## Deployment / Release Process

Initially followed [these instructions](https://packaging.python.org/tutorials/packaging-projects/) to set up a pypi-test package.  The `.pypirc` is installed on Kyle's laptop and placed in his personal portal account.


## Release / Deploy

```
python3 -m twine upload --repository testpypi dist/*
```

## Install

```
python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps pyportal
```




python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps pyportal



