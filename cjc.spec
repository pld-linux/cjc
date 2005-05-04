#
# TODO:
# - on amd64 with .pyc files search main module at BUILDROOT,
#
Summary:	Console Jabber Client
Summary(pl):	CJC - konsolowy klient Jabbera
Name:		cjc
Version:	0.5.s20050428
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Communications
#Source0:	http://www.jabberstudio.org/files/cjc/cjc-%{version}.tar.gz
#Source0:	http://www.jajcus.net/files/cjc-%{version}.tar.gz
Source0:	http://cjc.jabberstudio.org/snapshots/cjc-%{version}.tar.gz
# Source0-md5:	23d595f120cee66b37c5ad656b8d47a2
URL:		http://cjc.jabberstudio.org/
BuildRequires:	python-modules >= 2.3.0
%pyrequires_eq	python-modules
Requires:	python-pyxmpp >= 0.5.s20050428
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Jabber client for text terminals with user interface similar to
those known from popular IRC clients.

%description -l pl
Klient Jabbera dla terminali tekstowych z interfejsem u¿ytkownika
podobnym do tego znanego z popularnych klientów IRC.

%prep
%setup -q

%build
%{__make} \
	prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_prefix}/share/doc

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO ChangeLog doc/manual.html
%attr(755,root,root) %{_bindir}/*
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{name}
%dir %{_datadir}/%{name}/%{name}/ui
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/%{name}/*.py
%{_datadir}/%{name}/%{name}/ui/*.py
%{_datadir}/%{name}/plugins/*.py
