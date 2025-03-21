%global service py2pack_generate

Name:           obs-service-py2pack_generate
Summary:        An OBS source service: Create spec files from pypi
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
Version:        0.8
Release:        0%{?autorelease}
Source:         py2pack_generate
Source1:        py2pack_generate.service
Requires:       python3-py2pack
BuildArch:      noarch
BuildRequires:  rpm_macro(_obs_service_dir)

%description
This is a source service for openSUSE Build Service.

It's a wrapper around py2pack script

%prep
%setup -q -D -T 0 -c
sed -i 's~/usr/bin~%{_bindir}~' %{SOURCE0}

%build

%install
install -Dm 0755 %{SOURCE0} %{buildroot}%{_obs_service_dir}/py2pack_generate
install -Dm 0644 %{SOURCE1} %{buildroot}%{_obs_service_dir}/py2pack_generate.service

%files
%defattr(-,root,root)
%{_obs_service_dir}/py2pack_generate
%{_obs_service_dir}/py2pack_generate.service

%changelog
