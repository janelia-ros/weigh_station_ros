- [About](#org21504e9)
- [Setup](#org90999d3)
- [Development](#orge7dc7a8)

    <!-- This file is generated automatically from metadata -->
    <!-- File edits may be overwritten! -->


<a id="org21504e9"></a>

# About

```markdown
- ROS Package Name: weigher
- ROS Distribution: humble
- Description: ROS 2 weigh scale interface.
- Version: 0.1.0
- Release Date: 2023-02-01
- Creation Date: 2022-12-14
- License: BSD-3-Clause
- URL: https://github.com/janelia-ros/weigher_ros
- Author: Peter Polidoro
- Email: peter@polidoro.io
- Copyright: 2023 Howard Hughes Medical Institute
- References:
  - https://github.com/janelia-pypi/loadstar_sensors_interface_python
```


<a id="org90999d3"></a>

# Setup


<a id="orge7dc7a8"></a>

# Development


## Install Guix

[Install Guix](https://guix.gnu.org/manual/en/html_node/Binary-Installation.html)


## Clone Repository

```sh
git clone https://github.com/janelia-ros/weigher_ros
cd weigher_ros
```


## Make alias

```sh
source .metadata/.alias
```


## Edit metadata.org

```sh
,make metadata-edits
```


## Tangle metadata.org

```sh
,make metadata
```


## Install Docker

<https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository>


## Run Docker container

```sh
make, docker-container
```