- [About](#org720370e)
- [Setup](#org5b272ee)
- [Development](#org2483279)

    <!-- This file is generated automatically from metadata -->
    <!-- File edits may be overwritten! -->


<a id="org720370e"></a>

# About

```markdown
- ROS Package Names:
  - weigher
  - weigher_interfaces
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


<a id="org5b272ee"></a>

# Setup


<a id="org2483279"></a>

# Development


## metadata


### Install Guix

[Install Guix](https://guix.gnu.org/manual/en/html_node/Binary-Installation.html)


### Clone Repository

```sh
git clone git@github.com:janelia-ros/weigher_ros.git
cd weigher_ros
```


### Make alias

```sh
source .metadata/.alias
```


### Edit metadata.org

```sh
,make metadata-edits
```


### Tangle metadata.org

```sh
,make metadata
```


## Docker


### Install Docker

<https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository>


### Run Docker container

```sh
make, docker-container
```


## Ubuntu


### Install ROS

```text
https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html
```


### Configure Environment

```text
https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html
```


### Create Workspace

```text
https://docs.ros.org/en/humble/Tutorials/Beginner-Client-Libraries/Creating-A-Workspace/Creating-A-Workspace.html
```


### Clone this repository into workspace

```sh
cd ~/ros2_ws/src
git clone git@github.com:janelia-ros/weigher_ros.git
```


### Source the ROS underlay

```sh
cd ~/ros2_ws
source src/weigher_ros/.metadata/setup.bash
```


### Build ROS packages

```sh
cd ~/ros2_ws
colcon build --symlink-install
```