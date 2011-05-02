%define libxdmcp %mklibname xdmcp 6
%define develname %mklibname xdmcp -d
%define staticname %mklibname xdmcp -s -d

Name: libxdmcp
Summary: X Display Manager Control Protocol library
Version: 1.1.0
Release: %mkrel 3
Group: Development/X11
License: MIT
URL: http://xorg.freedesktop.org
Source0: http://xorg.freedesktop.org/releases/individual/lib/libXdmcp-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: x11-proto-devel >= 1.0.0
BuildRequires: x11-util-macros >= 1.0.1

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

%package -n %{develname}
Summary: Development files for %{name}
Group: Development/X11
Requires: %{libxdmcp} = %{version}
Requires: x11-proto-devel >= 1.0.0
Provides: libxdmcp-devel = %{version}-%{release}
Provides: libxdmcp6-devel = %{version}-%{release}
Obsoletes: %{mklibname xdmcp6}-devel

Conflicts: libxorg-x11-devel < 7.0

%description -n %{develname}
Development files for %{name}

%pre -n %{develname}
if [ -h %{_includedir}/X11 ]; then
	rm -f %{_includedir}/X11
fi

%files -n %{develname}
%defattr(-,root,root)
%_datadir/doc/libXdmcp/xdmcp.xml
%{_libdir}/libXdmcp.la
%{_libdir}/libXdmcp.so
%{_libdir}/pkgconfig/xdmcp.pc
%{_includedir}/X11/Xdmcp.h

#-----------------------------------------------------------

%package -n %{staticname}
Summary: Static development files for %{name}
Group: Development/X11
Requires: %{develname} = %{version}
Provides: libxdmcp-static-devel = %{version}-%{release}
Provides: libxdmcp6-static-devel = %{version}-%{release}
Obsoletes: %{mklibname xdmcp6}-static-devel

Conflicts: libxorg-x11-static-devel < 7.0

%description -n %{staticname}
Static development files for %{name}

%files -n %{staticname}
%defattr(-,root,root)
%{_libdir}/libXdmcp.a

#-----------------------------------------------------------

%prep
%setup -q -n libXdmcp-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -p /sbin/ldconfig
%endif

%files -n %{libxdmcp}
%defattr(-,root,root)
%{_libdir}/libXdmcp.so.6
%{_libdir}/libXdmcp.so.6.0.0


