%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	C library for the Flickr API
Name:		flickcurl
Version:	1.23
Release:	1
License:	LGPLv2+
Group:		Networking/File transfer
URL:		http://librdf.org/flickcurl/
Source0:	http://download.dajobe.org/flickcurl/%{name}-%{version}.tar.gz
BuildRequires:	curl-devel
BuildRequires:	libxml2-devel >= 2.6.8
BuildRequires:	raptor2-devel
BuildRequires:	libxslt-devel
BuildRequires:	c-ares-devel
BuildRequires:	gnutls-devel

%description
Flickcurl is a C library for the Flickr API, handling creating the
requests, signing, token management, calling the API, marshalling
request parameters and decoding responses. It uses libcurl to call the
REST web service and libxml2 to manipulate the XML responses. The
current version supports part of the API (see Flickcurl API coverage)
primarily the functions for reading photo, people and tags description,
uploading photos, changing tags and comments.

This package contains some utility programs using the %{name} library.


%package -n %{libname}
Summary:	C library for the Flickr API
Group:		System/Libraries

%description -n %{libname}
Flickcurl is a C library for the Flickr API, handling creating the
requests, signing, token management, calling the API, marshalling
request parameters and decoding responses. It uses libcurl to call the
REST web service and libxml2 to manipulate the XML responses. The
current version supports part of the API (see Flickcurl API coverage)
primarily the functions for reading photo, people and tags description,
uploading photos, changing tags and comments.


%package -n %{develname}
Summary:	Development files for %{libname}
Group:		System/Libraries
Requires:	%{libname} = %{version}
Provides:	%{name}-devel = %{EVRD}
Provides:	lib%{name}-devel = %{EVRD}

%description -n %{develname}
This package contains the developement files for the %{name} library.

%prep
%setup -q

%build
%configure2_5x --disable-static
%make

%install
%makeinstall_std

%files
%doc LICENSE-2.0.txt LICENSE.html AUTHORS
%doc NEWS NEWS.html README README.html ChangeLog coverage.html
%{_bindir}/%{name}
%{_bindir}/flickrdf
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/flickrdf.1.*

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{develname}
%doc NOTICE
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h
%{_bindir}/%{name}-config
%{_mandir}/man1/%{name}-config.1.*
%{_datadir}/gtk-doc/html/flickcurl

%changelog
* Tue Jan 24 2012 Andrey Bondrov <abondrov@mandriva.org> 1.22-1mdv2012.0
+ Revision: 767864
- New version 1.22, disable static

* Sat Apr 02 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 1.21-1
+ Revision: 649817
- update to new version 1.21

* Wed Mar 09 2011 Stéphane Téletchéa <steletch@mandriva.org> 1.20-1
+ Revision: 643208
- update to new version 1.20

* Sun Oct 17 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 1.19-1mdv2011.0
+ Revision: 586324
- update to new version 1.19

* Tue Apr 27 2010 Frederik Himpe <fhimpe@mandriva.org> 1.18-1mdv2010.1
+ Revision: 539833
- update to new version 1.18

* Mon Mar 08 2010 Ahmad Samir <ahmadsamir@mandriva.org> 1.17-1mdv2010.1
+ Revision: 515644
- new upstream release 1.17

* Thu Jan 14 2010 Frederik Himpe <fhimpe@mandriva.org> 1.16-1mdv2010.1
+ Revision: 491544
- update to new version 1.16

* Sun Jan 03 2010 Frederik Himpe <fhimpe@mandriva.org> 1.15-1mdv2010.1
+ Revision: 485872
- update to new version 1.15

* Mon Oct 19 2009 Frederic Crozat <fcrozat@mandriva.com> 1.14-2mdv2010.0
+ Revision: 458257
- Fix BR
- Fix BR
- Fix buildrequires

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - rebuild for new curl SSL backend
    - update to new version 1.14

* Tue Aug 04 2009 Frederik Himpe <fhimpe@mandriva.org> 1.13-1mdv2010.0
+ Revision: 409384
- Update to new version 1.13

* Tue Feb 17 2009 Jérôme Soyer <saispo@mandriva.org> 1.8-1mdv2009.1
+ Revision: 341534
- New upstream release

* Sun Dec 07 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.7-1mdv2009.1
+ Revision: 311657
- update to new version 1.7

* Fri Sep 05 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.6-1mdv2009.0
+ Revision: 281107
- update to new version 1.6

* Sat Aug 23 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.5-1mdv2009.0
+ Revision: 275321
- update to new version 1.5

* Fri Aug 01 2008 Pascal Terjan <pterjan@mandriva.org> 1.4-1mdv2009.0
+ Revision: 259455
- 1.4

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed May 28 2008 Nicolas Vigier <nvigier@mandriva.com> 1.3-1mdv2009.0
+ Revision: 212645
- update to version 1.3

  + Thierry Vignaud <tv@mandriva.org>
    - fix no-buildroot-tag

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - new version

* Thu Dec 27 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.13-1mdv2008.1
+ Revision: 138246
- new version
- drop sources 2,3,4 merged upstream
- do not package COPYING files
- new license policy
- spec file clean

* Mon Aug 13 2007 Nicolas Vigier <nvigier@mandriva.com> 0.12-1mdv2008.0
+ Revision: 62431
- new version

* Mon Aug 06 2007 Nicolas Vigier <nvigier@mandriva.com> 0.11-1mdv2008.0
+ Revision: 59495
- Import flickcurl

