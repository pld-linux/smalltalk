Summary:	GNU smalltalk
Summary(pl):	GNU smalltalk
Name:		smalltalk
Version:	2.1.8
Release:	3
License:	GPL
Group:		Development/Languages
Source0:	ftp://ftp.gnu.org/pub/gnu/smalltalk/%{name}-%{version}.tar.gz
# Source0-md5:	dd55006e41c87ddbf90f7cd2166b290b
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-info.patch
Patch1:		%{name}-PACKAGE.patch
Patch2:		%{name}-nolibs.patch
Patch3:		%{name}-aligned.patch
Patch4:		%{name}-proc.patch
Patch5:		%{name}-alloc.patch
Patch6:		%{name}-amd64.patch
Icon:		smalltalk.xpm
URL:		http://www.gnu.org/software/smalltalk/
BuildRequires:	atk-devel >= 1.0.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gawk
BuildRequires:	gdbm-devel
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libltdl-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pango-devel >= 1:1.0.0
BuildRequires:	pkgconfig
BuildRequires:	readline-devel >= 4.2
BuildRequires:	tk-devel >= 8.4
#BuildRequires:	xemacs
# 2.1.x versions won't work correctly on amd64 and alpha (on amd64 crashes
# even on build time) because of calling convention (no registers support)
# it should be fixed in devel (2.1e) version (but alloc,amd64 patches seem
# still needed there)
ExcludeArch:	alpha amd64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Smalltalk is a Free (or Open Source) implementation that closely
follows the Smalltalk-80 language as described in the book
Smalltalk-80: the Language and its Implementation by Adele Goldberg
and David Robson. GNUSmalltalk runs on most versions of Unix or Unix
like systems (GNU/Linux, FreeBSD, etc...). There is even a version for
commercial operating systems like MS-NT.

%description -l pl
GNU Smalltalk jest Woln± (lub Open Source) implementacj± tak blisk±
jêzykowi Smalltalk-80 jak to jest opisane w ksi±¿ce Smalltalk-80: the
Language and its Implementation napisanej przez Adele Goldberg oraz
David Robson. GNUSmalltalk dzia³a na wiêkszo¶ci wersji Unix'ów lub
systemów uniksopodobnych (GNU/Linux, FreeBSD, etc...). Jest nawet
wersja dla systemów komercyjnych, takich jak M$-NT.

%package devel
Summary:	GNU SmallTalk header files
Summary(pl):	Pliki nag³ówkowe dla GNU SmallTalka
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The GNU SmallTalk header files.

%description devel -l pl
Pliki nag³ówkowe dla GNU SmallTalka.

%package static
Summary:	Static libraries for GNU Smalltalk
Summary(pl):	Biblioteki statyczne dla GNU Smalltalka
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
# to be moved to -devel if shared libgst exists
Requires:	gmp-devel
Requires:	readline-devel

%description static
The GNU SmallTalk static libraries.

%description static -l pl
Biblioteki statyczne dla GNU SmallTalka.

%package tk
Summary:	blox-tk module for GNU Smalltalk
Summary(pl):	Modu³ blox-tk dla GNU Smalltalka
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description tk
blox-tk module for GNU Smalltalk.

%description tk -l pl
Modu³ blox-tk dla GNU Smalltalka.

%package gdbm
Summary:	GDBM module for GNU Smalltalk
Summary(pl):	Modu³ GDBM dla GNU Smalltalka
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gdbm
GDBM module for GNU Smalltalk.

%description gdbm -l pl
Modu³ GDBM dla GNU Smalltalka.

%package gtk
Summary:	GTK+ module for GNU Smalltalk
Summary(pl):	Modu³ GTK+ dla GNU Smalltalka
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gtk
GTK+ module for GNU Smalltalk.

%description gtk -l pl
Modu³ GTK+ dla GNU Smalltalka.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1 
%patch3 -p1 
%patch4 -p1 
%patch5 -p1 
%patch6 -p1 

cp -f %{_aclocaldir}/libtool.m4 config

%build
cd sigsegv
%{__aclocal} -I ../config
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../snprintfv
%{__aclocal} -I ../config
%{__autoconf}
%{__autoheader}
# intentionally no automake here
cd ..
%{__libtoolize}
%{__aclocal} -I snprintfv -I config
%{__autoconf}
%{__automake}
%configure \
	AWK=gawk

# gtk things are generated improperly when some locale are set
%{__make} \
	LC_ALL=C

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf ../../bin/gst $RPM_BUILD_ROOT%{_datadir}/gnu-smalltalk/gst

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

# no static modules (*.la used by ltdl)
rm -f $RPM_BUILD_ROOT%{_libdir}/gnu-smalltalk/*.a
# doesn't belong here
rm -rf $RPM_BUILD_ROOT{%{_aclocaldir}/snprintfv.m4,%{_includedir}/snprintfv}

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
%attr (755,root,root) %{_bindir}/gst
%dir %{_libdir}/gnu-smalltalk
%{_libdir}/gnu-smalltalk/libc.la
%attr (755,root,root) %{_libdir}/gnu-smalltalk/i18n*.so
%{_libdir}/gnu-smalltalk/i18n.la
%attr (755,root,root) %{_libdir}/gnu-smalltalk/md5*.so
%{_libdir}/gnu-smalltalk/md5.la
%attr (755,root,root) %{_libdir}/gnu-smalltalk/regex*.so
%{_libdir}/gnu-smalltalk/regex.la
%attr (755,root,root) %{_libdir}/gnu-smalltalk/tcp*.so
%{_libdir}/gnu-smalltalk/tcp.la
%{_datadir}/gnu-smalltalk
%{_infodir}/gst*
%{_mandir}/man1/*
%{_desktopdir}/*
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%attr (755,root,root) %{_bindir}/gst-config
%attr (755,root,root) %{_bindir}/gst-package
%{_includedir}/*.h
%{_aclocaldir}/gst.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
# no shared lib, so it's here... to be moved to -devel if shared exists
%{_libdir}/lib*.la

%files tk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnu-smalltalk/blox-tk*.so
%{_libdir}/gnu-smalltalk/blox-tk.la

%files gdbm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnu-smalltalk/gdbm*.so
%{_libdir}/gnu-smalltalk/gdbm.la

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnu-smalltalk/gst-gtk*.so
%{_libdir}/gnu-smalltalk/gst-gtk.la
