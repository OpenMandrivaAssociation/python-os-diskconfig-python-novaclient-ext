Name:		python-os-diskconfig-python-novaclient-ext
Version:	0.1.3
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/o/os-diskconfig-python-novaclient-ext/os_diskconfig_python_novaclient_ext-%{version}.tar.gz
Summary:	Disk Config extension for python-novaclient
URL:		https://pypi.org/project/os-diskconfig-python-novaclient-ext/
License:	Apache License, Version 2.0
Group:		Development/Python
BuildRequires:	python
BuildSystem:	python
BuildArch:	noarch

%description
Disk Config extension for python-novaclient

%files
%{py_sitedir}/os_diskconfig_python_novaclient_ext
%{py_sitedir}/os_diskconfig_python_novaclient_ext-*.*-info
