Summary:	GNU smalltalk (No X support)
Summary(pl):	GNU smalltalk (Bez wsparcia dla X)
Name:		smalltalk
Version:	1.7
Release:	1
License:	GPL
Group:		Development/Languages
Group(pl):	Programowanie/Jêzyki
Icon:		smalltalk.xpm
Source0:	ftp://prep.ai.mit.edu/pub/gnu/smalltalk/%{name}-%{version}.tar.gz
Source1:	smalltalk.desktop
Source2:	smalltalk.xpm
Patch0:		smalltalk-DESTDIR.patch
Patch1:		smalltalk-info.patch
PreReq:		/usr/sbin/fix-info-dir
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel >= 5.0
BuildRoot:	/tmp/%{name}-%{version}-root

%define _applnkdir %{_prefix}/X11R6/share/applnkdir

%description
The GNU smalltalk interpreter.

%description -l pl
GNU interpreter smalltalka

%package devel
Summary:	GNU SmallTalk header files
Summary(pl):	Pliki nag³ówkowe dla GNU SmallTalka
Group:		Libraries
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
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure
make

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT/{%{_includedir},%{_mandir}/man1,%{_infodir}} \
	$RPM_BUILD_ROOT/{%{_applnkdir},%{_datadir}/pixmaps}

make DESTDIR=$RPM_BUILD_ROOT install

ln -sf ../../bin/gst $RPM_BUILD_ROOT%{_datadir}/gnu-smalltalk/gst

gzip -9nf README docs/{AUTHORS,ChangeLog*,stamp-classes,todo,categories} \
	docs/NEWS $RPM_BUILD_ROOT{%{_mandir}/man1/*,%{_infodir}/*}

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/minicom.xpm
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/minicom.desktop

%post
%{_sbindir}/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
%{_sbindir}/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc README.gz docs/AUTHORS.gz docs/ChangeLog*.gz
%doc docs/DOM.html docs/stamp-classes.gz
%doc docs/todo.gz docs/NEWS.gz docs/categories.gz
%doc emacs
%attr (755,root,root) %{_bindir}/gst
%{_datadir}/gnu-smalltalk
%{_infodir}/*
%{_mandir}/man1/*
%{_applnkdir}/*
%{_datadir}/pixmaps/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/libgst.a
