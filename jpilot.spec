Summary:	Jpilot - Palm Pilot desktop software
Summary(pl):    Program zarz±dzania Palm Pilot'em
Summary(pt_BR):	Software para interação com o Pilot
Name:		jpilot
Version:	0.99
Release:	8
License:	GPL
Group:		X11/Applications
Source0:	http://jpilot.org/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
URL:		http://jpilot.org/
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	pilot-link-devel
ExcludeArch:	s390 s390x
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
J-Pilot is a desktop organizer application for the palm pilot that
runs under Linux. t is similar in functionality to the one that 3com
distributes for a well known rampant legacy operating system.

%description -l pl
J-Pilot jest programem do zarz±dzania organizerami typu Palm Pilot
dla Linux'a z mo¿liwo¶ci± dodawania wtyczek. Posiada zbli¿on± 
funkcjonalno¶æ do oryginalnego oprogramowania 3com'a dla Palm Pilota.

%description -l pt_BR
Um software para interação com o Pilot.

%prep
%setup -q

%build
gettextize --copy --force
%configure
%{__make}
%{__make} jpilot-dump
%{__make} libplugin

(cd Expense
%configure
%{__make}}

(cd SyncTime
%configure
%{__make}}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_datadir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install -C Expense \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} install -C SyncTime \
	DESTDIR=$RPM_BUILD_ROOT

install -d ${RPM_BUILD_ROOT}%{_sysconfdir}/X11/applnk/Applications
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/applnk/Applications/jpilot.desktop

#install man pages
install docs/jpilot*.1 $RPM_BUILD_ROOT%{_mandir}/man1

gzip -9nf BUGS README TODO CREDITS

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/jpilot
%{_libdir}/%{name}
%config(noreplace) %{_sysconfdir}/X11/applnk/Applications/jpilot.desktop
