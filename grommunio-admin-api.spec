Name:		grommunio-admin-api
Version:	1.18
Release:	2
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
# FIXME why does the rpm dependency generator not see those?
Requires:	python%{pyver}dist(argcomplete)
Requires:	python%{pyver}dist(mattermostdriver)
Requires:	python%{pyver}dist(ldap3)
Requires:	python%{pyver}dist(redis)
Requires:	python%{pyver}dist(sqlalchemy)
Requires:	python%{pyver}dist(multidict)
Requires:	python%{pyver}dist(openapi-core)
Requires:	python%{pyver}dist(openapi-spec-validator)
Requires:	python%{pyver}dist(mysqlclient)
Requires:	python%{pyver}dist(legacycrypt)
Requires:	python%{pyver}dist(cryptography)
Requires:	python%{pyver}dist(pyexmdb)
Requires:	python%{pyver}dist(flask)

%patchlist
grommunio-admin-api-no-artificial-user-limit.patch

%description
grommunio Admin API is the central API component of grommunio managing
appliance(s), domain(s), users(s) and more.

grommunio API orchestrates any components and architectures required to
operate and manage the entire grommunio stack.

%prep -a
# This is supposed to catch both "gromox" and "grommunio-admin-api"
find . -type f |xargs sed -i 's|/var/lib/grom|/srv/mail/grom|g'
mkdir -p %{buildroot}%{_sysconfdir}/grommunio-admin-api/conf.d

%install -a
mkdir -p %{buildroot}%{_sysusersdir}/
cat >%{buildroot}%{_sysusersdir}/grommunio.conf <<EOF
u grommunio - "Grommunio Groupware"
m grommunio gromox
m grommunio gromoxcf
EOF

%files
%{_sysconfdir}/grommunio-admin-api/conf.d
%{_sysconfdir}/sudoers.d/grommunio-sudo
%{_bindir}/grommunio-admin
%{_unitdir}/grommunio-admin-api.service
%{_unitdir}/grommunio-admin-api.socket
%{_tmpfilesdir}/grommunio-admin-api.conf
%{_datadir}/bash-completion/completions/grommunio-admin
%{_datadir}/grommunio-admin-api
%{_datadir}/grommunio-admin-common
%{_datadir}/polkit-1/rules.d/10-grommunio.rules
%{_sysusersdir}/grommunio.conf
%doc %{_mandir}/man1/grommunio-admin*.1*
