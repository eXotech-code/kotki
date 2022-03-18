#!/bin/sh

# List of supported Linux distros by package managers
# This is a list of ids as gotten from cat /etc/os-release
APT="raspbian ubuntu debian kali pop"
DNF="fedora rhel"
PACMAN="manjaro archlinux"
ZYPPER="opensuse"

# Detect if package is already installed.
check_pac()
{
    PACKAGENAME=$1
    # Directs the output from sterror to stout and checks if there was a result.
    if hash "$PACKAGENAME" 2>/dev/null; then
        return 0
    else
        return 1
    fi
}

check_distro()
{
        DISTRO_ID=cat /etc/os-release
        for DIST in $APT
        do
            if echo "$DISTRO" | grep "$DIST"; then
                return APT
            fi
        done

        for DIST in $DNF
        do
            if echo "$DISTRO" | grep "$DIST"; then
                return DNF
            fi
        done

        for DIST in $PACMAN
        do
            if echo "$DISTRO" | grep "$DIST"; then
                return PACMAN
            fi
        done

        for DIST in $ZYPPER
        do
            if echo "$DISTRO" | grep "$DIST"; then
                return ZYPPER
            fi
        done
}

# Detect Linux distro and download Python using a corresponding package manager.
install_py_lin()
{
    if check_pac python; then
        echo "Python jest juz zainstalowany na tym urzadzeniu. Pomijanie instalacji..."
    else
        if check_distro = APT; then
            sudo apt update
            # software-properties-common is needed to add a repository key
            PKG=software-properties-common
            STATUS=dpkg-query -W --showformat='${db:Status-Status}' "$PKG" 2>&1
            if [ ! $? = 0 ] || [ ! $STATUS = installed ]; then
                sudo apt install software-properties-common
            fi
            sudo add-apt-repository ppa:deadsnakes/ppa
            sudo apt update
            sudo install python3.9
            if [ check_pac python ]; then
                return 0
            else
                return 1
            fi
        elif check_distro = DNF; then
            sudo dnf upgrade
            sudo dnf install python -y
        elif check_distro = PACMAN; then
            sudo pacman -Syu
            sudo pacman -S python
        elif check_distro = ZYPPER; then
            sudo zypper install python
        fi

        if [ check_pac python ]; then
            return 0
        else
            return 1
        fi
    fi
}

if echo $OSTYPE | grep linux; then
    if install_py_lin; then
        echo "Instalacja Python 3.9 zakonczona."
    else
        echo "Instalacja interpretera Python z powodow blizej nieokreslonych nie powiodla sie." >&2
        echo "Prosze zainstalowac interpreter Python 3.9 manualnie." >&2
        exit 1
    fi

    pip install -r required.txt

elif echo $OSTYPE | grep darwin; then
    if brew -v 2>/dev/null; then
        brew install python3.9
    else
        echo "Zainstaluj Homebrew zanim rozpoczniesz instalacje tego programu." >&2
        exit 1
    fi
else
    echo "Ten system operacyjny nie jest wspierany przez instalator. Zainstaluj interpreter Python i biblioteki manualnie." >&2
    exit 1
fi

pip install -r required.txt
./genealogy.py
