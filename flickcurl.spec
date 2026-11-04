%define major 0
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

# This 2016 code calls malloc, free, and atoi without a declaration.
# Clang reports "use of undeclared identifier"; the warning flag does not declare them.
%global optflags %{optflags} -Wno-implicit-function-declaration -include stdlib.h

Summary:	C library for the Flickr API
Name:		flickcurl
Version:	1.26
Release:	3
License:	LGPLv2+
Group:		Networking/File transfer
URL:		https://librdf.org/flickcurl/
Source0:	http://download.dajobe.org/flickcurl/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool-base
BuildRequires:	slibtool
BuildRequires:	make
BuildRequires:	curl-devel
BuildRequires:	pkgconfig(libxml-2.0) >= 2.6.8
BuildRequires:	raptor2-devel
BuildRequires:	pkgconfig(libxslt)
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
%make_build

%install
%make_install

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
