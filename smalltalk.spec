Summary:	GNU smalltalk (No X or emacs support)
Summary(pl):	GNU smalltalk (Bez wsparcia dla X lub emacsa)
Name:		smalltalk
Version:	1.6.2
Release:	4
Copyright:	GPL
Group:		Development/Languages
Group(pl):	Programowanie/J�zyki
Source:		ftp://prep.ai.mit.edu/pub/gnu/%{name}-%{version}.tar.gz
Patch0:		smalltalk-makefile.patch
Patch1:		smalltalk-sysdep.patch
Patch2:		smalltalk-info.patch
PreReq:		/usr/sbin/fix-info-dir
BuildRequires:	readline-devel
BuildRequires:	ncurses-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The GNU smalltalk interpreter.

%description -l pl
GNU interpreter smalltalka

%package devel
Summary:	GNU SmallTalk header files
Summary(pl):	Pliki nag��wkowe dla GNU SmallTalka
Group:		Libraries
Group(pl):	Biblioteki

%description devel
The GNU SmallTalk header files.

%description devel -l pl
Pliki nag��wkowe dla GNU SmallTalka.

%package static
Summary:	Static libraries for GNU Smalltalk
Summary(pl):	Biblioteki statyczne dla GNU Smalltalka
Group:		Libraries
Group(pl):	Biblioteki

%description static
The GNU SmallTalk static libraries.

%description static -l pl
Biblioteki statyczne dla GNU SmallTalka.

%prep
%setup -q
%patch0 -p0
%patch1 -p0
%patch2 -p1

%build
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure
make

%clean
rm -rf $RPM_BUILD_ROOT

%install
rm -rf $RPM_BUILD_ROOT

make DESTDIR=$RPM_BUILD_ROOT install 

gzip -9nf README docs/AUTHORS \
	$RPM_BUILD_ROOT{%{_mandir}/man1/*,%{_infodir}/*}

%post
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
/usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr (644,root,root,755)
%doc README.gz docs/AUTHORS.gz
%attr (755,root,root) %{_bindir}/gst
%{_datadir}/smalltalk
%{_infodir}/*
%{_mandir}/man1/*

%files devel
%defattr (644,root,root,755)
%{_includedir}/*

%files static
%defattr (644,root,root,755)
%{_libdir}/libgst.a
