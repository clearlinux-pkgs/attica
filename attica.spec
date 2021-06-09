#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x58D0EE648A48B3BB (faure@kde.org)
#
Name     : attica
Version  : 5.82.0
Release  : 41
URL      : https://download.kde.org/stable/frameworks/5.82/attica-5.82.0.tar.xz
Source0  : https://download.kde.org/stable/frameworks/5.82/attica-5.82.0.tar.xz
Source1  : https://download.kde.org/stable/frameworks/5.82/attica-5.82.0.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0 LGPL-2.1 LGPL-3.0
Requires: attica-data = %{version}-%{release}
Requires: attica-lib = %{version}-%{release}
Requires: attica-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : mesa-dev
BuildRequires : qtbase-dev
BuildRequires : qtbase-dev mesa-dev

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
%setup -q -n attica-5.82.0
cd %{_builddir}/attica-5.82.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623262116
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
export SOURCE_DATE_EPOCH=1623262116
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/attica
cp %{_builddir}/attica-5.82.0/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/attica/20079e8f79713dce80ab09774505773c926afa2a
cp %{_builddir}/attica-5.82.0/LICENSES/LGPL-2.1-only.txt %{buildroot}/usr/share/package-licenses/attica/3c3d7573e137d48253731c975ecf90d74cfa9efe
cp %{_builddir}/attica-5.82.0/LICENSES/LGPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/attica/757b86330df80f81143d5916b3e92b4bcb1b1890
cp %{_builddir}/attica-5.82.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/attica/e458941548e0864907e654fa2e192844ae90fc32
cp %{_builddir}/attica-5.82.0/LICENSES/LicenseRef-KDE-Accepted-LGPL.txt %{buildroot}/usr/share/package-licenses/attica/e458941548e0864907e654fa2e192844ae90fc32
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/qlogging-categories5/attica.categories
/usr/share/qlogging-categories5/attica.renamecategories

%files dev
%defattr(-,root,root,-)
/usr/include/KF5/Attica/Attica/AccountBalance
/usr/include/KF5/Attica/Attica/Achievement
/usr/include/KF5/Attica/Attica/Activity
/usr/include/KF5/Attica/Attica/BuildService
/usr/include/KF5/Attica/Attica/BuildServiceJob
/usr/include/KF5/Attica/Attica/BuildServiceJobOutput
/usr/include/KF5/Attica/Attica/Category
/usr/include/KF5/Attica/Attica/Comment
/usr/include/KF5/Attica/Attica/Config
/usr/include/KF5/Attica/Attica/Content
/usr/include/KF5/Attica/Attica/DeleteJob
/usr/include/KF5/Attica/Attica/Distribution
/usr/include/KF5/Attica/Attica/DownloadDescription
/usr/include/KF5/Attica/Attica/DownloadItem
/usr/include/KF5/Attica/Attica/Event
/usr/include/KF5/Attica/Attica/Folder
/usr/include/KF5/Attica/Attica/Forum
/usr/include/KF5/Attica/Attica/GetJob
/usr/include/KF5/Attica/Attica/HomePageEntry
/usr/include/KF5/Attica/Attica/HomePageType
/usr/include/KF5/Attica/Attica/Icon
/usr/include/KF5/Attica/Attica/ItemJob
/usr/include/KF5/Attica/Attica/KnowledgeBaseEntry
/usr/include/KF5/Attica/Attica/License
/usr/include/KF5/Attica/Attica/ListJob
/usr/include/KF5/Attica/Attica/Message
/usr/include/KF5/Attica/Attica/Metadata
/usr/include/KF5/Attica/Attica/Person
/usr/include/KF5/Attica/Attica/PostJob
/usr/include/KF5/Attica/Attica/PrivateData
/usr/include/KF5/Attica/Attica/Project
/usr/include/KF5/Attica/Attica/Provider
/usr/include/KF5/Attica/Attica/ProviderManager
/usr/include/KF5/Attica/Attica/Publisher
/usr/include/KF5/Attica/Attica/PublisherField
/usr/include/KF5/Attica/Attica/PutJob
/usr/include/KF5/Attica/Attica/RemoteAccount
/usr/include/KF5/Attica/Attica/Topic
/usr/include/KF5/Attica/attica/accountbalance.h
/usr/include/KF5/Attica/attica/achievement.h
/usr/include/KF5/Attica/attica/activity.h
/usr/include/KF5/Attica/attica/attica_export.h
/usr/include/KF5/Attica/attica/atticabasejob.h
/usr/include/KF5/Attica/attica/atticautils.h
/usr/include/KF5/Attica/attica/buildservice.h
/usr/include/KF5/Attica/attica/buildservicejob.h
/usr/include/KF5/Attica/attica/buildservicejoboutput.h
/usr/include/KF5/Attica/attica/category.h
/usr/include/KF5/Attica/attica/comment.h
/usr/include/KF5/Attica/attica/config.h
/usr/include/KF5/Attica/attica/content.h
/usr/include/KF5/Attica/attica/deletejob.h
/usr/include/KF5/Attica/attica/distribution.h
/usr/include/KF5/Attica/attica/downloaddescription.h
/usr/include/KF5/Attica/attica/downloaditem.h
/usr/include/KF5/Attica/attica/event.h
/usr/include/KF5/Attica/attica/folder.h
/usr/include/KF5/Attica/attica/forum.h
/usr/include/KF5/Attica/attica/getjob.h
/usr/include/KF5/Attica/attica/homepageentry.h
/usr/include/KF5/Attica/attica/homepagetype.h
/usr/include/KF5/Attica/attica/icon.h
/usr/include/KF5/Attica/attica/itemjob.h
/usr/include/KF5/Attica/attica/knowledgebaseentry.h
/usr/include/KF5/Attica/attica/license.h
/usr/include/KF5/Attica/attica/listjob.h
/usr/include/KF5/Attica/attica/message.h
/usr/include/KF5/Attica/attica/metadata.h
/usr/include/KF5/Attica/attica/person.h
/usr/include/KF5/Attica/attica/platformdependent.h
/usr/include/KF5/Attica/attica/platformdependent_v2.h
/usr/include/KF5/Attica/attica/postjob.h
/usr/include/KF5/Attica/attica/privatedata.h
/usr/include/KF5/Attica/attica/project.h
/usr/include/KF5/Attica/attica/provider.h
/usr/include/KF5/Attica/attica/providermanager.h
/usr/include/KF5/Attica/attica/publisher.h
/usr/include/KF5/Attica/attica/publisherfield.h
/usr/include/KF5/Attica/attica/putjob.h
/usr/include/KF5/Attica/attica/remoteaccount.h
/usr/include/KF5/Attica/attica/topic.h
/usr/include/KF5/Attica/attica/version.h
/usr/include/KF5/attica_version.h
/usr/lib64/cmake/KF5Attica/KF5AtticaConfig.cmake
/usr/lib64/cmake/KF5Attica/KF5AtticaConfigVersion.cmake
/usr/lib64/cmake/KF5Attica/KF5AtticaTargets-relwithdebinfo.cmake
/usr/lib64/cmake/KF5Attica/KF5AtticaTargets.cmake
/usr/lib64/libKF5Attica.so
/usr/lib64/pkgconfig/libKF5Attica.pc
/usr/lib64/qt5/mkspecs/modules/qt_Attica.pri

%files lib
%defattr(-,root,root,-)
/usr/lib64/libKF5Attica.so.5
/usr/lib64/libKF5Attica.so.5.82.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/attica/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/attica/3c3d7573e137d48253731c975ecf90d74cfa9efe
/usr/share/package-licenses/attica/757b86330df80f81143d5916b3e92b4bcb1b1890
/usr/share/package-licenses/attica/e458941548e0864907e654fa2e192844ae90fc32
