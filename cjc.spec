Summary:	Console Jabber Client
Summary(pl):	CJC - konsolowy klient Jabbera
Name:		cjc
Version:	0.3
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://www.jabberstudio.org/files/cjc/cjc-%{version}.tar.gz
# Source0-md5:	962f95e558cec517e6930bc03a4e402c
URL:		http://cjc.jabberstudio.org/
BuildRequires:	python-modules >= 2.2.1
Requires:	python-pyxmpp = 0.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Jabber client for text terminals with user interface similar to those known
from popular IRC clients.

%prep
%setup -qn cjc-%{version}

%build

%{__make} prefix=%{_prefix}

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
%doc README TODO ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
