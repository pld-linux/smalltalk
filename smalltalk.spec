Summary:	GNU smalltalk (No X support)
Summary(pl):	GNU smalltalk (Bez wsparcia dla X)
Name:		smalltalk
Version:	1.95.1
Release:	3
License:	GPL
Group:		Development/Languages
Group(de):	Entwicklung/Sprachen
Group(pl):	Programowanie/Jêzyki
Source0:	ftp://prep.ai.mit.edu/pub/gnu/smalltalk/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-info.patch
Patch1:		%{name}-install.patch
Icon:		smalltalk.xpm
BuildRequires:	readline-devel >= 4.2
BuildRequires:	ncurses-devel >= 5.0
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
jêzykowi Smalltalk-80 jak to jest opisane w ksi±¿ce
Smalltalk-80: the Language and its Implementation napisanej przez
Adele Goldberg oraz David Robson. GNUSmalltalk dzia³a na wiêkszo¶ci
wersji Unix'ów lub systemów Unixo-podobnych (GNU/Linux, FreeBSD, etc...).
Jest nawet wersja dla systemów komercyjnych, takich jak M$-NT.

%package devel
Summary:	GNU SmallTalk header files
Summary(pl):	Pliki nag³ówkowe dla GNU SmallTalka
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name} = %{version}

%description devel
The GNU SmallTalk header files.

%description devel -l pl
Pliki nag³ówkowe dla GNU SmallTalka.

%package static
Summary:	Static libraries for GNU Smalltalk
Summary(pl):	Biblioteki statyczne dla GNU Smalltalka
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Requires:	%{name}-devel = %{version}

%description static
The GNU SmallTalk static libraries.

%description static -l pl
Biblioteki statyczne dla GNU SmallTalka.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Development,%{_pixmapsdir}}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

ln -sf ../../bin/gst $RPM_BUILD_ROOT%{_datadir}/gnu-smalltalk/gst

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Development
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

gzip -9nf AUTHORS NEWS README THANKS

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%attr (755,root,root) %{_bindir}/gst
%{_datadir}/gnu-smalltalk
%{_infodir}/*
%{_mandir}/man1/*
%{_applnkdir}/Development/*
%{_prefix}/X11R6/share/pixmaps/*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr (755,root,root) %{_bindir}/gst-config
%attr (755,root,root) %{_bindir}/gst-package
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgst.a
