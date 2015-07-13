Name: cxxtools_master
Summary: Install the cxxtools lib with the code of the master branch.
Version: 1
Group: develop
License: LGPL
Release: 1
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}
Source:%{name}-%{version}-%{release}.tar.gz
BuildArch: x86_64

BuildRequires: automake, autoconf, gcc-c++, zlib-devel
# Requires:


%description
Install the cxxtools lib with the code of the master branch. cxxtools is a toolbox with reusable c++-components.

%prep

# %setup  -n %{name}-%{version}-%{release}


%build

%install
if [ $1 -eq 1 ]; then
    echo "First install"
else
    echo "Upgrade"
fi

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
./configure --help
/bin/bash ./configure
make
ls -lah

mkdir -p %{buildroot}/usr/local/lib
make install prefix=%{_prefix} DESTDIR=$RPM_BUILD_ROOT
cd ..
rm -Rvf ./cxxtools-master


mkdir -p %{buildroot}/etc/ld.so.conf.d/
echo "/usr/local/lib" >  %{buildroot}/etc/ld.so.conf.d/cxxtools.conf

%post

ldconfig

%clean
# rm -Rvf /tmp/master.zip /tmp/cxxtools-master
#rm -fr $RPM_BUILD_ROOT

%postun

# rm /etc/ld.so.conf.d/cxxtools.conf
ldconfig


%files
# %dir  /usr/share/doc/olaf-system-post-init/
# /usr/share/doc/olaf-system-post-init/releasenote.md
/usr/lib/libcxxtools-xmlrpc.so.9.0.0
/usr/lib/libcxxtools-bin.so.9.0.0
/usr/lib/libcxxtools.so.9.0.0
/usr/lib/libcxxtools-unit.so.9.0.0
/usr/lib/libcxxtools-json.so.9.0.0
/usr/lib/libcxxtools-http.so.9.0.0



%changelog
* Sun Jul 12 2015 briefkasten@olaf-radicke.de - 1
- Init-Version.

