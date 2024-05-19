Summary:	Console Jabber Client
Summary(pl.UTF-8):	CJC - konsolowy klient Jabbera
Name:		cjc
Version:	1.2.1
Release:	2
Epoch:		1
License:	GPL v2
Group:		Applications/Communications
Source0:	http://cloud.github.com/downloads/Jajcus/cjc/cjc-%{version}.tar.gz
# Source0-md5:	fbb161f9d77ddb477f4d4a8165e2eb5b
Patch0:		%{name}-pyc.patch
URL:		https://github.com/Jajcus/cjc
BuildRequires:	python >= 1:2.6
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.745
BuildRequires:	sed >= 4.0
Requires:	python-pyxmpp >= 1.1.2
Suggests:	ca-certificates
Suggests:	python-modules-sqlite >= 1:2.6
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
%patch0 -p1

%{__sed} -i -e '1s,/usr/bin/python$,%{__python},' cjc.in cjc.py

%build
%{__make} \
	prefix=%{_prefix}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_prefix}/share/doc

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_postclean %{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO doc/manual.html
%attr(755,root,root) %{_bindir}/cjc
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/%{name}
%{_datadir}/%{name}/%{name}/*.py[co]
%dir %{_datadir}/%{name}/%{name}/ui
%{_datadir}/%{name}/%{name}/ui/*.py[co]
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/*.py[co]
