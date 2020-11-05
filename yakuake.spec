#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x92220328C632316E (hein@kde.org)
#
Name     : yakuake
Version  : 3.0.5
Release  : 6
URL      : https://download.kde.org/stable/yakuake/3.0.5/src/yakuake-3.0.5.tar.xz
Source0  : https://download.kde.org/stable/yakuake/3.0.5/src/yakuake-3.0.5.tar.xz
Source1  : https://download.kde.org/stable/yakuake/3.0.5/src/yakuake-3.0.5.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-2.0
Requires: yakuake-bin = %{version}-%{release}
Requires: yakuake-data = %{version}-%{release}
Requires: yakuake-license = %{version}-%{release}
Requires: yakuake-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kglobalaccel-dev
BuildRequires : ki18n-dev
BuildRequires : knotifyconfig-dev
BuildRequires : kwayland-dev
BuildRequires : libX11-dev libICE-dev libSM-dev libXau-dev libXcomposite-dev libXcursor-dev libXdamage-dev libXdmcp-dev libXext-dev libXfixes-dev libXft-dev libXi-dev libXinerama-dev libXi-dev libXmu-dev libXpm-dev libXrandr-dev libXrender-dev libXres-dev libXScrnSaver-dev libXt-dev libXtst-dev libXv-dev libXxf86misc-dev libXxf86vm-dev
BuildRequires : qtbase-dev mesa-dev

%description
Yakuake is a drop-down terminal emulator based on KDE Konsole technology.
It's a KDE Extragear application released under GPL v2, GPL v3 or any later
version accepted by the membership of KDE e.V.

%package bin
Summary: bin components for the yakuake package.
Group: Binaries
Requires: yakuake-data = %{version}-%{release}
Requires: yakuake-license = %{version}-%{release}

%description bin
bin components for the yakuake package.


%package data
Summary: data components for the yakuake package.
Group: Data

%description data
data components for the yakuake package.


%package license
Summary: license components for the yakuake package.
Group: Default

%description license
license components for the yakuake package.


%package locales
Summary: locales components for the yakuake package.
Group: Default

%description locales
locales components for the yakuake package.


%prep
%setup -q -n yakuake-3.0.5
cd %{_builddir}/yakuake-3.0.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604542723
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1604542723
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/yakuake
cp %{_builddir}/yakuake-3.0.5/COPYING %{buildroot}/usr/share/package-licenses/yakuake/c4c1107be4f6cbb7629e3b3edfbf12cc918cddc1
cp %{_builddir}/yakuake-3.0.5/COPYING.DOC %{buildroot}/usr/share/package-licenses/yakuake/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
pushd clr-build
%make_install
popd
%find_lang yakuake

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/yakuake

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.yakuake.desktop
/usr/share/dbus-1/services/org.kde.yakuake.service
/usr/share/icons/hicolor/128x128/apps/yakuake.png
/usr/share/icons/hicolor/16x16/apps/yakuake.png
/usr/share/icons/hicolor/22x22/apps/yakuake.png
/usr/share/icons/hicolor/256x256/apps/yakuake.png
/usr/share/icons/hicolor/32x32/apps/yakuake.png
/usr/share/icons/hicolor/48x48/apps/yakuake.png
/usr/share/icons/hicolor/64x64/apps/yakuake.png
/usr/share/knotifications5/yakuake.notifyrc
/usr/share/metainfo/org.kde.yakuake.appdata.xml
/usr/share/xdg/yakuake.knsrc
/usr/share/yakuake/skins/README
/usr/share/yakuake/skins/default/icon.png
/usr/share/yakuake/skins/default/tabs.skin
/usr/share/yakuake/skins/default/tabs/add_down.png
/usr/share/yakuake/skins/default/tabs/add_down.svg
/usr/share/yakuake/skins/default/tabs/add_up.png
/usr/share/yakuake/skins/default/tabs/add_up.svg
/usr/share/yakuake/skins/default/tabs/back_image.png
/usr/share/yakuake/skins/default/tabs/back_image.svg
/usr/share/yakuake/skins/default/tabs/close_down.png
/usr/share/yakuake/skins/default/tabs/close_down.svg
/usr/share/yakuake/skins/default/tabs/close_up.png
/usr/share/yakuake/skins/default/tabs/close_up.svg
/usr/share/yakuake/skins/default/tabs/left_corner.png
/usr/share/yakuake/skins/default/tabs/left_corner.svg
/usr/share/yakuake/skins/default/tabs/lock.png
/usr/share/yakuake/skins/default/tabs/lock.svg
/usr/share/yakuake/skins/default/tabs/right_corner.png
/usr/share/yakuake/skins/default/tabs/right_corner.svg
/usr/share/yakuake/skins/default/tabs/selected_back.png
/usr/share/yakuake/skins/default/tabs/selected_back.svg
/usr/share/yakuake/skins/default/tabs/selected_left.png
/usr/share/yakuake/skins/default/tabs/selected_left.svg
/usr/share/yakuake/skins/default/tabs/selected_right.png
/usr/share/yakuake/skins/default/tabs/selected_right.svg
/usr/share/yakuake/skins/default/tabs/separator.png
/usr/share/yakuake/skins/default/tabs/separator.svg
/usr/share/yakuake/skins/default/tabs/unselected_back.png
/usr/share/yakuake/skins/default/tabs/unselected_back.svg
/usr/share/yakuake/skins/default/tabs/unselected_left.png
/usr/share/yakuake/skins/default/tabs/unselected_left.svg
/usr/share/yakuake/skins/default/tabs/unselected_right.png
/usr/share/yakuake/skins/default/tabs/unselected_right.svg
/usr/share/yakuake/skins/default/title.skin
/usr/share/yakuake/skins/default/title/back.png
/usr/share/yakuake/skins/default/title/back.svg
/usr/share/yakuake/skins/default/title/config_down.png
/usr/share/yakuake/skins/default/title/config_down.svg
/usr/share/yakuake/skins/default/title/config_up.png
/usr/share/yakuake/skins/default/title/config_up.svg
/usr/share/yakuake/skins/default/title/focus_down.png
/usr/share/yakuake/skins/default/title/focus_down.svg
/usr/share/yakuake/skins/default/title/focus_over.png
/usr/share/yakuake/skins/default/title/focus_over.svg
/usr/share/yakuake/skins/default/title/focus_up.png
/usr/share/yakuake/skins/default/title/focus_up.svg
/usr/share/yakuake/skins/default/title/left.png
/usr/share/yakuake/skins/default/title/left.svg
/usr/share/yakuake/skins/default/title/quit_down.png
/usr/share/yakuake/skins/default/title/quit_down.svg
/usr/share/yakuake/skins/default/title/quit_up.png
/usr/share/yakuake/skins/default/title/quit_up.svg
/usr/share/yakuake/skins/default/title/right.png
/usr/share/yakuake/skins/default/title/right.svg
/usr/share/yakuake/skins/legacy/icon.png
/usr/share/yakuake/skins/legacy/tabs.skin
/usr/share/yakuake/skins/legacy/tabs/back_image.png
/usr/share/yakuake/skins/legacy/tabs/left_corner.png
/usr/share/yakuake/skins/legacy/tabs/lock.png
/usr/share/yakuake/skins/legacy/tabs/minus_down.png
/usr/share/yakuake/skins/legacy/tabs/minus_over.png
/usr/share/yakuake/skins/legacy/tabs/minus_up.png
/usr/share/yakuake/skins/legacy/tabs/plus_down.png
/usr/share/yakuake/skins/legacy/tabs/plus_over.png
/usr/share/yakuake/skins/legacy/tabs/plus_up.png
/usr/share/yakuake/skins/legacy/tabs/right_corner.png
/usr/share/yakuake/skins/legacy/tabs/selected_back.png
/usr/share/yakuake/skins/legacy/tabs/selected_left.png
/usr/share/yakuake/skins/legacy/tabs/selected_right.png
/usr/share/yakuake/skins/legacy/tabs/separator.png
/usr/share/yakuake/skins/legacy/tabs/unselected_back.png
/usr/share/yakuake/skins/legacy/title.skin
/usr/share/yakuake/skins/legacy/title/back.png
/usr/share/yakuake/skins/legacy/title/config_down.png
/usr/share/yakuake/skins/legacy/title/config_over.png
/usr/share/yakuake/skins/legacy/title/config_up.png
/usr/share/yakuake/skins/legacy/title/focus_down.png
/usr/share/yakuake/skins/legacy/title/focus_over.png
/usr/share/yakuake/skins/legacy/title/focus_up.png
/usr/share/yakuake/skins/legacy/title/left.png
/usr/share/yakuake/skins/legacy/title/quit_down.png
/usr/share/yakuake/skins/legacy/title/quit_over.png
/usr/share/yakuake/skins/legacy/title/quit_up.png
/usr/share/yakuake/skins/legacy/title/right.png
/usr/share/yakuake/skins/plastik_dark/icon.png
/usr/share/yakuake/skins/plastik_dark/tabs.skin
/usr/share/yakuake/skins/plastik_dark/tabs/back_image.png
/usr/share/yakuake/skins/plastik_dark/tabs/left_corner.png
/usr/share/yakuake/skins/plastik_dark/tabs/lock.png
/usr/share/yakuake/skins/plastik_dark/tabs/minus_down.png
/usr/share/yakuake/skins/plastik_dark/tabs/minus_over.png
/usr/share/yakuake/skins/plastik_dark/tabs/minus_up.png
/usr/share/yakuake/skins/plastik_dark/tabs/plus_down.png
/usr/share/yakuake/skins/plastik_dark/tabs/plus_over.png
/usr/share/yakuake/skins/plastik_dark/tabs/plus_up.png
/usr/share/yakuake/skins/plastik_dark/tabs/right_corner.png
/usr/share/yakuake/skins/plastik_dark/tabs/selected_back.png
/usr/share/yakuake/skins/plastik_dark/tabs/selected_left.png
/usr/share/yakuake/skins/plastik_dark/tabs/selected_right.png
/usr/share/yakuake/skins/plastik_dark/tabs/separator.png
/usr/share/yakuake/skins/plastik_dark/tabs/unselected_back.png
/usr/share/yakuake/skins/plastik_dark/title.skin
/usr/share/yakuake/skins/plastik_dark/title/back.png
/usr/share/yakuake/skins/plastik_dark/title/config_down.png
/usr/share/yakuake/skins/plastik_dark/title/config_over.png
/usr/share/yakuake/skins/plastik_dark/title/config_up.png
/usr/share/yakuake/skins/plastik_dark/title/focus_down.png
/usr/share/yakuake/skins/plastik_dark/title/focus_over.png
/usr/share/yakuake/skins/plastik_dark/title/focus_up.png
/usr/share/yakuake/skins/plastik_dark/title/left.png
/usr/share/yakuake/skins/plastik_dark/title/quit_down.png
/usr/share/yakuake/skins/plastik_dark/title/quit_over.png
/usr/share/yakuake/skins/plastik_dark/title/quit_up.png
/usr/share/yakuake/skins/plastik_dark/title/right.png
/usr/share/yakuake/skins/plastik_light/icon.png
/usr/share/yakuake/skins/plastik_light/tabs.skin
/usr/share/yakuake/skins/plastik_light/tabs/back_image.png
/usr/share/yakuake/skins/plastik_light/tabs/left_corner.png
/usr/share/yakuake/skins/plastik_light/tabs/lock.png
/usr/share/yakuake/skins/plastik_light/tabs/minus_down.png
/usr/share/yakuake/skins/plastik_light/tabs/minus_over.png
/usr/share/yakuake/skins/plastik_light/tabs/minus_up.png
/usr/share/yakuake/skins/plastik_light/tabs/plus_down.png
/usr/share/yakuake/skins/plastik_light/tabs/plus_over.png
/usr/share/yakuake/skins/plastik_light/tabs/plus_up.png
/usr/share/yakuake/skins/plastik_light/tabs/right_corner.png
/usr/share/yakuake/skins/plastik_light/tabs/selected_back.png
/usr/share/yakuake/skins/plastik_light/tabs/selected_left.png
/usr/share/yakuake/skins/plastik_light/tabs/selected_right.png
/usr/share/yakuake/skins/plastik_light/tabs/separator.png
/usr/share/yakuake/skins/plastik_light/tabs/unselected_back.png
/usr/share/yakuake/skins/plastik_light/title.skin
/usr/share/yakuake/skins/plastik_light/title/back.png
/usr/share/yakuake/skins/plastik_light/title/config_down.png
/usr/share/yakuake/skins/plastik_light/title/config_over.png
/usr/share/yakuake/skins/plastik_light/title/config_up.png
/usr/share/yakuake/skins/plastik_light/title/focus_down.png
/usr/share/yakuake/skins/plastik_light/title/focus_over.png
/usr/share/yakuake/skins/plastik_light/title/focus_up.png
/usr/share/yakuake/skins/plastik_light/title/left.png
/usr/share/yakuake/skins/plastik_light/title/quit_down.png
/usr/share/yakuake/skins/plastik_light/title/quit_over.png
/usr/share/yakuake/skins/plastik_light/title/quit_up.png
/usr/share/yakuake/skins/plastik_light/title/right.png

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/yakuake/bd75d59f9d7d9731bfabdc48ecd19e704d218e38
/usr/share/package-licenses/yakuake/c4c1107be4f6cbb7629e3b3edfbf12cc918cddc1

%files locales -f yakuake.lang
%defattr(-,root,root,-)

