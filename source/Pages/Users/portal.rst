.. _portal:

**********************
User management portal
**********************

.. contents:: 
    :depth: 4

.. _general_portal:

=======
General
=======

The user management portal is an interface to add, modify and delete Jupyter
users and groups.

.. _access_portal:

====================
Access to the portal
====================
After first setup of the Jupyter environment an e-mail has been send to the
contact person of the created Jupyter environment. This e-mail contains the
login information about the portal.

**URL:** https://<custom>-portal.jove.surfsara.nl/

.. _users_portal:

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


.. _groups_portal:

=================================
Enable users to access the portal
=================================
All users that are member of the group *admin* are allowed to login the portal.
By default the user *portaladmin* has been added to the group *admin*.

Select the tab *GROUP MEMBERS* to add members to the group *admin*:

.. image:: /Images/screenshot_portal_groups.png


