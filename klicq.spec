Summary:	Klicq - patched licq for KDE
Name:		klicq
Version:	0.61.2
Release:	1
Copyright:	GPL
Vendor:		Daniel Quist <dquist@cs.nmt.edu>
Packager:	Troy Engel <tengel@sonic.net>
Group:		X11/KDE/Internet
Source:		%{name}-%{version}.tar.gz
URL:		http://www.cs.nmt.edu/~dquist/klicq
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a patch to the licq 0.61 sources to add KDE support and
extensions.  See http://www.licq.org for the original licq
sources and information.

%prep
%setup -1

%build
CXXFLAGS="%{rpmcflags}" CFLAGS="%{rpmcflags}" ./configure \
	--prefix=%{prefix}
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
%{__make} prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/licq
%attr(644,root,root) %{_mandir}/man1/licq.1
%attr(644,root,root) %{_datadir}/licq-base.tar.gz
%doc README.Klicq doc/ contrib/ misc/licq.javaconvert.1
