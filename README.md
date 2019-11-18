# SURFsara Jupyter notebook administration guide
**This repository provides a user guide for administrators of SURFsara [Jupyter notebook service](https://www.surf.nl/en/jupyter-notebook-accessible-and-interactive-data-analysis-for-research-and-education)**.

For more information about this service, please see the overview page at the [SURFsara website](https://www.surf.nl/en/jupyter-notebook-accessible-and-interactive-data-analysis-for-research-and-education). To obtain access to the service, please contact us through our [helpdesk](mailto:info@surfsara.nl).

This user guide will assume you will have obtained access to a deployed Jupyter notebook environment, and will explain how to manage users and data in the environment.

## A Jupyter environment
When an environment has been created for you, you will be provided with the following information:

* JupyterHub URL: `https://jupyter.something.sda-dev-projects.nl`
* User management API URL: `https://api.something.sda-dev-projects.nl`
* User management API-key: \*
* User management web portal URL: `https://portal.something.sda-dev-projects.nl`
* User management web portal administrator username: \*
* User management web portal administrator password: \*
* Shared data storage URL: `https://data.something.sda-dev-projects.nl`
* Shared data storage access key: \*
* Shared data storage secret key: \*
* Shared data upload username: \*
* Shared data upload password: \*

The remainder of this guide will assume you will substitute `something` with the name of environment in the URLs above.

## User management
SURFsara's Jupyter notebook service offers two ways of managing users:
* The user management web portal
* The user management HTTP API

Information on how to manage users for your environment through the web portal can be found in the [user management guide](USERMANAGEMENT.md).

The HTTP API allows for control over user accounts through the use of scripting, allowing for the automated creation of a list of users, for example.
For instructions on using the API, see the [API documentation](USERMANAGEMENT-API.md).

## Data management & sharing
Instructions on how to manage and share data and notebooks through nbgitpuller or the shared data storage can be found in the [data management & sharing guide](SHARING-DATA.md).

## Using the environment
Instructions on using the Jupyter notebook environment can be found in the [usage documentation](USAGE.md).
