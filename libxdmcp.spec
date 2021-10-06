# libxdmcp is used by wine and steam -- 32-bit package needed
%define major 6
%define libname %mklibname xdmcp %{major}
%define devname %mklibname xdmcp -d
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif
%if %{with compat32}
%define lib32name libxdmcp%{major}
%define dev32name libxdmcp-devel
%endif

%global optflags %{optflags} -O3

Summary:	X Display Manager Control Protocol library
Name:		libxdmcp
Version:	1.1.3
Release:	4
Group:		Development/X11
License:	MIT
Url:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXdmcp-%{version}.tar.bz2
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(xproto)
BuildRequires:	pkgconfig(libbsd)
%if %{with compat32}
BuildRequires:	devel(libbsd)
%endif

%description
X Display Manager Control Protocol library.

%package -n %{libname}
Summary:	Development files for %{name}
Group:		Development/X11

%description -n %{libname}
X Display Manager Control Protocol library.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
Development files for %{name}.

%if %{with compat32}
%package -n %{lib32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11

%description -n %{lib32name}
X Display Manager Control Protocol library.

%package -n %{dev32name}
Summary:	Development files for %{name} (32-bit)
Group:		Development/X11
Requires:	%{lib32name} = %{version}-%{release}
Requires:	%{devname} = %{version}-%{release}

%description -n %{dev32name}
Development files for %{name}.
%endif

%prep
%autosetup -n libXdmcp-%{version} -p1
export CONFIGURE_TOP="`pwd`"
%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif
mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%files -n %{libname}
%{_libdir}/libXdmcp.so.%{major}*

%files -n %{devname}
%{_datadir}/doc/libXdmcp/xdmcp.*
%{_libdir}/libXdmcp.so
%{_libdir}/pkgconfig/xdmcp.pc
%{_includedir}/X11/Xdmcp.h

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libXdmcp.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/libXdmcp.so
%{_prefix}/lib/pkgconfig/*.pc
%endif
