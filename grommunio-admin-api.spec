Name:		grommunio-admin-api
Version:	1.18
Release:	1
Source0:	https://github.com/grommunio/admin-api/releases/download/%{version}/grommunio-admin-api-%{version}.tar.zst
Summary:	Management REST API for grommunio
URL:		https://github.com/grommunio/admin-api
License:	AGPL-3.0
Group:		Servers
BuildRequires:	cmake
BuildSystem:	cmake
BuildArch:	noarch
BuildRequires:	python
BuildRequires:	pkgconfig(systemd)
BuildRequires:	python%{pyver}dist(pyyaml)

%description
grommunio Admin API is the central API component of grommunio managing
appliance(s), domain(s), users(s) and more.

grommunio API orchestrates any components and architectures required to
operate and manage the entire grommunio stack.

%prep -a
# This is supposed to catch both "gromox" and "grommunio-admin-api"
find . -type f |xargs sed -i 's|/var/lib/grom|/srv/mail/grom|g'

%files
%{_sysconfdir}/sudoers.d/grommunio-sudo
%{_bindir}/grommunio-admin
%{_unitdir}/grommunio-admin-api.service
%{_unitdir}/grommunio-admin-api.socket
%{_tmpfilesdir}/grommunio-admin-api.conf
%{_datadir}/bash-completion/completions/grommunio-admin
%{_datadir}/grommunio-admin-api
%{_datadir}/grommunio-admin-common
%{_datadir}/polkit-1/rules.d/10-grommunio.rules
%doc %{_mandir}/man1/grommunio-admin*.1*

