Summary:	Desktop organizer application for PalmOS devices
Summary(pl):	Organizer dla urz±dzeñ PalmOS
Summary(pt_BR):	Software para interação com o Pilot
Name:		jpilot
Version:	0.99.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://jpilot.org/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-configure.patch
Patch1:		%{name}-makefile.patch
URL:		http://jpilot.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel >= 1.2.0
BuildRequires:	libtool
BuildRequires:	pilot-link-devel >= 0.11.5
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
J-Pilot is a desktop organizer application for the PalmOS devices that
runs under Linux with plugins support. It is similar in functionality 
to the original Palm Desktop software.

%description -l pl
J-Pilot jest programem do zarz±dzania urz±dzeniami PalmOS dla Linuksa
z mo¿liwo¶ci± dodawania wtyczek. Posiada zbli¿on± funkcjonalno¶æ do
oryginalnego oprogramowania Palm Desktop.

%description -l pt_BR
Um software para interação com o Pilot.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_datadir},%{_mandir}/man1}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d ${RPM_BUILD_ROOT}%{_sysconfdir}/X11/applnk/Applications
install %{SOURCE1} $RPM_BUILD_ROOT%{_sysconfdir}/X11/applnk/Applications/jpilot.desktop

#install man pages
install docs/jpilot*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS UPGRADING README TODO icons docs/{*.png,*.jpg,*.html}
%attr(755,root,root) %{_bindir}/*
%{_datadir}/jpilot
%{_mandir}/man1/*
%{_libdir}/%{name}
%config(noreplace) %{_sysconfdir}/X11/applnk/Applications/jpilot.desktop
