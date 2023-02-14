# This file is generated automatically from metadata
# File edits may be overwritten!

MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
MAKEFILE_DIR := $(notdir $(patsubst %/,%,$(dir $(MAKEFILE_PATH))))
GUIX-TIME-MACHINE = guix time-machine -C $(MAKEFILE_DIR)/guix/channels.scm
GUIX-SHELL = $(GUIX-TIME-MACHINE) -- shell -m $(MAKEFILE_DIR)/guix/manifest.scm
CONTAINER = --container --preserve='^DISPLAY$$' --preserve='^TERM$$'
GUIX-CONTAINER = $(GUIX-SHELL) $(CONTAINER)
VENV-SHELL = rm -rf .venv; mkdir .venv; python3 -m venv .venv; source .venv/bin/activate
DOCKER-IMAGE = docker build -f $(MAKEFILE_DIR)/docker/Dockerfile -t weigher:latest .
DOCKER-IMAGE-DEBUG = docker build -f $(MAKEFILE_DIR)/docker/Dockerfile --no-cache --progress=plain -t weigher:latest .
DOCKER-CONTAINER = docker run -it --net=host --pid=host weigher:latest

.PHONY: guix-container
guix-container:
	$(GUIX-CONTAINER)

.PHONY: requirements.txt
requirements.txt:
	$(GUIX-CONTAINER) -- $(VENV-SHELL) &&\
	pip install loadstar_sensors_interface &&\
	pip freeze --local > requirements.txt &&\
	deactivate &&\
	rm -rf .venv

.PHONY: docker-image
docker-image:
	$(DOCKER-IMAGE)

.PHONY: docker-image-debug
docker-image-debug:
	$(DOCKER-IMAGE-DEBUG)

.PHONY: docker-container
docker-container:
	$(DOCKER-CONTAINER) bash

.PHONY: metadata-edits
metadata-edits:
	$(GUIX-CONTAINER) -- sh -c "emacs -q --no-site-file --no-site-lisp --no-splash -l $(MAKEFILE_DIR)/emacs/init.el --file $(MAKEFILE_DIR)/metadata.org"

.PHONY: metadata
metadata: requirements.txt
	$(GUIX-CONTAINER) -- sh -c "emacs --batch -Q  -l $(MAKEFILE_DIR)/emacs/init.el --eval '(process-org \"$(MAKEFILE_DIR)/metadata.org\")'"

.PHONY: virtualenv
virtualenv:
	rm -rf .venv;\
	python3 -m venv .venv;\
	touch .venv/COLCON_IGNORE;\
	source .venv/bin/activate;\
	pip install -r src/weigher_ros/requirements.txt

.PHONY: ros-build
ros-build:
	source src/weigher_ros/.metadata/setup.bash;\
	colcon build --symlink-install

.PHONY: host-apt-dependencies
host-apt-dependencies:
	sudo apt install -y python3-filelock python3-docker python3-click;\

.PHONY: host-setup
host-setup: host-apt-dependencies
	python3 .metadata/host/host_setup.py install;\
	sudo chmod +x /usr/local/bin/find_device_then_run.py;\
	sudo chmod +x /usr/local/bin/echo-weight;\

PORT = /dev/ttyUSB0
DOCKER-CONTAINER-PORT = docker run -it --net=host --pid=host --device=$(PORT) weigher:latest

.PHONY: docker-container-port
docker-container-port:
	$(DOCKER-CONTAINER-PORT) bash

.PHONY: docker-publish-weight
docker-publish-weight:
	$(DOCKER-CONTAINER-PORT) ros2 launch weigher weigher_launch.py

.PHONY: docker-echo-weight
docker-echo-weight:
	$(DOCKER-CONTAINER) ros2 topic echo /weight
