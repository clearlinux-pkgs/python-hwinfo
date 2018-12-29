#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : python-hwinfo
Version  : 0.1.7
Release  : 5
URL      : https://github.com/rdobson/python-hwinfo/archive/0.1.7.tar.gz
Source0  : https://github.com/rdobson/python-hwinfo/archive/0.1.7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.1
Requires: python-hwinfo-bin = %{version}-%{release}
Requires: python-hwinfo-license = %{version}-%{release}
Requires: python-hwinfo-python = %{version}-%{release}
Requires: python-hwinfo-python3 = %{version}-%{release}
Requires: paramiko
Requires: prettytable
BuildRequires : buildreq-distutils3
BuildRequires : paramiko
BuildRequires : pluggy
BuildRequires : prettytable
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv
Patch1: 0001-python3-compat-fixes.patch
Patch2: 0002-python2to3-conversion.patch

%description
[![Build Status](https://travis-ci.org/rdobson/python-hwinfo.svg?branch=master)](https://travis-ci.org/rdobson/python-hwinfo)
[![Coverage Status](https://coveralls.io/repos/rdobson/python-hwinfo/badge.png)](https://coveralls.io/r/rdobson/python-hwinfo)

%package bin
Summary: bin components for the python-hwinfo package.
Group: Binaries
Requires: python-hwinfo-license = %{version}-%{release}

%description bin
bin components for the python-hwinfo package.


%package license
Summary: license components for the python-hwinfo package.
Group: Default

%description license
license components for the python-hwinfo package.


%package python
Summary: python components for the python-hwinfo package.
Group: Default
Requires: python-hwinfo-python3 = %{version}-%{release}

%description python
python components for the python-hwinfo package.


%package python3
Summary: python3 components for the python-hwinfo package.
Group: Default
Requires: python3-core

%description python3
python3 components for the python-hwinfo package.


%prep
%setup -q -n python-hwinfo-0.1.7
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538171416
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/python-hwinfo
cp LICENSE %{buildroot}/usr/share/package-licenses/python-hwinfo/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/hwinfo

%files license
%defattr(-,root,root,-)
/usr/share/package-licenses/python-hwinfo/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
