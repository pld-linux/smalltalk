Summary:	GNU smalltalk
Summary(pl):	GNU smalltalk
Name:		smalltalk
Version:	2.1.5
Release:	1
License:	GPL
Group:		Development/Languages
Source0:	ftp://ftp.gnu.org/pub/gnu/smalltalk/%{name}-%{version}.tar.gz
# Source0-md5:	ce993e99f7f3f65958840e4be7a3036e
Source1:	%{name}.desktop
Source2:	%{name}.png
#Patch0:		%{name}-info.patch
Patch1:		%{name}-PACKAGE.patch
Patch2:		%{name}-enums.patch
Icon:		smalltalk.xpm
BuildRequires:	atk-devel >= 1.0.0
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gawk
BuildRequires:	gdbm-devel
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	pango-devel >= 1.0.0
BuildRequires:	pkgconfig
BuildRequires:	readline-devel >= 4.2
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
Group:		Libraries
Requires:	%{name} = %{version}

%description devel
The GNU SmallTalk header files.

%description devel -l pl
Pliki nag³ówkowe dla GNU SmallTalka.

%package static
Summary:	Static libraries for GNU Smalltalk
Summary(pl):	Biblioteki statyczne dla GNU Smalltalka
Group:		Libraries
Requires:	%{name}-devel = %{version}

%description static
The GNU SmallTalk static libraries.

%description static -l pl
Biblioteki statyczne dla GNU SmallTalka.

%prep
%setup -q
#%patch0 -p1
%patch1 -p1
%patch2 -p1 

%build
%{__aclocal} -I snprintfv -I config
%{__autoconf}
%{__automake}
%configure \
	AWK=gawk
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Development,%{_pixmapsdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ln -sf ../../bin/gst $RPM_BUILD_ROOT%{_datadir}/gnu-smalltalk/gst

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Development
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

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
%attr (755,root,root) %{_libdir}/gnu-smalltalk/*.so
%{_datadir}/gnu-smalltalk
%{_infodir}/gst*
%{_mandir}/man1/*
%{_applnkdir}/Development/*
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%attr (755,root,root) %{_bindir}/gst-config
%attr (755,root,root) %{_bindir}/gst-package
%{_libdir}/lib*.la
%{_libdir}/gnu-smalltalk/*.la
%{_includedir}/*
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%{_libdir}/gnu-smalltalk/*.a
