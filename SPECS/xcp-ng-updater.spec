Summary: XAPI plugin for updating through yum
Name: xcp-ng-updater
Version: 1.3.0
Release: 1%{?dist}
URL: https://github.com/xcp-ng/xcp-ng-updater
Source0: https://github.com/xcp-ng/xcp-ng-updater/archive/v%{version}/%{name}-%{version}.tar.gz
License: AGPLv3

BuildArch: noarch

%description
A XAPI plugin that allows to interact with the underlying package manager.

%prep
%autosetup -p1

%install
install -D SOURCES/etc/xapi.d/plugins/updater.py %{buildroot}/etc/xapi.d/plugins/updater.py

%files
%doc LICENSE README.md test_updater.sh
/etc/xapi.d/plugins/*

%changelog
* Fri May 31 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.3.0-1
- New version 1.3.0 with added zfs discovery plugin

* Thu May 02 2019 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.2.0-1
- New version 1.2.0 with proxy configuration support

* Thu Sep 13 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.1.0-3
- Rebuild for XCP-ng 7.6.0

* Fri Jul 27 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.1.0-2
- Version of last published package was actually 1.1, updating

* Fri Jun 29 2018 Samuel Verschelde <stormi-xcp@ylix.fr> - 1.0.0-1
- Initial package.

