#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v20
# autospec commit: f35655a
#
# Source0 file verified with key 0x2C8DF587A6D4AAC1 (nicolas.fella@kde.org)
#
Name     : attica
Version  : 6.7.0
Release  : 94
URL      : https://download.kde.org/stable/frameworks/6.7/attica-6.7.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/6.7/attica-6.7.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/6.7/attica-6.7.0.tar.xz.sig
Source2  : 2C8DF587A6D4AAC1.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : CC0-1.0 LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: attica-data = %{version}-%{release}
Requires: attica-lib = %{version}-%{release}
Requires: attica-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : gnupg
BuildRequires : mesa-dev
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Attica
Open Collaboration Service client library
## Introduction
Attica is a Qt library that implements the Open Collaboration Services API version 1.6.
The REST API is defined here:
https://www.freedesktop.org/wiki/Specifications/open-collaboration-services/

%package data
Summary: data components for the attica package.
Group: Data

%description data
data components for the attica package.


%package dev
Summary: dev components for the attica package.
Group: Development
Requires: attica-lib = %{version}-%{release}
Requires: attica-data = %{version}-%{release}
Provides: attica-devel = %{version}-%{release}
Requires: attica = %{version}-%{release}

%description dev
dev components for the attica package.


%package lib
Summary: lib components for the attica package.
Group: Libraries
Requires: attica-data = %{version}-%{release}
Requires: attica-license = %{version}-%{release}

%description lib
lib components for the attica package.


%package license
Summary: license components for the attica package.
Group: Default

%description license
license components for the attica package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 2C8DF587A6D4AAC1' gpg.status
%setup -q -n attica-6.7.0
cd %{_builddir}/attica-6.7.0
pushd ..
cp -a attica-6.7.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1728690904
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
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
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
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
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
export SOURCE_DATE_EPOCH=1728690904
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/attica
cp %{_builddir}/attica-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/attica/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/attica-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/attica/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/attica-%{version}/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/attica/3c3d7573e137d48253731c975ecf90d74cfa9efe || :
cp %{_builddir}/attica-%{version}/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/attica/757b86330df80f81143d5916b3e92b4bcb1b1890 || :
cp %{_builddir}/attica-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/attica/e458941548e0864907e654fa2e192844ae90fc32 || :
cp %{_builddir}/attica-%{version}/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/attica/e458941548e0864907e654fa2e192844ae90fc32 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories6/attica.categories
/usr/share/qlogging-categories6/attica.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF6/Attica/Attica/AccountBalance
/usr/include/KF6/Attica/Attica/Achievement
/usr/include/KF6/Attica/Attica/Activity
/usr/include/KF6/Attica/Attica/BuildService
/usr/include/KF6/Attica/Attica/BuildServiceJob
/usr/include/KF6/Attica/Attica/BuildServiceJobOutput
/usr/include/KF6/Attica/Attica/Category
/usr/include/KF6/Attica/Attica/Comment
/usr/include/KF6/Attica/Attica/Config
/usr/include/KF6/Attica/Attica/Content
/usr/include/KF6/Attica/Attica/DeleteJob
/usr/include/KF6/Attica/Attica/Distribution
/usr/include/KF6/Attica/Attica/DownloadDescription
/usr/include/KF6/Attica/Attica/DownloadItem
/usr/include/KF6/Attica/Attica/Event
/usr/include/KF6/Attica/Attica/Folder
/usr/include/KF6/Attica/Attica/Forum
/usr/include/KF6/Attica/Attica/GetJob
/usr/include/KF6/Attica/Attica/HomePageEntry
/usr/include/KF6/Attica/Attica/HomePageType
/usr/include/KF6/Attica/Attica/Icon
/usr/include/KF6/Attica/Attica/ItemJob
/usr/include/KF6/Attica/Attica/KnowledgeBaseEntry
/usr/include/KF6/Attica/Attica/License
/usr/include/KF6/Attica/Attica/ListJob
/usr/include/KF6/Attica/Attica/Message
/usr/include/KF6/Attica/Attica/Metadata
/usr/include/KF6/Attica/Attica/Person
/usr/include/KF6/Attica/Attica/PostJob
/usr/include/KF6/Attica/Attica/PrivateData
/usr/include/KF6/Attica/Attica/Project
/usr/include/KF6/Attica/Attica/Provider
/usr/include/KF6/Attica/Attica/ProviderManager
/usr/include/KF6/Attica/Attica/Publisher
/usr/include/KF6/Attica/Attica/PublisherField
/usr/include/KF6/Attica/Attica/PutJob
/usr/include/KF6/Attica/Attica/RemoteAccount
/usr/include/KF6/Attica/Attica/Topic
/usr/include/KF6/Attica/attica/accountbalance.h
/usr/include/KF6/Attica/attica/achievement.h
/usr/include/KF6/Attica/attica/activity.h
/usr/include/KF6/Attica/attica/attica_export.h
/usr/include/KF6/Attica/attica/atticabasejob.h
/usr/include/KF6/Attica/attica/atticautils.h
/usr/include/KF6/Attica/attica/buildservice.h
/usr/include/KF6/Attica/attica/buildservicejob.h
/usr/include/KF6/Attica/attica/buildservicejoboutput.h
/usr/include/KF6/Attica/attica/category.h
/usr/include/KF6/Attica/attica/comment.h
/usr/include/KF6/Attica/attica/config.h
/usr/include/KF6/Attica/attica/content.h
/usr/include/KF6/Attica/attica/deletejob.h
/usr/include/KF6/Attica/attica/distribution.h
/usr/include/KF6/Attica/attica/downloaddescription.h
/usr/include/KF6/Attica/attica/downloaditem.h
/usr/include/KF6/Attica/attica/event.h
/usr/include/KF6/Attica/attica/folder.h
/usr/include/KF6/Attica/attica/forum.h
/usr/include/KF6/Attica/attica/getjob.h
/usr/include/KF6/Attica/attica/homepageentry.h
/usr/include/KF6/Attica/attica/homepagetype.h
/usr/include/KF6/Attica/attica/icon.h
/usr/include/KF6/Attica/attica/itemjob.h
/usr/include/KF6/Attica/attica/knowledgebaseentry.h
/usr/include/KF6/Attica/attica/license.h
/usr/include/KF6/Attica/attica/listjob.h
/usr/include/KF6/Attica/attica/message.h
/usr/include/KF6/Attica/attica/metadata.h
/usr/include/KF6/Attica/attica/person.h
/usr/include/KF6/Attica/attica/platformdependent.h
/usr/include/KF6/Attica/attica/platformdependent_v2.h
/usr/include/KF6/Attica/attica/platformdependent_v3.h
/usr/include/KF6/Attica/attica/postjob.h
/usr/include/KF6/Attica/attica/privatedata.h
/usr/include/KF6/Attica/attica/project.h
/usr/include/KF6/Attica/attica/provider.h
/usr/include/KF6/Attica/attica/providermanager.h
/usr/include/KF6/Attica/attica/publisher.h
/usr/include/KF6/Attica/attica/publisherfield.h
/usr/include/KF6/Attica/attica/putjob.h
/usr/include/KF6/Attica/attica/remoteaccount.h
/usr/include/KF6/Attica/attica/topic.h
/usr/include/KF6/Attica/attica/version.h
/usr/include/KF6/Attica/attica_version.h
/usr/lib64/cmake/KF6Attica/KF6AtticaConfig.cmake
/usr/lib64/cmake/KF6Attica/KF6AtticaConfigVersion.cmake
/usr/lib64/cmake/KF6Attica/KF6AtticaTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF6Attica/KF6AtticaTargets.cmake
/usr/lib64/libKF6Attica.so
/usr/lib64/pkgconfig/KF6Attica.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libKF6Attica.so.6.7.0
/usr/lib64/libKF6Attica.so.6
/usr/lib64/libKF6Attica.so.6.7.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/attica/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/attica/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/attica/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/attica/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/attica/e458941548e0864907e654fa2e192844ae90fc32
