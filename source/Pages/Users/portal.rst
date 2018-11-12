.. _users_portal:

User management portal
======================

.. contents:: 
    :depth: 2

.. _users_general_portal:

General
-------

The user management portal is an interface to **add**, **modify** and **delete** Jupyter
users and groups.

.. _users_access_portal:

Access to the portal
--------------------

After first setup of the JupyterHub environment an e-mail has been sent to the
contact person of the created JupyterHub environment. This e-mail contains the
login information for the portal.
::

  Username: <username>
  Password: <password>
  URL: https://<something>-portal.projects.sda.surfsara.nl

.. _users_users_portal:

Create new users
------------------------

Select the tab *ADD USER* to create new users:

**login**
    - A unique login name

**password**
    - minimal 8 characters
    - only character and numbers are allowed

.. image:: /Images/screenshot_portal.jpg

The portal enables you to add users one by one. See :ref:`API documentation <users_api>` to add multiple
users at once or other advanced options.

By default, new users can only log into Jupyter notebooks through the JupyterHub and do not have access to the `User management portal`. 

.. _users_groups_portal:

Access to the portal
-------------------------------------------------
Users which are members of the group *admin* can login to the portal and create more users.
By default the user *portaladmin* has been added to the group *admin*.
Members from other groups cannot access the portal and create more users.

Select the tab *GROUP MEMBERS* to add members to the group *admin*:

.. image:: /Images/screenshot_portal_groups.png

