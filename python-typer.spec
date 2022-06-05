%global debug_package %{nil}

Name: python-typer
Epoch: 100
Version: 0.4.2
Release: 1%{?dist}
BuildArch: noarch
Summary: Typer, build great CLIs. Easy to code. Based on Python type hints
License: MIT
URL: https://github.com/tiangolo/typer/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Typer is a library for building CLI applications that users will love
using and developers will love creating. Based on Python 3.6+ type
hints.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
%fdupes -s %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-typer
Summary: Typer, build great CLIs. Easy to code. Based on Python type hints
Requires: python3
Provides: python3-typer = %{epoch}:%{version}-%{release}
Provides: python3dist(typer) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-typer = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(typer) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-typer = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(typer) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-typer
Typer is a library for building CLI applications that users will love
using and developers will love creating. Based on Python 3.6+ type
hints.

%files -n python%{python3_version_nodots}-typer
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-typer
Summary: Typer, build great CLIs. Easy to code. Based on Python type hints
Requires: python3
Requires: python3-click >= 7.1.1
Provides: python3-typer = %{epoch}:%{version}-%{release}
Provides: python3dist(typer) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-typer = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(typer) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-typer = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(typer) = %{epoch}:%{version}-%{release}

%description -n python3-typer
Typer is a library for building CLI applications that users will love
using and developers will love creating. Based on Python 3.6+ type
hints.

%files -n python3-typer
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-typer
Summary: Typer, build great CLIs. Easy to code. Based on Python type hints
Requires: python3
Requires: python3-click >= 7.1.1
Provides: python3-typer = %{epoch}:%{version}-%{release}
Provides: python3dist(typer) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-typer = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(typer) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-typer = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(typer) = %{epoch}:%{version}-%{release}

%description -n python3-typer
Click is a Python package for creating command line interfaces in a
composable way with as little code as necessary. It's the "Command Line
Interface Creation Kit". It is configurable, and comes with defaults out
of the box.

%files -n python3-typer
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
