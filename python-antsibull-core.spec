# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
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

Name: python-antsibull-core
Epoch: 100
Version: 1.6.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Tools for building the Ansible Distribution
License: GPL-3.0-only
URL: https://github.com/ansible-community/antsibull-core/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Tools for building the Ansible Distribution.

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
%package -n python%{python3_version_nodots}-antsibull-core
Summary: Tools for building the Ansible Distribution
Requires: python3
Requires: python3-aiofiles
Requires: python3-aiohttp >= 3.0.0
Requires: python3-packaging >= 20.0
Requires: python3-perky
Requires: python3-pydantic >= 1.0.0
Requires: python3-pydantic < 2.0.0
Requires: python3-PyYAML
Requires: python3-semantic_version
Requires: python3-sh >= 1.0.0
Requires: python3-sh < 2.0.0
Requires: python3-twiggy >= 0.5.0
Provides: python3-antsibull-core = %{epoch}:%{version}-%{release}
Provides: python3dist(antsibull-core) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-antsibull-core = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(antsibull-core) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-antsibull-core = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(antsibull-core) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-antsibull-core
Tools for building the Ansible Distribution.

%files -n python%{python3_version_nodots}-antsibull-core
%license LICENSE
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-antsibull-core
Summary: Tools for building the Ansible Distribution
Requires: python3
Requires: python3-aiofiles
Requires: python3-aiohttp >= 3.0.0
Requires: python3-packaging >= 20.0
Requires: python3-perky
Requires: python3-pydantic >= 1.0.0
Requires: python3-pydantic < 2.0.0
Requires: python3-PyYAML
Requires: python3-semantic_version
Requires: python3-sh >= 1.0.0
Requires: python3-sh < 2.0.0
Requires: python3-twiggy >= 0.5.0
Provides: python3-antsibull-core = %{epoch}:%{version}-%{release}
Provides: python3dist(antsibull-core) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-antsibull-core = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(antsibull-core) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-antsibull-core = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(antsibull-core) = %{epoch}:%{version}-%{release}

%description -n python3-antsibull-core
Tools for building the Ansible Distribution.

%files -n python3-antsibull-core
%license LICENSE
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-antsibull-core
Summary: Tools for building the Ansible Distribution
Requires: python3
Requires: python3-aiofiles
Requires: python3-aiohttp >= 3.0.0
Requires: python3-packaging >= 20.0
Requires: python3-perky
Requires: python3-pydantic >= 1.0.0
Requires: python3-pydantic < 2.0.0
Requires: python3-pyyaml
Requires: python3-semantic_version
Requires: python3-sh >= 1.0.0
Requires: python3-sh < 2.0.0
Requires: python3-twiggy >= 0.5.0
Provides: python3-antsibull-core = %{epoch}:%{version}-%{release}
Provides: python3dist(antsibull-core) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-antsibull-core = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(antsibull-core) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-antsibull-core = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(antsibull-core) = %{epoch}:%{version}-%{release}

%description -n python3-antsibull-core
Tooling for building Ansible documentation.

%files -n python3-antsibull-core
%license LICENSE
%{python3_sitelib}/*
%endif

%changelog
