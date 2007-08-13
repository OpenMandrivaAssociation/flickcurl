%define name flickcurl
%define version 0.12
%define release %mkrel 1
%define major 0
%define libname %mklibname %name %major
%define devname %mklibname -d %name

Name:		%name
Version:	%version
Release:	%release
Summary:	C library for the Flickr API
Source0:	http://download.dajobe.org/flickcurl/%{name}-%{version}.tar.gz
Source1:	http://download.dajobe.org/flickcurl/%{name}-%{version}.tar.gz.asc
# manpages taken from debian package
Source2:	%{name}.1
Source3:	flickrdf.1
Source4:	%{name}-config.1
URL:		http://librdf.org/flickcurl/
License:	LGPLv2 or ASL 2.0
Group:		Networking/File transfer
BuildRequires:	curl-devel, libxml2-devel >= 2.6.8, raptor-devel >= 1.4.14
BuildRequires:	libxslt-devel
%description
Flickcurl is a C library for the Flickr API, handling creating the
requests, signing, token management, calling the API, marshalling
request parameters and decoding responses. It uses libcurl to call the
REST web service and libxml2 to manipulate the XML responses. The
current version supports part of the API (see Flickcurl API coverage)
primarily the functions for reading photo, people and tags description,
uploading photos, changing tags and comments.

This package contains some utility programs using the %{name} library.


%package -n %libname
Summary:	C library for the Flickr API
Group:		System/Libraries

%description -n %libname
Flickcurl is a C library for the Flickr API, handling creating the
requests, signing, token management, calling the API, marshalling
request parameters and decoding responses. It uses libcurl to call the
REST web service and libxml2 to manipulate the XML responses. The
current version supports part of the API (see Flickcurl API coverage)
primarily the functions for reading photo, people and tags description,
uploading photos, changing tags and comments.


%package -n %devname
Summary:	Development files for %libname
Group:		System/Libraries
Requires:	%{libname} = %{version}
Provides:	%name-devel = %version-%release, lib%{name}-devel = %version-%release

%description -n %devname
This package contains the developement files for the %{name} library.


%prep
%setup -q
%{__cp} -p %{SOURCE2} %{SOURCE3} %{SOURCE4} .

%build
%configure
%make
for file in %{name}.1 flickrdf.1 %{name}-config.1
do
  %{__lzma} $file
done

%install
%{__rm} -Rf %{buildroot}
%makeinstall
%{__mkdir} -p %{buildroot}%{_mandir}/man1
%{__cp} -p *.1.lzma %{buildroot}%{_mandir}/man1

%post -n %{libname} -p /sbin/ldconfig

%postun -n %{libname} -p /sbin/ldconfig

%files
%doc LICENSE-2.0.txt LICENSE.html AUTHORS COPYING COPYING.LIB
%doc NEWS NEWS.html README README.html ChangeLog coverage.html
%{_bindir}/%{name}
%{_bindir}/flickrdf
%{_mandir}/man1/%{name}.1.*
%{_mandir}/man1/flickrdf.1.*

%files -n %libname
%{_libdir}/lib%{name}.so.%{major}*

%files -n %devname
%doc NOTICE
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.la
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}.h
%{_bindir}/%{name}-config
%{_mandir}/man1/%{name}-config.1.*

