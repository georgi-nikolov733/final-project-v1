# Example App

A basic Python app used to depomstrate the CI/CD pipeline.

## Step 1. Checking for credentials:

Using the pre-build [Easy detect-secrets](https://github.com/marketplace/actions/easy-detect-secrets) action to check for hardcoded credential.

The credentials that the actions checks for are listed in the [.secrets.baseline](https://github.com/georgi-nikolov733/final-project-v1/blob/master/.secrets.baseline) file in the repository.

## Step 2. Lint, style and SAST:

#### Linting 

Installing the package manager [pip](https://pip.pypa.io/en/stable/) then using it to install [pylint](https://pylint.org/)

```yaml
- name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pylint
        pip install pylint-exit
    - name: Lint with pylint
      run: |
        find . -name 'example.py' -exec pylint {} \;
```

#### Style

Installing the package manager [pip](https://pip.pypa.io/en/stable/) then using it to install [pycodestyle](https://pypi.org/project/pycodestyle/)

```yaml
- name: Install dependencies
      run: |
        python --version
        python -m pip install --upgrade pip
        pip install pycodestyle
    - name: Style with pycodestyle
      run: |
        python --version
        pycodestyle *.py
```

#### Static Application Security Testing (SAST)

The Static Application Security Testing is done by using [SonarCloud](sonarcloud.io) with the pre-build Github Action [SonarCloud Scan](https://github.com/marketplace/actions/sonarcloud-scan).

## Step 3. Unit Testing:

The unit-testing is done by using [doctest](https://docs.python.org/3/library/doctest.html).

```yaml
- name: Unit testing
      run: |
           python --version 
           python3 -m doctest example.py
```

## Step 4. Building and uploading the Docker image:

Building a docker image and uploading it to [DockerHub](https://hub.docker.com/) using this [Dockerfile](https://github.com/georgi-nikolov733/final-project-v1/blob/master/Dockerfile) and the official Github Action [Build and push Docker images](https://github.com/marketplace/actions/build-and-push-docker-images) published by Docker.




