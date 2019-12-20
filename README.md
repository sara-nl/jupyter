<img height="75px" src="images/surfsara.png"/>
<hr/>

# SURFsara Jupyter notebook administration guide
**This repository provides a user guide for administrators of SURFsara [Jupyter notebook service](https://www.surf.nl/en/jupyter-notebook-accessible-and-interactive-data-analysis-for-research-and-education)**.

For more information about this service, please see the overview page at the [SURFsara website](https://www.surf.nl/en/jupyter-notebook-accessible-and-interactive-data-analysis-for-research-and-education). To obtain access to the service, please contact us through our [helpdesk](mailto:info@surfsara.nl).

This user guide will assume you will have obtained access to a deployed Jupyter notebook environment, and will explain how to manage users and data in the environment.

## Jupyter environment components
A Jupyter environment consists of a number of components:

1. A JupyterHub interface
1. A customizable Docker notebook image
1. A web portal and an API for managing users
1. Persistent user storage
1. A persistent, shared **read-only** data storage (optional)

The JupyterHub interface is the entry point for end-users. By logging in, the Hub will start an isolated notebook container based on a Docker notebook image. This image can be customized by installing additional kernels, libraries, extensions and other software. A web portal is available for easy management of users, and a user management API for automated control through scripting.

Each user's notebook environment has its own persistent storage attached. Changes made to the data by the user will be saved between consecutive logins to the environment. In addition, a shared read-only data storage is available for hosting large data sets. Each user has read-only access to this data store in their own container.

The remainder of this page provides instructions on how to create a new Jupyter deployment, as well as links to a number of pages describing how to use the environment, and how to manage users and data.

## Creating a new Jupyter environment
To create an Jupyter environment, SURFsara requires some information about the environment's hardware capacity and the software installation.  This information is used to right-size the Jupyter cluster, prepare the (shared) storage and install the required software packages. The below information should be provided:

* The start and end date of the environment
* The number of users
* The capacity of the notebook pods. Three 'sizes' are available:
    * **Light**: 1 vcore, 3 GB RAM
    * **Medium**: 2 vcores, 6 GB RAM
    * **Heavy**: 4 vcores, 12 GB RAM
* The per-user storage, in GB
* The amount of shared storage, in GB
* Additional software to be installed, including:
    * Python/R/other packages
    * Additional kernels
    * Jupyter extensions
    * Other software
* A short name for the course that can be used as part of the URL. For example, for a course 'Machine Learning 1' this name can be `ml1`, which would result in the following URL to log in to the Hub: `https://jupyter.ml1.sda-projects.nl`.

## A Jupyter environment
When an environment has been created for you, you will be provided with the following information:

* JupyterHub URL: `https://jupyter.something.sda-projects.nl`
* User management API URL: `https://api.something.sda-projects.nl`
* User management API-key: \*
* User management web portal URL: `https://portal.something.sda-projects.nl`
* User management web portal administrator username: \*
* User management web portal administrator password: \*
* Shared data storage URL: `https://data.something.sda-projects.nl`
* Shared data storage access key: \*
* Shared data storage secret key: \*

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
Instructions on using the Jupyter notebook environment can be found in the [usage documentation](USAGE.md). For troubleshooting tips, see the documentation page [here](TROUBLESHOOTING.md).
