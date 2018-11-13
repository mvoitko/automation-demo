## Prerequisites
### Recommended:

OS: Unix-based (Linux, MacOS)

Shell: [Zshell](https://ohmyz.sh/)

### Must install dependencies in order of mentioning:
1. [Python 3.7](https://www.python.org/downloads/)
2. [poetry](https://poetry.eustace.io/docs/#installation)
3. [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/install.html)
4. [git](https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/)
5. [Create account on Github](https://github.com/join)

### Project installation

Open Terminal run the following commands:
1. Navigate to project directory:
```bash
cd /path/to/projects/directory/
```
2. Clone the repository:
```bash
git clone git@github.com:mvoitko/automation-demo.git
```
3. Navigate to project directory:
```bash
cd automation-demo
```
4. Create virtualenv:
```bash
mkvirtualenv -p python3.7 automation-demo
```
5. Install project dependencies with:
```bash
poetry install
```

### Running tests
Run the following command *IN PROJECT FOLDER*:
```bash
pytest
```
