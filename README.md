- [About](#org9206ddb)
- [Setup](#org49eab66)
- [Development](#orgaae5b29)

    <!-- This file is generated automatically from .metadata.org -->
    <!-- File edits may be overwritten! -->


<a id="org9206ddb"></a>

# About

```markdown
- Name: weigher
- Description: Rat City weigher ROS 2 code for the Janelia Gowan Lab.
- Version: 0.1.0
- Release Date: 2022-12-14
- Creation Date: 2022-12-14
- License: BSD-3-Clause
- URL: https://github.com/janelia-ros/weigher_ros
- Author: Peter Polidoro
- Email: peter@polidoro.io
- Copyright: 2022 Howard Hughes Medical Institute
- References:
  - https://github.com/janelia-pypi/loadstar_sensors_interface_python
```


<a id="org49eab66"></a>

# Setup


<a id="orgaae5b29"></a>

# Development

1.  Install Guix.

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