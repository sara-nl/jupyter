.. _users_portal:

**********************
User management portal
**********************

.. contents:: 
    :depth: 4

.. _users_general_portal:

=======
General
=======

The user management portal is an interface to add, modify and delete Jupyter
users and groups.

.. _users_access_portal:

====================
Access to the portal
====================
After first setup of the JupyterHub environment an e-mail has been sent to the
contact person of the created JupyterHub environment. This e-mail contains the
login information for the portal.

**URL:** `https://<custom>-portal.jove.surfsara.nl/ <https://<custom>-portal.jove.surfsara.nl/>`_

.. _users_users_portal:

========================
Create new Jupyter users
========================
Select the tab *ADD USER* to create new users:

**login**
    - unique login name used to login Jupyter

**password**
    - minimal 8 characters
    - only character and numbers are allowed

.. image:: /Images/screenshot_portal.jpg

The portal enables you to add users one by one. See :ref:`API documentation <users_api>` to add multiple
users at once or other advanced options.

By default, new users have the same privilege as a member in the group *users* which can log in and access notebooks.


.. _users_groups_portal:

=================================================
Enable users to access the user-management portal
=================================================
Users which are members of the group *admin* can login to the portal and create more users.
By default the user *portaladmin* has been added to the group *admin*.
Members from other groups cannot access the portal and create more users.

Select the tab *GROUP MEMBERS* to add members to the group *admin*:

.. image:: /Images/screenshot_portal_groups.png


