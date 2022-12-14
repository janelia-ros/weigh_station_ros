- [About](#org858a814)
- [Setup](#orgf4bdd39)
- [Development](#orgeae2bb2)

    <!-- This file is generated automatically from .metadata.org -->
    <!-- File edits may be overwritten! -->


<a id="org858a814"></a>

# About

```markdown
- Name: weigh_station
- Description: Rat City weigh station ROS 2 code for the Janelia Gowan Lab.
- Version: 0.1.0
- Release Date: 2022-12-14
- Creation Date: 2022-12-14
- License: BSD-3-Clause
- URL: https://github.com/janelia-ros/weigh_station_ros
- Author: Peter Polidoro
- Email: peter@polidoro.io
- Copyright: 2022 Howard Hughes Medical Institute
- References:
  - https://github.com/janelia-pypi/loadstar_sensors_interface_python
```


<a id="orgf4bdd39"></a>

# Setup


<a id="orgeae2bb2"></a>

# Development

1.  Install Guix.

[Install Guix](https://guix.gnu.org/manual/en/html_node/Binary-Installation.html)

1.  Clone repository.

```sh
git clone https://github.com/janelia-ros/weigh_station_ros
cd weigh_station_ros
```

```sh
make metadata-edits
```

1.  Modify project specific variables.

```sh
make metadata
```