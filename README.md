# TailwindCSS and Django

In this repository, I practice the integration process of Django and TailwindCSS. My goal is to achieve a best practice to configure my furthcoming projects.

## Python virtual environments

```bash
mkdir project_directory
cd project_directory
python -V # at the time of development, I use 3.10.8 since 3.11 is inapplicable in some projects (e.g., Celery)
python -m pip install --upgrade pip
python -m venv venv # the latter venv is optional and you can choose a different name as you wish
source venv/bin/activate # activates the environment, to quit press <CTRL D> or use deactivate command
```

## Required packages

```bash
python -m pip install 'django<4.2' # installing the latest version of django 4.1
mkdir src && cd src
```

### Start developing

```bash
django-admin startproject conf . # creates a project named `conf` in the current directory (i.e., src)

```
