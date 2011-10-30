%define         module distutils-extra
Summary:	Python DistUtilsExtra module
Summary(pl.UTF-8):	Moduł języka Python - DistUtilsExtra
Name:		python-distutils-extra
Version:	2.30
Release:	0.9
License:	GPL
Group:		Libraries/Python
Source0:	http://launchpad.net/python-distutils-extra/trunk/%{version}/+download/python-%{module}-%{version}.tar.gz
# Source0-md5:	892804ef5575da9273bde8dd3d2c574f
URL:		http://www.glatzor.de/projects/python-distutils-extra/
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python-distutils-extra allows to easily integrate themable icons,
scrollkeeper based documentation and gettext based translations in
your python install and build tools. It can be used with python's
distutils or the enhanced setuptools.

%description -l pl.UTF-8
Ten pakiet pozwala łatwo zintegrować ikony z obsługą motywów,
dokumentacje opartą na scrollkeeperze i tłumaczenia oparte na
gettekście w tworzonych narzędziach do budowania i instalacji pakietów
pythonowych. Może być używany z pythonowymi distutils lub
rozszerzonymi setuptools.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/DistUtilsExtra
%{py_sitescriptdir}/DistUtilsExtra/*.py[co]
%dir %{py_sitescriptdir}/DistUtilsExtra/command
%{py_sitescriptdir}/DistUtilsExtra/command/*.py[co]
%{py_sitescriptdir}/python_distutils_extra-*-py*.egg-info
