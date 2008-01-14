%define libxdmcp %mklibname xdmcp 6
Name: libxdmcp
Summary: X Display Manager Control Protocol library
Version: 1.0.2
Release: %mkrel 4
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXdmcp-%{version}.tar.bz2
Patch0: libxdmcp-visibility.patch
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel		>= 7.3
BuildRequires: x11-util-macros		>= 1.1.5

%description
X Display Manager Control Protocol library

#-----------------------------------------------------------

%package -n %{libxdmcp}
Summary: Development files for %{name}
Group: Development/X11
Conflicts: libxorg-x11 < 7.0
Provides: %{name} = %{version}

%description -n %{libxdmcp}
X Display Manager Control Protocol library

#-----------------------------------------------------------

%package -n %{libxdmcp}-devel
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libxdmcp} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libxdmcp-devel = %{version}-%{release}

Conflicts: libxorg-x11-devel < 7.0

%description -n %{libxdmcp}-devel
Development files for %{name}

%pre -n %{libxdmcp}-devel
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{libxdmcp}-devel
%defattr(-,root,root)
%{_libdir}/libXdmcp.la
%{_libdir}/libXdmcp.so
%{_libdir}/pkgconfig/xdmcp.pc
%{_includedir}/X11/Xdmcp.h

#-----------------------------------------------------------

%package -n %{libxdmcp}-static-devel
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{libxdmcp}-devel = %{version}
Provides: libxdmcp-static-devel = %{version}-%{release}

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{libxdmcp}-static-devel
Static development files for %{name}

%files -n %{libxdmcp}-static-devel
%defattr(-,root,root)
%{_libdir}/libXdmcp.a

#-----------------------------------------------------------

%prep
%setup -q -n libXdmcp-%{version}
%patch0 -p1 -b .visibility

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -n %{libxdmcp}
%defattr(-,root,root)
%{_libdir}/libXdmcp.so.6
%{_libdir}/libXdmcp.so.6.0.0


