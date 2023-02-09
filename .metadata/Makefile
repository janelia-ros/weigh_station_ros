# This file is generated automatically from metadata
# File edits may be overwritten!

.PHONY: upload
upload: metadata package twine add clean

MAKEFILE_PATH := $(abspath $(lastword $(MAKEFILE_LIST)))
MAKEFILE_DIR := $(notdir $(patsubst %/,%,$(dir $(MAKEFILE_PATH))))
GUIX-TIME-MACHINE = guix time-machine -C $(MAKEFILE_DIR)/guix/channels.scm
GUIX-SHELL = $(GUIX-TIME-MACHINE) -- shell -m $(MAKEFILE_DIR)/guix/manifest.scm
CONTAINER = --container --preserve='^DISPLAY$$' --preserve='^TERM$$'
GUIX-CONTAINER = $(GUIX-SHELL) $(CONTAINER)
VENV-SHELL = rm -rf .venv; mkdir .venv; python3 -m venv .venv; source .venv/bin/activate
DOCKER-IMAGE = docker build -f $(MAKEFILE_DIR)/docker/Dockerfile -t weigher_ros .
DOCKER-IMAGE-DEBUG = docker build -f $(MAKEFILE_DIR)/docker/Dockerfile --no-cache --progress=plain -t weigher_ros .
DOCKER-CONTAINER = $(DOCKER-IMAGE); docker run -it weigher_ros

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

.PHONY: docker-image-debug
docker-image-debug:
	$(DOCKER-IMAGE-DEBUG)

.PHONY: docker-container
docker-container:
	$(DOCKER-CONTAINER)

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
