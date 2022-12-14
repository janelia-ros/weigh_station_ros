# This file is generated automatically from .metadata.org
# File edits may be overwritten!

.PHONY: upload
upload: metadata package twine add clean

GUIX-SHELL = guix time-machine -C .channels.scm -- shell --pure --check -m .manifest.scm
GUIX-CONTAINER = guix time-machine -C .channels.scm -- shell -m .manifest.scm --container
GUIX-CONTAINER-GUI = $(GUIX-CONTAINER) -E "^DISPLAY$$" -E "^XAUTHORITY$$" --expose="$$XAUTHORITY" --expose=/tmp/.X11-unix/ --expose=$$HOME/.Xauthority --expose=/etc/machine-id

.PHONY: shell
shell:
	$(GUIX-SHELL)

.PHONY: container
container:
	$(GUIX-CONTAINER)

.PHONY: metadata-edits
metadata-edits:
	$(GUIX-CONTAINER-GUI) -- sh -c "emacs -q --no-site-file --no-site-lisp --no-splash -l .init.el --file .metadata.org"

.PHONY: metadata
metadata:
	$(GUIX-CONTAINER) -- sh -c "emacs --batch -Q  -l .init.el --eval '(process-org \".metadata.org\")'"
