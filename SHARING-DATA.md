# Managing & sharing data
The Jupyter notebook service contains two data stores by default: the user's home directory, and the shared data storage.

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
1. Sharing read-only data through the shared data storage

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
https://jupyter.something.sda-dev-projects.nl/hub/user-redirect/git-pull?repo=<your-repo-url>&branch=<your-branch-name>&subPath=<redirection>
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
https://jupyter.example.sda-dev-projects.nl/hub/user-redirect/git-pull?repo=https://github.com/sara-nl/jupyter-bigdata-notebooks&branch=master&subPath=notebooks/01-python.ipynb
```

When this link is clicked the following will happen:

1. The user will be promted for login credentials for the Jupyter notebook environment at `https://jupyter.example.sda-dev-projects.nl/`.
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
Large data sets can be shared with user through the shared data storage. All data on the shared data storage will be available in users' notebook containers as a **read-only data set**.
Since the data on the shared storage is read-only, users should first copy the data to their home directory before they can modify the data.

The shared data storage is hosted through an S3-compatible object store called Minio, available in each Jupyter environment. The 'Shared data storage URL' of the object store for your environment will have been provided to you, as well as the 'Shared data storage access key' and 'Shared data storage access key' needed to log in. All data uploaded to the object store is synchronized to the machines on which notebook containers are running, and will be mounted automatically in users' notebook containers under `/data`.

### Managing the shared data storage
There are several ways of managing data in the shared data storage: 
* Through the web interface
* Via an S3 client
* With the Minio command line client. 

These three options will be discussed below.

### The Minio web interface
The first is through the web interface available under the provided URL. After entering your access and secret key and logging in, you should see a web interface with a file browser. On the left side of the file browser will be a list of so-called *buckets*. The data storage will by default have a single bucket called `data`, listed on the left side of the screen. All data in this bucket will be available automatically in the users' notebook containers.

Clicking on the bucket `data` on the left side of the screen will show the contents of the bucket on the right side of the screen. Since this bucket is initially empty, you will not see any files listed until data has been uploaded.

To upload a file, click on the plus sign in the red circle in the bottom-right corner of the screen, and select upload file (the top option) in the menu that pops up. After selecting files to upload in the file selection dialog, Minio will upload the files one by one.

To delete a file, select the checkbox on the left side of the file name in the file browser, and select 'Delete selected' in the menu bar that pops up on the top of the screen.

**Please be aware that there is a file size limit of 128 MB when uploading files through the web interface. Upload larger files with an S3 client or with the Minio command line client (see below).**

### S3 client
The shared data storage is S3-compatible, and should be accessible with any S3-compatible client through the provided URL with the access and secret keys. Cyberduck is a popular storage client available for Windows and macOS, and downloadable from the Cyberduck [website](https://cyberduck.io/). The remainder of this subsection will explain how to manage the shared data storage with Cyberduck.

### Minio command line client
The Minio command line client, `mc`, is available for Windows, macOS and Linux. It can be downloaded from the [Minio website](https://docs.min.io/docs/minio-client-complete-guide). After downloading it, please make sure it is available on the path by modifying the `$PATH` environment variable.

First, add the data storage for the environment to the client using the URL, access key and secret key provided to you:

```bash
$ mc config host add alias URL ACCESSKEY SECRETKEY
```

Here, `alias` should be a name with which you will refer to the storage for this environment in the future. The name can be anything.

To copy a file called `data.csv` from your local machine to the `data` bucket in the shared data storage, use `mc cp`:

```bash
$ mc cp data.csv alias/data/data.csv
```

Here, `alias` in the command above should be replaced with the one you chose in the first command above.

To remove a file called `data.csv` from the `data` bucket, use `mc rm`:

```bash
$ mc rm alias/data/data.csv
```

As an administrator, you have full access rights on the `data` bucket. For more information about the functionality exposed by the Minio client, please see the [Minio client complete guide](https://docs.min.io/docs/minio-client-complete-guide).

#### Synchronization
Depending on the size of the data and the number of files in the shared data storage, synchronization to the different machines in the Jupyter cluster can take a while. Our experiments indicate that ..., but please be aware that depending on circumstances this may take more or less time. We advise you to upload the data some time before the data will be used, so there will be enough time to synchronize all data.
