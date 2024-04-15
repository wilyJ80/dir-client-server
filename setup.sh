#!/bin/bash

check_installed() {
	local PACKAGE_NAME=$1

	if ! dpkg -l | grep -q "$PACKAGE_NAME"; then
		echo "Package $PACKAGE_NAME is not installed. Exiting the script."
		return
	else
		echo "Package $PACKAGE_NAME found. Continuing setup..."
	fi
}

if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
	cat <<- EOF

	***************************
	*    This script is not   *
	*    being sourced. venv  *
	*    will not enter       *
	*    correctly. Please,   *
	*    run it as            *
	*                         *
	*    source ./setup.sh    *
	*                         *
	*    instead of           *
	*                         *
	*    ./setup.sh           *
	*                         *
	***************************

	EOF
	exit 1
else
	echo -e "Script is being sourced. Continuing...\n"
	check_installed "python3"
	check_installed "python3-venv"
	check_installed "python3-pip"

fi

read -p "This script will activate a new venv, pip install necessary dependencies, setup necessary folders and start the nameserver. Continue? [y/n] " confirm

if [[ $confirm == "n" ]]; then
	return
fi

echo "Creating virtual environment..."
python3 -m venv venv
echo "Activating virtual environment..."
source venv/bin/activate

echo -e "\nPython venv configured successfully.\n"
echo -e "Use the deactivate command to leave it.\n"

pip install Pyro5

mkdir -p source-folder
mkdir -p mirror-folder

echo -e "Project folders setup for client-server mirroring.\n"

echo -e "Starting nameserver...\n"
pyro5-ns
