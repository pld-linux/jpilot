Summary: Jpilot pilot desktop software
Name: jpilot
Version: 0.99
Release: 7
License: GPL
Group: Applications/Productivity
URL: http://jpilot.org
Source: http://jpilot.org/jpilot-%{version}.tar.gz
Source1: jpilot.desktop
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildPrereq: gtk+-devel >= 1.2.0, pilot-link-devel
Requires: gtk+ >= 1.2.0 , pilot-link
PreReq: /sbin/ldconfig
ExcludeArch: s390 s390x

%description
J-Pilot is a desktop organizer application for the palm pilot that runs under
Linux. t is similar in functionality to the one that 3com distributes for a
well known rampant legacy operating system.

%prep
%setup -q

%build
%configure
make
make jpilot-dump
make libplugin

pushd Expense
  %configure
  make
popd

pushd SyncTime
    %configure
    make
popd

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT{%{_bindir},%{_libdir},%{_datadir},%{_mandir}/man1}
%makeinstall 

pushd Expense
  %makeinstall
popd

pushd SyncTime
    %makeinstall
popd

mkdir -p ${RPM_BUILD_ROOT}/etc/X11/applnk/Applications
install -m644 %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/Applications/jpilot.desktop

#install man pages
install -m 644 docs/jpilot*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc BUGS README COPYING TODO CREDITS INSTALL  
%{_bindir}/*
%{_datadir}/jpilot
%{_libdir}/%{name}
%config(noreplace) /etc/X11/applnk/Applications/jpilot.desktop

%changelog
* Sun Aug  5 2001 Than Ngo <than@redhat.com>
- fix bug #50586

* Mon Jul 16 2001 Trond Eivind Glomsrød <teg@redhat.com>
- s/Copyright/License/
- Improve langification
- mark desktop file as config(noreplace)
- move dependency on ldconfig from requires to prereq

* Sat Jul  7 2001 Tim Powers <timp@redhat.com>
- languify to satisfy rpmlint

* Fri Jun 29 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- delete Packager: line in spec file

* Tue Jun 26 2001 Florian La Roche <Florian.LaRoche@redhat.de>
- exclude s390,s390x

* Fri Jun 22 2001 Preston Brown <pbrown@redhat.com>
- build for dist

* Thu Feb  8 2001 Tim Powers <timp@redhat.com>
- updated to 0.99, bug fixes/feature enhancements

* Tue Dec 19 2000 Tim Powers <timp@redhat.com>
- rebuilt. For some reason buildsystem made the dirs 777 again. Now
  it's fine.

* Fri Dec 15 2000 Tim Powers <timp@redhat.com>
- fixd bad dir perms for ~/.jpilot (was creating them as 777, needs to
  be 700 for security purposes
- no devel package, was a waste to do that when only two files are included
- use %%makeinstall, and predefined macros for dirs so that if
  %%configure and %%makeinstall change it can be picked up without
  further editing of the files section
- changed Copyright, it's GPL'ed
 
* Thu Nov 23 2000 Than Ngo <than@redhat.com>
- add missing plugin library and jpilot-dump
- made devel package
- clean up spec file

* Mon Jul 24 2000 Prospector <prospector@redhat.com>
- rebuilt

* Mon Jul 10 2000 Tim Powers <timp@redhat.com>
- rebuilt

* Fri Jun 30 2000 Prospector <bugzilla@redhat.com>
- automatic rebuild

* Mon May 15 2000 Tim Powers <timp@redhat.com>
- using applnk now instead of a GNOME specific menu entry
- built for 7.0

* Wed Apr 19 2000 Tim Powers <timp@redhat.com>
- added desktop entry for GNOME

* Wed Apr 12 2000 Tim Powers <timp@redhat.com>
- updated to 0.98.1

* Mon Apr 3 2000 Tim Powers <timp@redhat.com>
- updated to 0.98
- bzipped source
- using percent configure instead of ./configure
- quiet setup
- minor spec file cleanups

* Tue Dec 21 1999 Tim Powers <timp@redhat.com>
- changed requires

* Mon Oct 25 1999 Tim Powers <timp@redhat.com>
- changed group to Applications/Productivity
- first build
