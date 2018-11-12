JupyterHub documentation
========================

This is the JupyterHub documentation by SURFsara. 
In this documenation we cover how to manage users and distribute content to the users.

.. sidebar:: Need help?

   We are always willing to help! Contact us at helpdesk@surfsara.nl.

Starting out
------------

When the environment is ready for you, you will receive an e-mail containing all relevant information:

* URL: https://something.projects.sda.surfsara.nl
* Admin username: *
* Admin password: *
* API URL: https://something-api.projects.sda.surfsara.nl/usermgmtapi/
* Portal URL: https://something-portal.projects.sda.surfsara.nl
* API-key: *

Here you will need to substitude `something` based on your deployment.

To simply start a Jupyter notebook go to https://something.projects.sda.surfsara.nl and login.
This will start a new notebook just for you. The inital loading can take everything from 3 seconds to 5 minutes.

All work done by you in this notebook is saved between logins.
That being said, we do not guarantee the data on the notebook and you should not treat the notebook as storage medium and save your data/work as you would do on other systems (git etc.). 

Each notebook started from JupyterHub will have the same tools installed.
We offer a few **pre-configured** notebooks based on the selection available on `jupyter-docker-stacks <https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html>`_
In addition to these images we can further customize these images with additional packages or plugins.

.. jupyter-docker-stacks: 

The notebooks which we offer come with **nbgitpuller** which allows you to distribute content to all your users via a link. See more in :ref:`distributing content <distributing>`.
For simple python package management keep in mind that installing packages at the user-level will persist between logins.
::

  pip install --user package-name

Packages installed with-out the "--user" flag will not persist between logins.

Documentation
--------------

.. toctree::
   :maxdepth: 2

   Pages/Users/portal
   Pages/Users/api
   Pages/Data/distributing
