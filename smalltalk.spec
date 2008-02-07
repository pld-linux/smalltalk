Summary:	GNU smalltalk
Summary(pl.UTF-8):	GNU smalltalk
Name:		smalltalk
Version:	3.0.1
Release:	0.1
License:	GPL
Group:		Development/Languages
Source0:	ftp://ftp.gnu.org/pub/gnu/smalltalk/%{name}-%{version}.tar.gz
# Source0-md5:	dbd1bc308dda3a4ef936dce2b78faa5a
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-PACKAGE.patch
Patch1:		%{name}-proc.patch
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
BuildRequires:	sqlite3-devel
BuildRequires:	rpmbuild(macros) >= 1.213
BuildRequires:	texinfo
BuildRequires:	tk-devel >= 8.4
#BuildRequires:	xemacs
Requires(post,postun):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNU Smalltalk is a Free (or Open Source) implementation that closely
follows the Smalltalk-80 language as described in the book
Smalltalk-80: the Language and its Implementation by Adele Goldberg
and David Robson. GNUSmalltalk runs on most versions of Unix or Unix
like systems (GNU/Linux, FreeBSD, etc...). There is even a version for
commercial operating systems like MS-NT.

%description -l pl.UTF-8
GNU Smalltalk jest Wolną (lub Open Source) implementacją tak bliską
językowi Smalltalk-80 jak to jest opisane w książce Smalltalk-80: the
Language and its Implementation napisanej przez Adele Goldberg oraz
David Robson. GNUSmalltalk działa na większości wersji Unix'ów lub
systemów uniksopodobnych (GNU/Linux, FreeBSD, etc...). Jest nawet
wersja dla systemów komercyjnych, takich jak M$-NT.

%package devel
Summary:	GNU SmallTalk header files
Summary(pl.UTF-8):	Pliki nagłówkowe dla GNU SmallTalka
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gmp-devel
Requires:	readline-devel

%description devel
The GNU SmallTalk header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla GNU SmallTalka.

%package static
Summary:	Static libraries for GNU Smalltalk
Summary(pl.UTF-8):	Biblioteki statyczne dla GNU Smalltalka
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
The GNU SmallTalk static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne dla GNU SmallTalka.

%package tk
Summary:	blox-tk module for GNU Smalltalk
Summary(pl.UTF-8):	Moduł blox-tk dla GNU Smalltalka
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description tk
blox-tk module for GNU Smalltalk.

%description tk -l pl.UTF-8
Moduł blox-tk dla GNU Smalltalka.

%package gdbm
Summary:	GDBM module for GNU Smalltalk
Summary(pl.UTF-8):	Moduł GDBM dla GNU Smalltalka
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gdbm
GDBM module for GNU Smalltalk.

%description gdbm -l pl.UTF-8
Moduł GDBM dla GNU Smalltalka.

%package gtk
Summary:	GTK+ module for GNU Smalltalk
Summary(pl.UTF-8):	Moduł GTK+ dla GNU Smalltalka
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description gtk
GTK+ module for GNU Smalltalk.

%description gtk -l pl.UTF-8
Moduł GTK+ dla GNU Smalltalka.

%package sqlite3
Summary:	Sqlite3 module for GNU Smalltalk
Summary(pl.UTF-8):	Moduł Sqlite3 dla GNU Smalltalka
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description sqlite3
Sqlite3 module for GNU Smalltalk.

%description sqlite3 -l pl.UTF-8
Moduł Sqlite3 dla GNU Smalltalka.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 

rm -f config/libtool.m4

%build
cd libffi
%{__aclocal} -I ../build-aux
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../sigsegv
%{__aclocal} -I ../build-aux
%{__autoconf}
%{__autoheader}
%{__automake}
cd ../snprintfv
%{__aclocal} -I ../build-aux
%{__autoconf}
%{__autoheader}
# intentionally no automake here
cd ..
%{__libtoolize}
%{__aclocal} -I snprintfv -I build-aux
%{__autoconf}
%{__automake}
%configure \
	--enable-gtk=yes \
	--enable-disassembler \
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
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/sbin/ldconfig
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS
%attr(755,root,root) %{_bindir}/gst
%attr(755,root,root) %{_bindir}/gst-blox
%attr(755,root,root) %{_bindir}/gst-convert
%attr(755,root,root) %{_bindir}/gst-doc
%attr(755,root,root) %{_bindir}/gst-load
%attr(755,root,root) %{_bindir}/gst-reload
%attr(755,root,root) %{_bindir}/gst-sunit
%attr(755,root,root) %{_libdir}/libgst.so.*.*.*
%attr(755,root,root) %{_libdir}/libsigsegv.so.*.*.*
%dir %{_libdir}/gnu-smalltalk
%{_libdir}/gnu-smalltalk/libc.la
%attr(755,root,root) %{_libdir}/gnu-smalltalk/digest*.so
%{_libdir}/gnu-smalltalk/digest.la
%attr(755,root,root) %{_libdir}/gnu-smalltalk/i18n*.so
%{_libdir}/gnu-smalltalk/i18n.la
%attr(755,root,root) %{_libdir}/gnu-smalltalk/iconv*.so
%{_libdir}/gnu-smalltalk/iconv.la
%attr(755,root,root) %{_libdir}/gnu-smalltalk/tcp*.so
%{_libdir}/gnu-smalltalk/tcp.la
%attr(755,root,root) %{_libdir}/gnu-smalltalk/zlib*.so
%{_libdir}/gnu-smalltalk/zlib.la
%{_libdir}/gnu-smalltalk/deb
%{_libdir}/gnu-smalltalk/lslR
%{_libdir}/gnu-smalltalk/mailfs
%{_libdir}/gnu-smalltalk/patchfs
%{_libdir}/gnu-smalltalk/uar
%{_libdir}/gnu-smalltalk/ucpio
%{_libdir}/gnu-smalltalk/ulha
%{_libdir}/gnu-smalltalk/urar
%{_libdir}/gnu-smalltalk/utar
%{_libdir}/gnu-smalltalk/uzip
%{_libdir}/gnu-smalltalk/uzoo
%{_datadir}/gnu-smalltalk
%{_infodir}/gst*
%{_mandir}/man1/gst.1*
%{_mandir}/man1/gst-convert.1*
%{_mandir}/man1/gst-doc.1*
%{_mandir}/man1/gst-load.1*
%{_mandir}/man1/gst-sunit.1*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
/var/lib/gnu-smalltalk/gst.im

%files devel
%defattr(644,root,root,755)
%attr (755,root,root) %{_bindir}/gst-config
%attr (755,root,root) %{_bindir}/gst-package
%attr(755,root,root) %{_libdir}/libgst.so
%attr(755,root,root) %{_libdir}/libsigsegv.so
%{_libdir}/libgst.la
%{_libdir}/libsigsegv.la
%{_includedir}/*.h
%{_aclocaldir}/gst.m4
%{_aclocaldir}/gst-package.m4
%{_pkgconfigdir}/gnu-smalltalk.pc
%{_mandir}/man1/gst-config.1*
%{_mandir}/man1/gst-package.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgst.a
%{_libdir}/libsigsegv.a

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

%files sqlite3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/gnu-smalltalk/dbd-sqlite3*.so
%{_libdir}/gnu-smalltalk/dbd-sqlite3.la
