#!/bin/sh

# List of supported Linux distros by package managers
# This is a list of ids as gotten from cat /etc/os-release
APT="Raspbian Ubuntu Debian Kali Pop"
DNF="Fedora RHEL"
PACMAN="Manjaro ArchLinux"
ZYPPER="OpenSUSE"

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
        for DIST in $APT
        do
            if lsb_release -id | grep "$DIST"; then
                echo Ubuntu
                return 2
            fi
        done

        for DIST in $DNF
        do
            if cat /etc/os-release | grep "$DIST"; then
                return 3
            fi
        done

        for DIST in $PACMAN
        do
            if cat /etc/os-release | grep "$DIST"; then
                return 4
            fi
        done

        for DIST in $ZYPPER
        do
            if cat /etc/os-release | grep "$DIST"; then
                return 5
            fi
        done
}

# Check if package is installed on debian-based systems using dpkg.
check_pac_debian()
{
    PKG=$1
    STATUS=dpkg-query -W --showformat='${db:Status-Status}' "$PKG" 2>&1
    if $STATUS | grep not-installed; then
        return 1
    else
        return 0
    fi
}

# Detect Linux distro and download Python using a corresponding package manager.
install_py_lin()
{
    if { check_pac python || check_pac python3; } && { check_pac pip3 || check_pac pip; }; then
        echo "Python jest juz zainstalowany na tym urzadzeniu. Pomijanie instalacji..."
    else
        DISTRO_NUM=check_distro
        if [[ $DISTRO_NUM == 2 ]]; then
            sudo apt update
            # software-properties-common is needed to add a repository key
            if check_pac_debian software-properties-common; then
                sudo apt install software-properties-common
            fi
            sudo add-apt-repository ppa:deadsnakes/ppa
            sudo apt update
            sudo apt install -y python3.9
            if ! check_pac pip3; then
                sudo apt install python3-pip -y
                if ! check_pac pip3; then
                    return 1
                fi
            fi
        elif [[ $DISTRO_NUM == 3 ]]; then
            sudo dnf -y upgrade
            sudo -y dnf install python
        elif [[ $DISTRO_NUM == 4 ]]; then
            sudo pacman -Syu --noconfirm
            sudo pacman -S python --noconfirm
        elif [[ $DISTRO_NUM == 5 ]]; then
            sudo zypper install python -y
        fi
    fi

    # I don't know how to check if the package is already installed by the package manager
    # on other systems, so I only check for it on Ubuntu. People on other OS'es will have a
    # less optimized installation script.
    if [[ $DISTRO_NUM == 2 ]]; then
        sudo apt install -y python3-tk python3-pil python3-pil.imagetk
    elif [[ $DISTRO_NUM == 3 ]]; then
        sudo -y dnf install python3-tkinter
    elif [[ $DISTRO_NUM == 4 ]]; then
        sudo pacman -S tk python-pillow --noconfirm
    elif [[ $DISTRO_NUM == 5 ]]; then
        sudo zypper install python-tk python-Pillow -y
    fi

    if  check_pac python || check_pac python3; then
        return 0
    else
        return 1
    fi
}

if echo $(uname) | grep Darwin; then
    if brew -v 2>/dev/null; then
        brew install python3.9
    else
        echo "Zainstaluj Homebrew zanim rozpoczniesz instalacje tego programu." >&2
        exit 1
    fi
elif echo $(uname) | grep Linux; then
    if install_py_lin; then
        echo "Instalacja Python 3.9 zakonczona."
    else
        echo "Instalacja interpretera Python z powodow blizej nieokreslonych nie powiodla sie." >&2
        echo "Prosze zainstalowac interpreter Python 3.9 manualnie." >&2
        exit 1
    fi
else
    echo "Ten system operacyjny nie jest wspierany przez instalator. Zainstaluj interpreter Python i biblioteki manualnie." >&2
    exit 1
fi

pip3 install -r required.txt
./genealogy.py
