- [About](#org83bf643)
- [Setup](#org69ae026)
- [Development](#orga4c2788)

    <!-- This file is generated automatically from metadata -->
    <!-- File edits may be overwritten! -->


<a id="org83bf643"></a>

# About

```markdown
- ROS Package Names:
  - weigher
  - weigher_interfaces
- ROS Distribution: humble
- Description: ROS 2 weigh scale interface.
- Version: 0.1.0
- Release Date: 2023-02-07
- Creation Date: 2022-12-14
- License: BSD-3-Clause
- URL: https://github.com/janelia-ros/weigher_ros
- Author: Peter Polidoro
- Email: peter@polidoro.io
- Copyright: 2023 Howard Hughes Medical Institute
- References:
  - https://github.com/janelia-pypi/loadstar_sensors_interface_python
- Python Dependency List: loadstar_sensors_interface
```


<a id="org69ae026"></a>

# Setup


<a id="orga4c2788"></a>

# Development


## metadata


### Install Guix

[Install Guix](https://guix.gnu.org/manual/en/html_node/Binary-Installation.html)


### Clone Repository

```sh
git clone git@github.com:janelia-ros/weigher_ros.git
cd weigher_ros
```


### Edit metadata.org

```sh
make -f .metadata/Makefile metadata-edits
```


### Tangle metadata.org

```sh
make -f .metadata/Makefile metadata
```


## Docker


### Install Docker

<https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository>


### Run Docker container

```sh
make -f .metadata/Makefile docker-container
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
python3 -m venv .venv
touch .venv/COLCON_IGNORE
source .venv/bin/activate
pip install -r src/weigher_ros/requirements.txt
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