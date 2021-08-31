# Lazy Makefile that just installs script to somewhere in $PATH

SCRIPT_DIR=/${HOME}/.local/bin

install:
	install stock-ticker.py ${SCRIPT_DIR}/stock-ticker.py

uninstall:
	rm ${SCRIPT_DIR}/stock-ticker.py
