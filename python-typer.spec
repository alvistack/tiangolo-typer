# Copyright 2024 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-typer
Epoch: 100
Version: 0.12.5
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
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-typer
Summary: Typer, build great CLIs. Easy to code. Based on Python type hints
Requires: python3
Requires: python3-click >= 8.0.0
Requires: python3-typing-extensions >= 3.7.4.3
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
Requires: python3-click >= 8.0.0
Requires: python3-typing-extensions >= 3.7.4.3
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
Requires: python3-click >= 8.0.0
Requires: python3-typing-extensions >= 3.7.4.3
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

%changelog
