Summary:	Console Jabber Client
Summary(pl):	CJC - konsolowy klient Jabbera
Name:		cjc
Version:	0.5.s20041219
Release:	2
License:	GPL
Group:		Applications/Communications
#Source0:	http://www.jabberstudio.org/files/cjc/cjc-%{version}.tar.gz
Source0:	http://cjc.jabberstudio.org/snapshots/cjc-%{version}.tar.gz
# Source0-md5:	d3031815efc022b549df3dc1059025c8
URL:		http://cjc.jabberstudio.org/
BuildRequires:	python-modules >= 2.3.0
Requires:	python-pyxmpp >= 0.5.s20041101
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
%{_datadir}/%{name}
