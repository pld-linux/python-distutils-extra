#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		pkgname		distutils-extra
%define 	module		DistUtilsExtra
%define 	egg_name	python_distutils_extra
Summary:	Python DistUtilsExtra module
Summary(pl.UTF-8):	Moduł języka Python - DistUtilsExtra
Name:		python-%{pkgname}
Version:	2.39
Release:	1
License:	GPL v2
Group:		Libraries/Python
Source0:	http://launchpad.net/python-distutils-extra/trunk/%{version}/+download/%{name}-%{version}.tar.gz
# Source0-md5:	16e06db0ef73a35b4bff4b9eed5699b5
URL:		http://www.glatzor.de/projects/python-distutils-extra/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python-distutils-extra allows to easily integrate themable icons,
scrollkeeper based documentation and gettext based translations in
your Python install and build tools. It can be used with Python's
distutils or the enhanced setuptools.

%description -l pl.UTF-8
Ten pakiet pozwala łatwo zintegrować ikony z obsługą motywów,
dokumentacje opartą na scrollkeeperze i tłumaczenia oparte na
gettekście w tworzonych narzędziach do budowania i instalacji pakietów
pythonowych. Może być używany z pythonowymi distutils lub
rozszerzonymi setuptools.

%package -n python3-%{pkgname}
Summary:	Python DistUtilsExtra module
Summary(pl.UTF-8):	Moduł języka Python - DistUtilsExtra
Group:		Libraries/Python

%description -n python3-%{pkgname}
Python-distutils-extra allows to easily integrate themable icons,
scrollkeeper based documentation and gettext based translations in
your Python install and build tools. It can be used with Python's
distutils or the enhanced setuptools.

%prep
%setup -q

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pkgname}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
