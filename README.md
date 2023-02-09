- [About](#org19a58a4)
- [Setup](#org828c9d6)
- [Development](#org6d2bf40)

    <!-- This file is generated automatically from metadata -->
    <!-- File edits may be overwritten! -->


<a id="org19a58a4"></a>

# About

```markdown
- ROS Package Names:
  - weigher
  - weigher_interfaces
- ROS Distribution: humble
- Description: ROS 2 weigh scale interface.
- Version: 0.1.0
- Release Date: 2023-02-09
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


<a id="org828c9d6"></a>

# Setup


<a id="org6d2bf40"></a>

# Development


## metadata


### Install Guix

[Install Guix](https://guix.gnu.org/manual/en/html_node/Binary-Installation.html)


### Clone Repository

```sh
git clone git@github.com:janelia-ros/weigher_ros.git && \
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


### Setup

1.  Install ROS

    ```text
    https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html
    ```

2.  Create ROS Workspace and clone this repository

    ```sh
    mkdir -p ~/ros2_ws/src && \
    cd ~/ros2_ws/src && \
    git clone git@github.com:janelia-ros/weigher_ros.git
    ```

3.  Setup Python virtualenv

    ```sh
    sudo apt install python3-venv
    cd ~/ros2_ws
    python3 -m venv .venv
    touch .venv/COLCON_IGNORE
    source .venv/bin/activate
    pip install -r src/weigher_ros/requirements.txt
    ```


### Build

1.  Source the ROS underlay and activate the Python virtualenv and build ROS packages

    ```sh
    source ~/ros2_ws/src/weigher_ros/.metadata/setup.bash && \
    colcon build --symlink-install
    ```


### Run

1.  Source the ROS underlay and overlay and activate Python virtualenv and run the weigher node

    ```sh
    source ~/ros2_ws/src/weigher_ros/.metadata/setup.bash && \
    source ~/ros2_ws/install/setup.bash && \
    ros2 run weigher weigher_node
    ```

2.  Echo the weigher topic

    ```sh
    # Open a new termial
    source ~/ros2_ws/install/setup.bash && \
    ros2 topic echo /weight
    ```