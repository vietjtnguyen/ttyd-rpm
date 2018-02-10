Name:           ttyd
Version:        1.4.0
Release:        1%{?dist}
Summary:        Share your terminal over the web

License:        MIT
URL:            https://github.com/tsl0922/ttyd
Source0:        https://github.com/tsl0922/ttyd/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:  cmake3
BuildRequires:  json-c-devel
BuildRequires:  libwebsockets-devel
BuildRequires:  openssl-devel
BuildRequires:  /usr/bin/xxd

%description
ttyd is a simple command-line tool for sharing terminal over the web, inspired by GoTTY.

%prep
%setup -q

%build
mkdir build
pushd build
  %cmake3 ..
  %make_build
popd

%install
pushd build
  %make_install
popd

%files
%{_bindir}/ttyd
%doc %{_mandir}/man1/ttyd.1.gz

%changelog
* Fri Feb 09 2018 Viet The Nguyen <vietjtnguyen@gmail.com> - 1.4.0:1
- Initial packaging
