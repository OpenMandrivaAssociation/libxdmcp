%define major 6
%define libxdmcp %mklibname xdmcp %{major}
%define develname %mklibname xdmcp -d

Name:		libxdmcp
Summary:	X Display Manager Control Protocol library
Version:	1.1.1
Release:	2
Group:		Development/X11
License:	MIT
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXdmcp-%{version}.tar.bz2

BuildRequires:	x11-proto-devel >= 1.0.0
BuildRequires:	x11-util-macros >= 1.0.1

%description
X Display Manager Control Protocol library

%package -n %{libxdmcp}
Summary:	Development files for %{name}
Group:		Development/X11
Conflicts:	libxorg-x11 < 7.0
Provides:	%{name} = %{version}

%description -n %{libxdmcp}
X Display Manager Control Protocol library

%package -n %{develname}
Summary:	Development files for %{name}
Group:		Development/X11
Requires:	%{libxdmcp} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{_lib}xdmcp6-devel < 1.1.1
Obsoletes:	%{_lib}xdmcp-static-devel < 1.1.1
Conflicts:	libxorg-x11-devel < 7.0

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


%changelog
* Sat Mar 10 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.1-1
+ Revision: 783941
- version update 1.1.1

* Thu Mar 08 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.1.0-5
+ Revision: 783351
- Remove pre scriptlet to correct rpm upgrade moving from /usr/X11R6.

* Tue Dec 27 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.0-4
+ Revision: 745502
- rebuild
- disabled static build
- removed .la files
- employed major macro
- cleaned up spec

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-3
+ Revision: 662422
- mass rebuild

* Thu Feb 17 2011 Matthew Dawkins <mattydaw@mandriva.org> 1.1.0-2
+ Revision: 638236
- dropped major number from devel and static devel pkgs
- added proper provides and obsoletes for older naming scheme

* Sat Oct 30 2010 Thierry Vignaud <tv@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 590581
- adjust filelist
- new release

* Tue Mar 16 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.3-2mdv2010.1
+ Revision: 520964
- rebuilt for 2010.1

* Fri Sep 25 2009 Thierry Vignaud <tv@mandriva.org> 1.0.3-1mdv2010.0
+ Revision: 448645
- new release
- drop visibility patch

* Wed Sep 02 2009 Christophe Fergeau <cfergeau@mandriva.com> 1.0.2-7mdv2010.0
+ Revision: 425884
- rebuild

* Wed Aug 06 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-6mdv2009.0
+ Revision: 264972
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Jun 02 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-5mdv2009.0
+ Revision: 214366
- Rebuild to match changes in xtrans.
- Revert build requires.

* Mon Jan 14 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-4mdv2008.1
+ Revision: 151455
- Update BuildRequires and rebuild.

* Sun Jan 13 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-3mdv2008.1
+ Revision: 150851
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Paulo Andrade <pcpa@mandriva.com.br>
    - This is a "noop" patch. But it can be considered a list of the functions,
      code from X Server uses from libXdmcp, at a later stage, this library can be
      changed to make available only the public symbols.

