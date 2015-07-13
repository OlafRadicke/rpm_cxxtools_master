Name:           cxxtools
Version:        2.3rc1
Release:        1%{?dist}
Summary:        A collection of general-purpose C++ classes

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.tntnet.org/cxxtools.html
Source0:        http://www.tntnet.org/download/cxxtools-%{version}.tar.gz
Patch0:         cxxtools-2.3-arm.patch

Provides:       bundled(md5-polstra)

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
Development files for %{name}


# %prep
# %setup -q
# %patch0 -p0

# fix spurious executable perm
find -name "*.cpp" -exec chmod -x {} \;
find -name "*.h" -exec chmod -x {} \;

%build

rm -Rvf %{_builddir}/*
# mkdir -p %{_builddir}/
touch %{_builddir}/RPM_BUILD
ls -lah

echo %{_builddir}
ls -lah %{_builddir}/
cd %{_builddir}


wget https://github.com/maekitalo/cxxtools/archive/master.zip
ls -lah %{_builddir}/
cd %{_builddir}
unzip -u master.zip
ls -lah %{_builddir}/
cd %{_builddir}/cxxtools-master
/usr/bin/ls -lah
autoreconf -i


%configure --disable-static
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
mkdir -p  $RPM_BUILD_ROOT
cp -R %{_builddir}/cxxtools-master/*  %{buildroot}/

ls -lah

make install DESTDIR=$RPM_BUILD_ROOT

# Find and remove all la files
find $RPM_BUILD_ROOT -type f -name "*.la" -exec rm -f {} ';'

%check
    test/alltests

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libcxxtools*.so.*

%files devel
%{_bindir}/cxxtools-config
%{_libdir}/libcxxtools*.so
%{_libdir}/pkgconfig/%{name}-*.pc
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/cxxtools/

%changelog
* Sun Jul 12 2015 Martin Gansser <martinkg@fedoraproject.org> - 2.3rc1-1
- Update to 2.3rc1 (#1242222)
- removed cxxtools-2.2-arm.patch
- added cxxtools-2.3-arm.patch

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu May 22 2014 baude <baude@us.ibm.com> - 2.2.1-3
- Moving removal of .las from check to install section

* Mon Feb 17 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.2.1-2
- fix build on aarch64 where atomicity detection fails

* Mon Jan 20 2014 Martin Gansser <martinkg@fedoraproject.org> - 2.2.1-1
- new release

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 3 2013 Martin Gansser <martinkg@fedoraproject.org> - 2.2-1
- new release
- spec file cleanup

* Fri Sep 21 2012 Jon Ciesla <limburgher@gmail.com> - 2.1.1-5
- Fix FTBFS on ARM.

* Thu Jul 26 2012 Dan Horák <dan[at]danny.cz> - 2.1.1-4
- fix build on s390(x) where atomicity detection fails

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon May 28 2012 Martin Gansser <linux4martin@gmx.de> - 2.1.1-2
- added Provides: bundled(md5-polstra)

* Sat May 26 2012 Martin Gansser <linux4martin@gmx.de> - 2.1.1-1
- rebuild for new release
- fixed url
- removed empty files from doc
- fixed Requires for devel package
- added group tag for main package
- added unit test

* Sun Apr 29 2012 Martin Gansser <linux4martin@gmx.de> - 2.1-1
- new release
- removed license comment

* Mon Sep 19 2011 Sebastian Vahl <fedora@deadbabylon.de> - 2.0-2
- split into -devel subpkg

* Sun Sep 18 2011 Sebastian Vahl <fedora@deadbabylon.de> - 2.0-1
- initial release

