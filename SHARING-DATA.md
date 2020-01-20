# Managing & sharing data
The Jupyter notebook service contains two data stores by default: the user's home directory, and the shared data storage. The shared data storage is an optional component of the service, and is disabled by default.

## User home directories
When a user's notebook container starts, the *user's home directory* will be available as **persistent storage** inside the notebook container. Regardless of the user name, the persistent storage will be mounted under `/home/jovyan`. Changes made to files and directories under this path will persist between logins and container restarts.

Although the user's home directory is persistent, you should not rely on it as a reliable file storage solution. Important data should be backed up to an external system. In addition, **no backups are made of any user's home directory**. When a user removes files themselves, or when the home directory is wiped or corrupted by a hardware of software outage, the **data will not be recoverable**.

Administrators cannot access users' home directories: they are only accessible through the username and password from the users themselves.

## Shared data storage
The shared data storage provides a storage solution for hosting large data sets, and is managed by administators. Data in the shared data storage solution is available **read-only** inside each notebook container under `/data`.

## Sharing data
The Jupyter notebook service provides several ways of sharing data with end-users:

1. Cloning a git repository during container startup to a user's home directory
1. Cloning a git repository with an nbgitpuller link to a user's home directory
1. Sharing read-only data through the shared data storage, see also [shared data storage guide](MINIO-SHARED-DATA-STORAGE.md)

The first two options will clone a git repository in the **user's home directory**. Changes made to files in a user's home directory **are persistent**. We advise these two options for distributing notebooks and small data sets. For larger data sets (a few hundred megabytes to dozens of gigabytes) we advise to use the shared data storage solution (option 3).

**Please note that options 1 and 2 cannot be used together: when option 1 is used, option 2 will not work, and vice versa.**

## Option 1: cloning a git repository during container startup
When SURFsara provisions a notebook environment, a link to a git repository can be provided by an administrator. This link will be used to clone the repository to the **user's home directory** when a user's notebook container starts up.

Any changes made to these files in a user's home directory will be saved between logins: **data is persistent**. When changes are made to the files in the git repository, they will be merged with the files in the user's home directory. Depending on the changes a user has made to their local files, this merge can either incorporate the changes from the git repository, or create a *separate version* of a particular file. The latter case occurs frequently when making changes to notebooks, because notebooks are difficult for git to merge successfully. As such, it may happen that when the git repository is modified, two versions of the same notebook will appear in a user's notebook environment.

We advise to use this option when distributing notebooks, scripts, and small data sets. It is the simplest way to provide all users with some material in their home directories, without needing to click on a special link (option 2), or copy data from the shared data storage (option 3).

## Option 2: cloning a git repository with an nbgitpuller link
[nbgitpuller](https://jupyterhub.github.io/nbgitpuller/) is a tool to clone a git repository through a URL. When a notebook container starts up, nbgitpuller will clone the repository provided in the URL.

To start a notebook container with an automatic clone of a git repository through nbgitpuller, you will need to format a URL. The easiest way to do so is with the nbgitpuller [link generator](https://jupyterhub.github.io/nbgitpuller/link). By providing the JupyterHub URL and the git repository URL, it will generate a link that you can send to end-users.

Alternatively, you can generate the URL manually by creating it according to the following format:

```
https://jupyter.something.k8s.surfsara.nl/hub/user-redirect/git-pull?repo=<your-repo-url>&branch=<your-branch-name>&subPath=<redirection>
```

For example, with the following parameters:

```
<something> = example
<your-repo-url> = https://github.com/sara-nl/jupyter-bigdata-notebooks
<your-branch-name> = master
<redirection> = notebooks/01-python.ipynb
```

the output will be:

```
https://jupyter.example.k8s.surfsara.nl/hub/user-redirect/git-pull?repo=https://github.com/sara-nl/jupyter-bigdata-notebooks&branch=master&subPath=notebooks/01-python.ipynb
```

When this link is clicked the following will happen:

1. The user will be promted for login credentials for the Jupyter notebook environment at `https://jupyter.example.k8s.surfsara.nl/`.
1. After logging in, a notebook container will be started, and the repository at [https://github.com/sara-nl/jupyter-bigdata-notebooks](https://github.com/sara-nl/jupyter-bigdata-notebooks) will be cloned from the **master** branch to the user's home directory.
1. The user is redirected to **notebooks/01-python.ipynb** of the repository.

For more information on all the options provided by nbgitpuller, please see the [documentation](https://jupyterhub.github.io/nbgitpuller/).

### Resynchronizing data from the repository
Accessing the URL again will update the user's home directory from the specified repository. This update behaviour tries to keep local changes to the repository with the following features:

1. If the user has changed files locally in their home directory, those changes will take precedence over the changes in the remote repository.

1. If a file was deleted locally from the user's home directory but is present on the remote repository, the remote file is restored to local repository. This allows users to get a 'fresh copy' of a file by just deleting the file locally and clicking the link again.

### Notes
* Clicking the link repeatedly does no harm.
* Since each user is prompted for login credentials, the same link can be used for all users.
* Consider sending the user a shorter version of the link, using for example [bitly](https://bitly.com/).
* nbgitpuller does not support git submodules, so you need to pull each individual git repository.
* The git repository needs to be public.

## Option 3: sharing read-only data through the shared data storage
Large data sets can be shared with user through the shared data storage. All data on the shared data storage will be available in users' notebook containers as a **read-only data set**. More information on the shared data storage solution can be found here: [shared data storage guide](MINIO-SHARED-DATA-STORAGE.md)

