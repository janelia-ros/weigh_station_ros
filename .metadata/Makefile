# This file is generated automatically from metadata.org
# File edits may be overwritten!

.PHONY: upload
upload: metadata package twine add clean

GUIX-SHELL = guix time-machine -C guix/channels.scm -- shell --pure --check -m guix/manifest.scm
GUIX-CONTAINER = guix time-machine -C guix/channels.scm -- shell -m guix/manifest.scm --container
GUIX-CONTAINER-GUI = $(GUIX-CONTAINER) -E "^DISPLAY$$" -E "^XAUTHORITY$$" --expose="$$XAUTHORITY" --expose=/tmp/.X11-unix/ --expose=$$HOME/.Xauthority --expose=/etc/machine-id

.PHONY: guix-shell
guix-shell:
	$(GUIX-SHELL)

.PHONY: guix-container
guix-container:
	$(GUIX-CONTAINER)

.PHONY: docker-container
docker-container:
	docker pull ros:humble && docker run -it ros:humble

.PHONY: metadata-edits
metadata-edits:
	$(GUIX-CONTAINER-GUI) -- sh -c "emacs -q --no-site-file --no-site-lisp --no-splash -l emacs/init.el --file metadata.org"

.PHONY: metadata
metadata:
	$(GUIX-CONTAINER) -- sh -c "emacs --batch -Q  -l emacs/init.el --eval '(process-org \"metadata.org\")'"
