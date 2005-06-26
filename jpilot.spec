#
# Conditional build:
%bcond_with	gtk1	# use GTK+ 1.2 instead of GTK+2
#
Summary:	Desktop organizer application for PalmOS devices
Summary(pl):	Organizer dla urz±dzeñ PalmOS
Summary(pt_BR):	Software para interação com o Pilot
Name:		jpilot
Version:	0.99.7
Release:	4
License:	GPL
Group:		X11/Applications
Source0:	http://jpilot.org/%{name}-%{version}.tar.gz
# Source0-md5:	11bb7236702e2e4c7e3d06372bdc9695
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-locale-names.patch
Patch1:		%{name}_other.v0_99_7.diff
URL:		http://jpilot.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
%{?with_gtk1:BuildRequires:	gtk+-devel >= 1.2.0}
%{!?with_gtk1:BuildRequires:	gtk+2-devel >= 1:2.0.3}
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pilot-link-devel >= 0.11.5
BuildRequires:	pkgconfig
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

mv -f po/{no,nb}.po
rm -f po/stamp-po

%{__perl} -pi -e 's@pilot_prefix/lib /usr/lib@pilot_prefix/%{_lib} /usr/%{_lib}@' configure.in
%{__perl} -pi -e 's@/lib/jpilot/plugins@/%{_lib}/jpilot/plugins@' */Makefile.am

%build
%{?with_gtk1:echo 'AC_DEFUN([AM_PATH_GTK_2_0],[$3])' >> acinclude.m4}
%{!?with_gtk1:echo 'AC_DEFUN([AM_PATH_GTK],[$3])' >> acinclude.m4}
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	ABILIB="%{_lib}" \
	%{!?with_gtk1:--enable-gtk2}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -D %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/jpilot.desktop

# plugins are dlopened by *.so
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS UPGRADING README TODO icons docs/{*.png,*.jpg,*.html}
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.so*
#%{_datadir}/jpilot
%{_mandir}/man1/*
%{_desktopdir}/jpilot.desktop
