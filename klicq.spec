%define name klicq
%define version 0.61.2
%define release 1.rh60
%define prefix /usr

%define builddir $RPM_BUILD_DIR/%{name}-%{version}

Summary: Klicq - patched licq for KDE
Name: %{name}
Version: %{version}
Release: %{release}
Prefix: %{prefix}
Copyright: GPL
Vendor: Daniel Quist <dquist@cs.nmt.edu>
Packager: Troy Engel <tengel@sonic.net>
Group: X11/KDE/Internet
Source: %{name}-%{version}.tar.gz
URL: http://www.cs.nmt.edu/~dquist/klicq
BuildRoot: /tmp/%{name}-%{version}-root

%description
This is a patch to the licq 0.61 sources to add KDE support and
extensions.  See http://www.licq.org for the original licq
sources and information.

%prep
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}

%setup  

%build
CXXFLAGS="$RPM_OPT_FLAGS" CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=%{prefix}
make 

%install
make prefix=$RPM_BUILD_ROOT%{prefix} install

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{builddir}

%files
%defattr(-,root,root)
%attr(0755,root,root) %{prefix}/bin/licq
%attr(0644,root,root) %{prefix}/man/man1/licq.1
%attr(0644,root,root) %{prefix}/share/licq-base.tar.gz
%doc README.Klicq doc/ contrib/ misc/licq.javaconvert.1
