%define major 6
%define libxdmcp %mklibname xdmcp %{major}
%define develname %mklibname xdmcp -d

Name: libxdmcp
Summary: X Display Manager Control Protocol library
Version: 1.1.0
Release: 5
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXdmcp-%{version}.tar.bz2

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

%description
X Display Manager Control Protocol library

%package -n %{libxdmcp}
Summary: Development files for %{name}
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxdmcp}
X Display Manager Control Protocol library

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libxdmcp} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}
Obsoletes: %{_lib}xdmcp6-devel
Obsoletes: %{_lib}xdmcp-static-devel
Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%prep
%setup -qn libXdmcp-%{version}

%build
%configure2_5x \
	--disable-static \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%files -n %{libxdmcp}
%{_libdir}/libXdmcp.so.%{major}*

%files -n %{develname}
%_datadir/doc/libXdmcp/xdmcp.xml
%{_libdir}/libXdmcp.so
%{_libdir}/pkgconfig/xdmcp.pc
%{_includedir}/X11/Xdmcp.h

