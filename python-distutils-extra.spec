%define         module distutils-extra
Summary:	python Distutils Extra module
Summary(pl.UTF-8):	moduł języka Python - Distutils Extra
Name:		python-distutils-extra
Version:	1.91.2
Release:	1
License:	GPL
Group:		Libraries/Python
# from ubuntu
Source0:	https://launchpad.net/ubuntu/hardy/+source/python-distutils-extra/1.91.2/+files/python-%{module}_%{version}.tar.gz
# Source0-md5:	413ebd3e52c45437eaa36d1d9e6912fd
URL:		http://www.glatzor.de/projects/python-distutils-extra/
BuildRequires:	rpm-pythonprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python-distutils-extra allows to easily integrate themable icons,
scrollkeeper based documentation and gettext based translations in
your python install and build tools. It can be used with python's
distutils or the enhanced setuptools.

%prep
%setup -q -n debian

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean %{py_sitescriptdir}/%{module}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{py_sitescriptdir}/DistUtilsExtra
%{py_sitescriptdir}/DistUtilsExtra/*.py[co]
%dir %{py_sitescriptdir}/DistUtilsExtra/command
%{py_sitescriptdir}/DistUtilsExtra/command/*.py[co]
%{py_sitescriptdir}/python_distutils_extra-*-py*.egg-info
