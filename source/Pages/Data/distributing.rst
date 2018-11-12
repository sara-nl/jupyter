.. _distributing:

Distributing data
=================

.. contents:: 
    :depth: 2


.. _content_distributing:

Cloning a git repository on start / with a link
-------------------------------------------------

A common way to distribute content to the user's home directory is through git clone/pull.
This can be difficult for inexperienced users.

We use `nbgitpuller <https://github.com/jupyterhub/nbgitpuller>`_ to offer automatic git cloning/pulling so that the user can simply click a link and the repository will cloned/pulled.

This functionality is made accessible through a URL, such as  `https://your-domain.com/hub/user-redirect?git-pull?repo=https://github.com/repo/&subPath=directoy/notebook.ipynb <https://your-domain.com/hub/user-redirect?git-pull?repo=https://github.com/repo/&subPath=directoy/notebook.ipynb>`_.
When the user clicks this link, the specified repository will be cloned to the user home directory and subsequently redirected to 'directoy/notebook.ipynb' which specifies a notebook in the git repository.

Creating the link
------------------

Simply substitute each '<variable>' with your 'value':
::

  https://<custom>.projects.sda.surfsara.nl/hub/user-redirect/git-pull?repo=<your-repo-url>&branch=<your-branch-name>&subPath=<redirection>

For example:
:: 

  <custom> = base
  <your-repo-url> = https://git.osd.surfsara.nl/srb/notebooks
  <your-branch-name> = master
  <redirection> = track1-unix-cluster/cartesius-demo.md

The output will be:
::

  https://base.projects.sda.surfsara.nl/hub/user-redirect/git-pull?repo=https://git.osd.surfsara.nl/srb/notebooks&branch=master&subPath=track1-unix-cluster/cartesius-demo.md


When this link is clicked the following will happen:

1) The user will be promted for login credentials for **base.projects.sda.surfsara.nl**. The user successfully logs in.

2) The environment will be allocated and the **https://git.osd.surfsara.nl/srb/notebooks** repository will be cloned from the **master** branch to the user's home directory.

3) The user is redirected to **track1-unix-cluster/cartesius-demo.md** of the repo.

.. _JupyterHub: https://the-littlest-jupyterhub.readthedocs.io/en/latest/howto/content/nbgitpuller.html
.. _binder: https://mybinder.org/v2/gh/jupyterhub/nbgitpuller/master?urlpath=apps/binder%2Flink_generator.ipynb

For more detailed information on how to create a link see `JupyterHub`_ and the `binder`_ application. 

Resynchronizing
---------------

Clicking the link again will update the cloned repository.
This update behaviour tries to keep local changes to the repository with the following features.

* If some edits have been made by the user in files in the git repository, those changes will take presidence over the changes in the remote repository.

* If a file was deleted locally but is present in the remote, the remote file is restored to local repository. This allows users to get a 'fresh copy' of a file by just deleting the file locally and clicking the link again.

.. _official: https://github.com/jupyterhub/nbgitpuller#merging-behavior

For more details see the `official`_ documentation 

Advanced notes
--------------
- Clicking the link repeatedly does no harm.
- Since each user is prompted for login credentials, the same link can be used for all users.
- Consider sending the user a shorter version of the link, using for example `bitly <https://bitly.com/>`_ .
- "nbgitpuller" does not support git submodules, so you need to pull each individual git repository.
- The git repository needs to be public.
