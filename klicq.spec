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
BuildRoot:	/tmp/%{name}-%{version}-root

%description
This is a patch to the licq 0.61 sources to add KDE support and
extensions.  See http://www.licq.org for the original licq
sources and information.

%prep
%setup -1

%build
CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=%{prefix}
make 

%install
rm -rf $RPM_BUILD_ROOT
make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%attr(0755,root,root) %{prefix}/bin/licq
%attr(0644,root,root) %{prefix}/man/man1/licq.1
%attr(0644,root,root) %{prefix}/share/licq-base.tar.gz
%doc README.Klicq doc/ contrib/ misc/licq.javaconvert.1
