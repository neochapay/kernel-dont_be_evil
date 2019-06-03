Name:       kernel-dont_be_evil
Summary:    Linux kernel for PinePhone64
Version:    5.1
Release:    0
Group:      System/Kernel
License:    GPLv2
URL:        https://github.com/neochapay/kernel-dont_be_evil
Source0:    %{name}-%{version}.tar.bz2
Source1:    dont_be_evil.conf
BuildRequires: pkgconfig(ncurses)
BuildRequires: flex
BuildRequires: bison

%description
This package contains the config files specifided for
PinePhone64.

%package modules
Summary: modules for linux kernel for PinePhone64
Group:   System/Kernel

%description modules
%{Summary}

%prep
%setup -q -n %{name}-%{version}/linux
cp %{SOURCE1} .config

%build
export ARCH=arm64
export LOCALVERSION=-nemo
make clean
make oldconfig
make Image modules dtbs

%install
mkdir -p $RPM_BUILD_ROOT/boot
cp arch/arm64/boot/Image $RPM_BUILD_ROOT/boot/
cp arch/arm64/boot/dts/allwinner/sun50i-a64-dontbeevil.dtb $RPM_BUILD_ROOT/boot/
cp arch/arm64/boot/dts/allwinner/sun50i-a64-dontbeevil.dts $RPM_BUILD_ROOT/boot/
make modules_install INSTALL_MOD_PATH=$RPM_BUILD_ROOT

%files
/boot/

%files modules
/lib/modules
