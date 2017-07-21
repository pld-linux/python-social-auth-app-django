#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module

%define		module		social_django
%define		pypi_name	social-auth-app-django
%define		egg_name	social_auth_app_django
Summary:	Python Social Auth - Application - Django
Name:		python-%{pypi_name}
Version:	1.2.0
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/s/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	ec78f03b8053ecaa4d33b35a128c00bd
URL:		https://github.com/python-social-auth/social-app-django
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	python-social-auth-core >= 1.2.0
%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
BuildRequires:	python3-social-auth-core >= 1.2.0
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python Social Auth is an easy to setup social
authentication/registration mechanism with support for several
frameworks and auth providers.

This is the Django component of the python-social-auth ecosystem, it
implements the needed functionality to integrate social-auth-core in a
Django based project.

%package -n python3-%{pypi_name}
Summary:	Python Social Auth - Application - Django
Group:		Libraries/Python

%description -n python3-%{pypi_name}
Python Social Auth is an easy to setup social
authentication/registration mechanism with support for several
frameworks and auth providers.

This is the Django component of the python-social-auth ecosystem, it
implements the needed functionality to integrate social-auth-core in a
Django based project.

%prep
%setup -q -n %{pypi_name}-%{version}

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
%doc README.md LICENSE
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc README.md LICENSE
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
