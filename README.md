- [About](#org2d4e763)
- [Setup](#orge7f4374)
- [Development](#orgbb43f0e)

    <!-- This file is generated automatically from .metadata.org -->
    <!-- File edits may be overwritten! -->


<a id="org2d4e763"></a>

# About

```markdown
- Name: weigher
- Description: ROS 2 weigh scale interface.
- Version: 0.1.0
- Release Date: 2023-01-09
- Creation Date: 2022-12-14
- License: BSD-3-Clause
- URL: https://github.com/janelia-ros/weigher_ros
- Author: Peter Polidoro
- Email: peter@polidoro.io
- Copyright: 2023 Howard Hughes Medical Institute
- References:
  - https://github.com/janelia-pypi/loadstar_sensors_interface_python
```


<a id="orge7f4374"></a>

# Setup


<a id="orgbb43f0e"></a>

# Development

1.  Install Docker.
    
    <https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository>

2.  Install Guix.

[Install Guix](https://guix.gnu.org/manual/en/html_node/Binary-Installation.html)

1.  Clone repository.

```sh
git clone https://github.com/janelia-ros/weigher_ros
cd weigher_ros
```

```sh
make metadata-edits
```

1.  Modify project specific variables.

```sh
make metadata
```