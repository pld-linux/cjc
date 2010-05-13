Summary:	Console Jabber Client
Summary(pl.UTF-8):	CJC - konsolowy klient Jabbera
Name:		cjc
Version:	1.2.0
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Communications
Source0:	http://cjc.jajcus.net/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	ffec1743b44618d5efa3b211de90e63a
URL:		http://cjc.jajcus.net/
BuildRequires:	python
BuildRequires:	python-modules
BuildRequires:	rpm-pythonprov
Requires:	python-pyxmpp >= 1.1.0
Suggests:	ca-certificates
Suggests:	python-modules-sqlite
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Jabber client for text terminals with user interface similar to
those known from popular IRC clients.

%description -l pl.UTF-8
Klient Jabbera dla terminali tekstowych z interfejsem użytkownika
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

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}
%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins

rm -f $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}{,/ui}/*.py

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
%{_datadir}/%{name}/%{name}/*.pyc
%{_datadir}/%{name}/%{name}/ui/*.pyc
%{_datadir}/%{name}/plugins/*
