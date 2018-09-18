.. _distributing:

*****************
Distributing data
*****************

In this page you will find general information about the Jupyter api, how it works and what is suited for:

.. contents:: 
    :depth: 4


.. _content_distributing:

=======
Clone a git repository using a link
=======

A user's home directory is empty be default when JupyterHub creates a new notebook server.
A common way to distribute content to the user's home directory is through git clone/pull.
It can be difficult making the user manage git synchronization if the user is unfamiliar with git or does not have access to a terminal running on the notebook server.
We use "nbgitpuller" (https://github.com/jupyterhub/nbgitpuller) to offer automatic git pulling so that the user can simply click a link and the repository will cloned/pulled.
This functionality is made accessible through a URL, such as https://your-domain.com/hub/user-redirect?git-pull?repo=https://github.com/repo/&subPath=directoy/notebook.ipynb .
When a user clicks this link, the specified repository will be cloned to the user home directory and subsequently redirected to 'directoy/notebook.ipynb' which specifies a notebook in the git repository.
If the link is clicked again, the repository will be pulled again.

=======
Creating the link
=======

Simply substitute each '<variable>' with your 'value'

**URL** https://<custom>.jove.surfsara.nl/hub/user-redirect/git-pull?repo=<your-repo-url>&branch=<your-branch-name>&subPath=<redirection>

For example,

- <custom> = base
- <your-repo-url> = https://git.osd.surfsara.nl/srb/notebooks
- <your-branch-name> = master
- <redirection> = track1-unix-cluster/cartesius-demo.md

Resulting in the following URL.
**URL** https://base.jove.surfsara.nl/hub/user-redirect/git-pull?repo=https://git.osd.surfsara.nl/srb/notebooks&branch=master&subPath=track1-unix-cluster/cartesius-demo.md

This will clone the 'https://git.osd.surfsara.nl/srb/notebooks' repository from the 'master' branch to the user's home directory on JupyterHub 'http://base.jove.surfsara.nl' and then redirect the user to 'track1-unix-cluster/cartesius-demo.md'.

For more detailed information on how to create a link see https://the-littlest-jupyterhub.readthedocs.io/en/latest/howto/content/nbgitpuller.html
and the application https://mybinder.org/v2/gh/jupyterhub/nbgitpuller/master?urlpath=apps/binder%2Flink_generator.ipynb

- The user will be prompted for login credentials after linking the link.
- If the notebook server has not been initialized when the user clicks the link (i.e. the notebook environment is not ready) the notebook server will be started first and then the clone will be performed.
In this case, the user might have to wait from 5 secs up to a few minutes.
- Clicking the link repeatedly does no harm.
- Since each user is prompted for login credentials, the same link can be used for all users.
- Consider sending the user a shorter version of the link, using f.ex. bit.ly.

=======
Resynchronizing
=======

Edits in the remote git repository can be reflected by clicking the link again.
This will call git pull again.
If some edits have been made by the user in files in the git repository, those changes will take presidence over the changes in the remote repository.

If a file was deleted locally but is present in the remote, the remote file is restored to local repository.
This allows users to get a 'fresh copy' of a file by just deleting the file locally and clicking the link again.

For more details see the official documentation https://github.com/jupyterhub/nbgitpuller#merging-behavior

=======
Advanced notes
=======

- "nbgitpuller" does not support git submodules, so you need to pull each individual git repository.
- The git repository needs to be public.