#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v19
# autospec commit: f35655a
#
# Source0 file verified with key 0xBB463350D6EF31EF (heiko@shruuf.de)
#
Name     : yakuake
Version  : 24.08.1
Release  : 19
URL      : https://download.kde.org/stable/release-service/24.08.1/src/yakuake-24.08.1.tar.xz
Source0  : https://download.kde.org/stable/release-service/24.08.1/src/yakuake-24.08.1.tar.xz
Source1  : https://download.kde.org/stable/release-service/24.08.1/src/yakuake-24.08.1.tar.xz.sig
Source2  : BB463350D6EF31EF.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 GPL-2.0 GPL-3.0
Requires: yakuake-bin = %{version}-%{release}
Requires: yakuake-data = %{version}-%{release}
Requires: yakuake-license = %{version}-%{release}
Requires: yakuake-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : kcrash-dev
BuildRequires : kdbusaddons-dev
BuildRequires : kglobalaccel-dev
BuildRequires : ki18n-dev
BuildRequires : kio-dev
BuildRequires : knotifications-dev
BuildRequires : knotifyconfig-dev
BuildRequires : kstatusnotifieritem-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
** What is a Yakuake skin?
A Yakuake skin, at present, is a collection of PNG image files and related
settings that allows modifying the visual appearance of the Yakuake window
frame, the window title bar and the tab bar along with the button controls
on them and the default title bar caption.

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
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) BB463350D6EF31EF' gpg.status
%setup -q -n yakuake-24.08.1
cd %{_builddir}/yakuake-24.08.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1726257020
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1726257020
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/yakuake
cp %{_builddir}/yakuake-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/yakuake/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/yakuake-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/yakuake/3e8971c6c5f16674958913a94a36b1ea7a00ac46 || :
cp %{_builddir}/yakuake-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/yakuake/2123756e0b1fc8243547235a33c0fcabfe3b9a51 || :
cp %{_builddir}/yakuake-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/yakuake/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/yakuake-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/yakuake/7d9831e05094ce723947d729c2a46a09d6e90275 || :
export GOAMD64=v2
GOAMD64=v2
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
/usr/share/knotifications6/yakuake.notifyrc
/usr/share/knsrcfiles/yakuake.knsrc
/usr/share/metainfo/org.kde.yakuake.appdata.xml
/usr/share/yakuake/skins/README
/usr/share/yakuake/skins/default/icon.svg
/usr/share/yakuake/skins/default/tabs.skin
/usr/share/yakuake/skins/default/tabs/add_down.svg
/usr/share/yakuake/skins/default/tabs/add_up.svg
/usr/share/yakuake/skins/default/tabs/back_image.svg
/usr/share/yakuake/skins/default/tabs/close_down.svg
/usr/share/yakuake/skins/default/tabs/close_up.svg
/usr/share/yakuake/skins/default/tabs/left_corner.svg
/usr/share/yakuake/skins/default/tabs/lock.svg
/usr/share/yakuake/skins/default/tabs/right_corner.svg
/usr/share/yakuake/skins/default/tabs/selected_back.svg
/usr/share/yakuake/skins/default/tabs/selected_left.svg
/usr/share/yakuake/skins/default/tabs/selected_right.svg
/usr/share/yakuake/skins/default/tabs/separator.svg
/usr/share/yakuake/skins/default/tabs/unselected_back.svg
/usr/share/yakuake/skins/default/tabs/unselected_left.svg
/usr/share/yakuake/skins/default/tabs/unselected_right.svg
/usr/share/yakuake/skins/default/title.skin
/usr/share/yakuake/skins/default/title/back.svg
/usr/share/yakuake/skins/default/title/config_down.svg
/usr/share/yakuake/skins/default/title/config_up.svg
/usr/share/yakuake/skins/default/title/focus_down.svg
/usr/share/yakuake/skins/default/title/focus_over.svg
/usr/share/yakuake/skins/default/title/focus_up.svg
/usr/share/yakuake/skins/default/title/left.svg
/usr/share/yakuake/skins/default/title/quit_down.svg
/usr/share/yakuake/skins/default/title/quit_up.svg
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
/usr/share/package-licenses/yakuake/2123756e0b1fc8243547235a33c0fcabfe3b9a51
/usr/share/package-licenses/yakuake/3e8971c6c5f16674958913a94a36b1ea7a00ac46
/usr/share/package-licenses/yakuake/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/yakuake/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0

%files locales -f yakuake.lang
%defattr(-,root,root,-)

