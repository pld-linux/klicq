Summary:	Klicq - patched licq for KDE
Summary(pl):	Klicq - wersja licq dla KDE
Name:		klicq
Version:	0.61.2
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	%{name}-%{version}.tar.gz
#Source0:	http://www.cs.nmt.edu/~dquist/klicq/%{name}-0.61-2.tar.gz
URL:		http://www.cs.nmt.edu/~dquist/klicq/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This is a patch to the licq 0.61 sources to add KDE support and
extensions. See http://www.licq.org/ for the original licq sources and
information.

%description -l pl
To jest zmodyfikowane licq 0.61 tak, aby dodaæ wsparcie dla KDE i
rozszerzeñ. Oryginalne licq znajduje siê pod adresem
http://www.licq.org/.

%prep
%setup -q -1

%build
CXXFLAGS="%{rpmcflags}" CFLAGS="%{rpmcflags}" ./configure \
	--prefix=%{_prefix}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{_prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/licq
%{_mandir}/man1/licq.1
%{_datadir}/licq-base.tar.gz
%doc README.Klicq doc/ contrib/ misc/licq.javaconvert.1
