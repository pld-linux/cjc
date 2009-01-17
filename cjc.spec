Summary:	Console Jabber Client
Summary(pl.UTF-8):	CJC - konsolowy klient Jabbera
Name:		cjc
Version:	1.0.1
Release:	1
Epoch:		1
License:	GPL
Group:		Applications/Communications
Source0:	http://cjc.jajcus.net/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	d1fbba4da7d0187d22997f4732b0211c
URL:		http://cjc.jajcus.net/
Requires:	python-pyxmpp >= 1.0.1
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
