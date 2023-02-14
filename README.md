- [About](#org5f3042e)
- [Setup](#org6a95676)
- [Development](#org7728e81)

    <!-- This file is generated automatically from metadata -->
    <!-- File edits may be overwritten! -->


<a id="org5f3042e"></a>

# About

```markdown
- ROS Package Names:
  - weigher
  - weigher_interfaces
- ROS Distribution: humble
- Description: ROS 2 weigh scale interface.
- Version: 0.1.0
- Release Date: 2023-02-14
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


<a id="org6a95676"></a>

# Setup


<a id="org7728e81"></a>

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
    make -f src/weigher_ros/.metadata/Makefile virtualenv
    ```


### Build

1.  Source the ROS underlay and activate the Python virtualenv and build ROS packages

    ```sh
    # build may finish with stderr warnings about deprecated setup.py install
    # if using Python 3.10 or higher
    cd ~/ros2_ws && \
    make -f src/weigher_ros/.metadata/Makefile ros-build
    ```


### Run

1.  Source the ROS underlay and overlay and activate Python virtualenv and run the weigher node

    ```sh
    source ~/ros2_ws/src/weigher_ros/.metadata/setup.bash && \
    source ~/ros2_ws/install/setup.bash && \
    ros2 run weigher weigher_node --ros-args -p serial_port:=/dev/ttyUSB0
    ```

2.  Echo the weigher topic

    ```sh
    # Open a new termial
    source ~/ros2_ws/install/setup.bash && \
    ros2 topic echo /weight
    ```


## Host Setup


### Raspberry Pi

1.  Setup Raspberry Pi

    <https://github.com/janelia-experimental-technology/raspberrypi_setup>
    
    -   username: weigher
    -   hostname: weigher

2.  SSH into Raspberry Pi

    ```sh
    ssh weigher@weigher.local
    ```

3.  Web Console

    <https://weigher.lan:9090/>

4.  Clone Repository

    ```sh
    cd ~ && \
    git clone git@github.com:janelia-ros/weigher_ros.git
    ```

5.  Add deploy ssh key to Github Repository

    ```sh
    cat .ssh/id_ed25519.pub
    ```

6.  Install make for metadata commands

    ```sh
    sudo apt install make
    ```

7.  Host Setup

    ```sh
    cd ~/weigher_ros && \
    make -f .metadata/Makefile host-setup
    sudo reboot
    ```

8.  Check systemd service

    ```sh
    systemctl status weigher-attached@00.service
    systemd-analyze plot > boot_analysis.svg
    ```