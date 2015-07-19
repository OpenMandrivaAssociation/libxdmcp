%define major 6
%define libname %mklibname xdmcp %{major}
%define devname %mklibname xdmcp -d

Summary:	X Display Manager Control Protocol library
Name:		libxdmcp
Version:	1.1.2
Release:	2
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXdmcp-%{version}.tar.bz2
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)

%description
X Display Manager Control Protocol library.

%package -n %{libname}
Summary:	Development files for %{name}
Group:		Development/X11
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
X Display Manager Control Protocol library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%prep
%setup -qn libXdmcp-%{version}
%apply_patches

%build
%configure \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/libXdmcp.so.%{major}*

%files -n %{devname}
%{_datadir}/doc/libXdmcp/xdmcp.*
%{_libdir}/libXdmcp.so
%{_libdir}/pkgconfig/xdmcp.pc
%{_includedir}/X11/Xdmcp.h

