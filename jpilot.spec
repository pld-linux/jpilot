#
# Conditional build:
# _with_gtk1	- use GTK+ 1.2 instead of GTK+2
#
Summary:	Desktop organizer application for PalmOS devices
Summary(pl):	Organizer dla urz±dzeñ PalmOS
Summary(pt_BR):	Software para interação com o Pilot
Name:		jpilot
Version:	0.99.5
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://jpilot.org/%{name}-%{version}.tar.gz
# Source0-md5:	6ee51e69838c826c4ed8fd42ef12cc59
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-configure.patch
Patch1:		%{name}-makefile.patch
URL:		http://jpilot.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
%{?_with_gtk1:BuildRequires:	gtk+-devel >= 1.2.0}
%{!?_with_gtk1:BuildRequires:  gtk+2-devel >= 2.0.3}
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	openssl-devel
BuildRequires:	pilot-link-devel >= 0.11.5
BuildRequires:	readline-devel
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
%{?_with_gtk1:echo 'AC_DEFUN([AM_PATH_GTK_2_0],[$3])' >> acinclude.m4}
%{!?_with_gtk1:echo 'AC_DEFUN([AM_PATH_GTK],[$3])' >> acinclude.m4}
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?_with_gtk1:--enable-gtk2}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_datadir},%{_mandir}/man1}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Utilities/jpilot.desktop

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
%{_applnkdir}/Utilities/jpilot.desktop
