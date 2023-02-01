- [About](#org6611531)
- [Setup](#org30279ac)
- [Development](#org71241a2)

    <!-- This file is generated automatically from metadata -->
    <!-- File edits may be overwritten! -->


<a id="org6611531"></a>

# About

```markdown
- ROS Package Names:
  - weigher
  - weigher_interface
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


<a id="org30279ac"></a>

# Setup


<a id="org71241a2"></a>

# Development


## metadata


### Install Guix

[Install Guix](https://guix.gnu.org/manual/en/html_node/Binary-Installation.html)


### Clone Repository

```sh
git clone https://github.com/janelia-ros/weigher_ros
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
git clone https://github.com/janelia-ros/weigher_ros
```


### Source the setup files

```sh
source /opt/ros/humble/setup.bash
colcon build --symlink-install
```


### Build ROS packages

```sh
colcon build --symlink-install
```