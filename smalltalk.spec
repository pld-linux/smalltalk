Summary:	GNU smalltalk
Summary(pl):	GNU smalltalk
Name:		smalltalk
Version:	2.1.5
Release:	2
License:	GPL
Group:		Development/Languages
Source0:	ftp://ftp.gnu.org/pub/gnu/smalltalk/%{name}-%{version}.tar.gz
# Source0-md5:	ce993e99f7f3f65958840e4be7a3036e
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-info.patch
Patch1:		%{name}-PACKAGE.patch
Patch2:		%{name}-enums.patch
Patch3:		%{name}-nolibs.patch
Icon:		smalltalk.xpm
BuildRequires:	atk-devel >= 1.0.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gawk
BuildRequires:	gdbm-devel
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	libtool >= 2:1.5
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pango-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRequires:	readline-devel >= 4.2
BuildRequires:	tk-devel >= 8.4
#BuildRequires:  xemacs
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
systemów Unixo-podobnych (GNU/Linux, FreeBSD, etc...). Jest nawet
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
Summary:	GTK module for GNU Smalltalk
Summary(pl):	Modu³ GTK dla GNU Smalltalka
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gtk
GTK module for GNU Smalltalk.

%description gtk -l pl
Modu³ GTK dla GNU Smalltalka.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1 
%patch3 -p1 

%build
cd libltdl
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../sigsegv
%{__libtoolize}
%{__aclocal} -I ../config
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../snprintfv
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
# intentionally no automake here
cd ..
%{__libtoolize}
%{__aclocal} -I snprintfv -I config
%{__autoconf}
%{__automake}
%configure \
	AWK=gawk \
%ifarch sparc sparc64 sparcv9
	gst_cv_double_alignment=8 \
	gst_cv_long_double_alignment=8
# alignment test is too weak for sparc (it can perform only some instructions
# on misaligned doubles; e.g. ldd seems to work, but std on %%o4 causes SIGBUS)
%endif

%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Development,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf ../../bin/gst $RPM_BUILD_ROOT%{_datadir}/gnu-smalltalk/gst

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Development
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
%{_applnkdir}/Development/*
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
