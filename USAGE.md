# Usage instructions
This page will provide instructions on how to use the environment as an end-user.

## Starting a notebook environment
The hub (or JupyterHub) is the entry point for your users and is located at `https://jupyter.something.k8s.surfsara.nl`. After logging in with a valid username and password, a notebook environment will start in a container. The initial start up process may take up to two minutes.

After a container has started, the Jupyter notebook environment will display a file browser showing you all files and directories in your **home directory**. Any changes you make in your home directory will be saved and available in future logins. This includes changes to notebooks in your home directory, as well as modifications to any other data.

That being said, we cannot guarantee the integrity of the data in your notebook environment, and you should not rely on the notebook's storage medium. Important data and work should be saved to another system by downloading it from the environment.

## Memory usage
In addition, notebooks are provisioned with the [nbresuse](https://github.com/yuvipanda/nbresuse) Jupyter extension, which will show the **total memory usage of the container** in the top-right corner of each notebook, as well as the **total memory available to the container**. When the memory usage exceeds the available memory the container may be deleted by the environment, so it is important to keep the memory usage below the available memory limit.

## Notebook images
Each notebook environment will have the same libraries and tools installed. We offer a **pre-configured** notebook environment based on Docker images from [jupyter-docker-stacks](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html). These images contain the popular data science packages. For more information, please see the [Docker stacks documentation](https://jupyter-docker-stacks.readthedocs.io/en/latest/using/selecting.html).

Additional software packages, kernels and Jupyter extensions can be installed if required.

The notebook image comes with **nbgitpuller** pre-installed, which allows you to share data with your users via a link. For more information, see the documentation page about [sharing data](SHARING.md).

## Downloading user data
Users can download data from their home directories using the instructions found in the [downloading data section](DOWNLOAD-USER-DATA.md).

## Installing packages
Although the installation of new packages and extensions is possible through tools like conda and pip, this is not supported in the SURFsara notebook environments. SURFsara does not accept liability for any errors and/or data loss  arising due to additionally installed, or changed software.

## Troubleshooting
Troubleshooting tips can be found on the [troubleshooting page](TROUBLESHOOTING.md).
