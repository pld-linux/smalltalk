Summary:	GNU smalltalk
Summary(pl.UTF-8):	GNU smalltalk
Name:		smalltalk
Version:	3.1
Release:	3
License:	GPL
Group:		Development/Languages
Source0:	ftp://ftp.gnu.org/pub/gnu/smalltalk/%{name}-%{version}.tar.gz
# Source0-md5:	fb4630a86fc47c893cf9eb9adccd4851
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-proc.patch
URL:		http://www.gnu.org/software/smalltalk/
BuildRequires:	OpenGL-devel
BuildRequires:	OpenGL-glut
BuildRequires:	SDL-devel
BuildRequires:	atk-devel >= 1.0.0
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	gawk
BuildRequires:	gdbm-devel
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 1:2.0.0
BuildRequires:	libffi-devel
BuildRequires:	libltdl-devel
BuildRequires:	libsigsegv
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

%package sdl
Summary:	SDL module for GNU Smalltalk
Summary(pl.UTF-8):	Moduł SDL dla GNU Smalltalka
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description sdl
SDL module for GNU Smalltalk.

%description sdl -l pl.UTF-8
Moduł SDL dla GNU Smalltalka.

%package opengl
summary:	OpenGL module for GNU Smalltalk
Summary(pl.UTF-8):	Moduł OpenGL dla GNU Smalltalka
Group:		Libraries
Requires:	%{name} = %{version}-%{release}

%description opengl
openGL module for GNU Smalltalk.

%description opengl -l pl.UTF-8
Moduł OpenGL dla GNU Smalltalka.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--enable-gtk=yes \
	--enable-disassembler \
	--enable-preemption \
	--with-system-libffi \
	--with-system-libsigsegv \
	AWK=gawk

# gtk things are generated improperly when some locale are set
%{__make} \
	LC_ALL=C

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf ../../bin/gst $RPM_BUILD_ROOT%{_datadir}/smalltalk/gst

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

# no static modules (*.la used by ltdl)
rm -f $RPM_BUILD_ROOT%{_libdir}/smalltalk/*.a
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
%attr(755,root,root) %{_bindir}/gst-remote
%attr(755,root,root) %{_bindir}/gst-sunit
%attr(755,root,root) %{_libdir}/libgst.so.*.*.*
%dir %{_libdir}/smalltalk
%{_libdir}/smalltalk/libc.la
%attr(755,root,root) %{_libdir}/smalltalk/digest*.so
%{_libdir}/smalltalk/digest.la
%attr(755,root,root) %{_libdir}/smalltalk/i18n*.so
%{_libdir}/smalltalk/i18n.la
%attr(755,root,root) %{_libdir}/smalltalk/iconv*.so
%{_libdir}/smalltalk/iconv.la
%attr(755,root,root) %{_libdir}/smalltalk/zlib*.so
%{_libdir}/smalltalk/zlib.la
%attr(755,root,root) %{_libdir}/smalltalk/sockets*.so
%{_libdir}/smalltalk/sockets.la
%attr(755,root,root) %{_libdir}/smalltalk/vfs/*
%{_datadir}/smalltalk
%{_infodir}/gst*
%{_mandir}/man1/gst.1*
%{_mandir}/man1/gst-convert.1*
%{_mandir}/man1/gst-doc.1*
%{_mandir}/man1/gst-load.1*
%{_mandir}/man1/gst-reload.1*
%{_mandir}/man1/gst-sunit.1*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
%dir /var/lib/smalltalk
/var/lib/smalltalk/gst.im

%files devel
%defattr(644,root,root,755)
%attr (755,root,root) %{_bindir}/gst-config
%attr (755,root,root) %{_bindir}/gst-package
%attr(755,root,root) %{_libdir}/libgst.so
%{_libdir}/libgst.la
%{_includedir}/*.h
%{_aclocaldir}/gst.m4
%{_aclocaldir}/gst-package.m4
%{_pkgconfigdir}/gnu-smalltalk.pc
%{_mandir}/man1/gst-config.1*
%{_mandir}/man1/gst-package.1*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgst.a

%files tk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/smalltalk/blox-tk*.so
%{_libdir}/smalltalk/blox-tk.la

%files gdbm
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/smalltalk/gdbm*.so
%{_libdir}/smalltalk/gdbm.la

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/smalltalk/gst-gtk*.so
%{_libdir}/smalltalk/gst-gtk.la

%files sqlite3
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/smalltalk/dbd-sqlite3*.so
%{_libdir}/smalltalk/dbd-sqlite3.la

%files sdl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/smalltalk/sdl*.so
%{_libdir}/smalltalk/sdl.la

%files opengl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/smalltalk/gstglut*.so
%{_libdir}/smalltalk/gstglut.la
%attr(755,root,root) %{_libdir}/smalltalk/gstopengl*.so
%{_libdir}/smalltalk/gstopengl.la
