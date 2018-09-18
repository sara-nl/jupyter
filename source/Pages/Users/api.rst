.. _users_api:

*******************
User management api
*******************

The user management api is an advanced way to add, modify and delete Jupyter
users and groups. Please be careful when adding and changing users and groups
with the api. Some special settings are needed and without these settings it may not work properly anymore.

An easier way to manage users and groups is by using the :ref:`portal <users_portal>`

.. contents:: 
    :depth: 4


.. _users_credentials_api:

===========
Credentials
===========
After first setup of the Jupyter environment an e-mail has been sent to the
contact person of the created Jupyter environment. This e-mail contains the
api credentials.

- Api: `https://<custom>-api.jove.surfsara.nl/usermgmtapi/ <https://<custom>-api.jove.surfsara.nl/usermgmtapi/>`_
- Application: jaas-ldap-api
- Key: **********

.. _users_specifications_api:

==================
API specifications
==================
The swagger interface makes it possible to make changes to users and groups via api calls at a website:

- `https://<custom>-api.jove.surfsara.nl/usermgmtapi/ <https://<custom>-api.jove.surfsara.nl/usermgmtapi/>`_

This is also the documentation of the api.

For managing single users and groups we advise to use the :ref:`portal <users_portal>`. For advanced usage
it is possible to make api calls by the swagger api .


This example shows how to use it:

- Click on *Expand Operations* below 'This API provides endpoints for managing JAAS LDAP user entries.'
- Fill credentials at X-API-Application and X-API-Key fields

.. image:: /Images/screenshot_swagger_users.png

- Click 'Try it out'

.. image:: /Images/screenshot_swagger_users_output.png


.. _users_commandline_api:

=====================
Command line example
=====================

- Copy curl command from swagger interface:

.. image:: /Images/screenshot_swagger_users_curl.png


.. code-block:: bash

    curl -X GET --header 'Accept: application/json'
    --header 'X-API-Application: jaas-ldap-api'
    --header 'X-API-Key: *********'
    'https://laura-dev-api.jove.surfsara.nl/usermgmtapi/v1/jaas-ldap-rest/user/'

    {"users":[{"dn":"cn=laura,ou=users,dc=laura-dev,dc=jove,dc=surfsara,dc=nl",
    "givenName":"Laura","sn":"Leistikow","cn":"laura","uid":"laura",
    "userPassword":"*******","uidNumber":"5001","gidNumber":"500",
    "homeDirectory":"","loginShell":"","mail":"laura@laura-dev.jove.surfsara.nl",
    "employeeType":"portal"},{"dn":"cn=portaladmin,ou=users,dc=laura-dev,
    dc=jove,dc=surfsara,dc=nl","givenName":"portaladmin","sn":"smoketest",
    "cn":"portaladmin","uid":"portaladmin","userPassword":"*********",
    "uidNumber":"1003","gidNumber":"501","homeDirectory":"/}


==========================
Add multiple users example
==========================

- Create add_multiple_user script

.. code-block:: bash

    vi add_multiple_user.bash

- Copy code and replace credentials

.. code-block:: bash

    #!/bin/bash

    url="https://laura-dev-api.jove.surfsara.nl/usermgmtapi/v1/jaas-ldap-rest/user/"
    application="jaas-ldap-api"
    key="******************"
    input="users.cvs"

    while IFS=',' read -r f1 f2 f3 f4 f5
    do
    # Add user
    curl -X PUT "$url" \
        -H "Content-Type: application/json" \
        -H "Accept: application/json" \
        -H "X-API-Application: $application" \
        -H "X-API-Key: $key" \
        --data @- <<END;
        {
           "givenName": "$f2", \
           "sn": "$f3",
           "cn": "$f1",
           "uid": "$f1",
           "userPassword": "$f4",
           "homeDirectory": "",
           "loginShell": "",
           "mail": "$f5",
           "employeeType": "portal"
        }
    END

        done < "$input"

- Create users.cvs file

.. code-block:: bash

    vi users.cvs

- Add users in users.cvs: login, firstname, lastname, password, email(optional)

.. code-block:: bash

    login1,firstname1,lastname1,password1
    login2,firstname2,lastname2,password2
    login3,firstname3,lastname3,password3

- Run the add_multiple_user.bash script

.. code-block:: bash

    chmod +x add_multiple_user.bash
    ./add_multiple_user.bash
    {"dn":"cn=login1,ou=users,dc=laura-dev,dc=jove,dc=surfsara,dc=nl",
    "givenName":"firstname1","sn":"lastname1","cn":"login1","uid":"login1",
    "userPassword":"[B@51bd4df5","uidNumber":"5002","gidNumber":"500","homeDirectory":"",
    "loginShell":"","mail":"login1@laura-dev.jove.surfsara.nl",
    "employeeType":"portal"}{"dn":"cn=login2,ou=users,dc=laura-dev,dc=jove,dc=surfsara,dc=nl",
    "givenName":"firstname2","sn":"lastname2","cn":"login2","uid":"login2",
    "userPassword":"[B@563c80fe","uidNumber":"5003","gidNumber":"500",
    "homeDirectory":"","loginShell":"","mail":"login2@laura-dev.jove.surfsara.nl",
    "employeeType":"portal"}{"dn":"cn=login3,ou=users,dc=laura-dev,dc=jove,dc=surfsara,dc=nl",
    "givenName":"firstname3","sn":"lastname3","cn":"login3","uid":"login3",
    "userPassword":"[B@582421cf","uidNumber":"5004","gidNumber":"500","homeDirectory":"",
    "loginShell":"","mail":"login3@laura-dev.jove.surfsara.nl","employeeType":"portal"}

- Check the portal

.. image:: /Images/screenshot_portal_show_users.png








