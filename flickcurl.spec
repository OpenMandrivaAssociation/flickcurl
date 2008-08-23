%define major 0
%define libname %mklibname %{name} %{major}
%define devname %mklibname %{name} -d

Summary:	C library for the Flickr API
Name:		flickcurl
Version:	1.5
Release:	%mkrel 1
License:	LGPLv2+
Group:		Networking/File transfer
URL:		http://librdf.org/flickcurl/
Source0:	http://download.dajobe.org/flickcurl/%{name}-%{version}.tar.gz
Source1:	http://download.dajobe.org/flickcurl/%{name}-%{version}.tar.gz.asc
BuildRequires:	curl-devel
BuildRequires:	libxml2-devel >= 2.6.8
BuildRequires:	raptor-devel >= 1.4.14
BuildRequires:	libxslt-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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


%package -n %{devname}
Summary:	Development files for %{libname}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Provides:	lib%{name}-devel = %{version}-%{release}

%description -n %{devname}
This package contains the developement files for the %{name} library.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%{__rm} -Rf %{buildroot}
%makeinstall_std

%clean
%{__rm} -Rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%doc LICENSE-2.0.txt LICENSE.html AUTHORS
%doc NEWS NEWS.html README README.html ChangeLog coverage.html
%{_bindir}/%{name}
%{_bindir}/flickrdf
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/flickrdf.1.*

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{devname}
%doc NOTICE
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.la
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h
%{_bindir}/%{name}-config
%{_mandir}/man1/%{name}-config.1.*
%{_datadir}/gtk-doc/html/flickcurl
