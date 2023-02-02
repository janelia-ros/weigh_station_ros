- [About](#orgbe5ce7c)
- [Setup](#org5f29b58)
- [Development](#org616b87f)

    <!-- This file is generated automatically from metadata -->
    <!-- File edits may be overwritten! -->


<a id="orgbe5ce7c"></a>

# About

```markdown
- ROS Package Names:
  - weigher
  - weigher_interfaces
- ROS Distribution: humble
- Description: ROS 2 weigh scale interface.
- Version: 0.1.0
- Release Date: 2023-02-02
- Creation Date: 2022-12-14
- License: BSD-3-Clause
- URL: https://github.com/janelia-ros/weigher_ros
- Author: Peter Polidoro
- Email: peter@polidoro.io
- Copyright: 2023 Howard Hughes Medical Institute
- References:
  - https://github.com/janelia-pypi/loadstar_sensors_interface_python
```


<a id="org5f29b58"></a>

# Setup


<a id="org616b87f"></a>

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
mkdir -p ~/ros2_ws/src && cd ~/ros2_ws/src
git clone git@github.com:janelia-ros/weigher_ros.git
```


### Setup Python virtualenv

```sh
sudo apt install python3-venv
cd ~/ros2_ws
python3 -m venv venv
touch venv/COLCON_IGNORE
```


### Source the ROS underlay and activate the Python virtualenv

```sh
cd ~/ros2_ws
source src/weigher_ros/.metadata/setup.bash
```


### Build ROS packages

```sh
cd ~/ros2_ws
colcon build --symlink-install
```


### Source the ROS overlay

```sh
cd ~/ros2_ws
source install/setup.bash
```


### Run the weigher node

```sh
ros2 run weigher weigher_node
```


### Echo the weigher topic

Open a new termial

```sh
ros2 topic echo /weight
```