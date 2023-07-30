%global commit0      1cb513cb1009855e01a69f9881d9cde555219a6c
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name: libks
Version: 2.0.2
Release: 0
Summary: Foundational support for signalwire C products 
Group: System/Libraries
License: MIT
Url: https://github.com/signalwire/libks
Source0: https://github.com/sergey-safarov/libks/archive/%{commit0}.tar.gz#/%{name}-%{version}-%{shortcommit0}.tar.gz
BuildRequires: cmake ninja-build gcc-c++ ninja-build libatomic
BuildRequires: pkgconfig(uuid) pkgconfig(openssl)

%description
Foundational support for signalwire C products

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version

%description devel
Development files for %name

%prep
%autosetup -p1 -n %{name}-%{commit0}

%build
%{cmake} -D KS_PLAT_LIN=true \
	-D CENTOS_FOUND=true \
	-G Ninja \
	-D CMAKE_BUILD_TYPE=Release .
%{cmake_build} -j 1

%install
%{cmake_install}
find %{buildroot} -name '*.a' -delete


%files -n %name
%_libdir/libks2.so.*

%files devel
%doc %_docdir/libks2/copyright
%_includedir/libks2
%_libdir/pkgconfig/libks2.pc
%_libdir/libks2.so

%changelog
* Tue Feb 28 2023 Anton Farygin <rider@altlinux.ru> 1.8.2-alt1
- 1.8.0 -> 1.8.2

* Sat Feb 12 2022 Anton Farygin <rider@altlinux.ru> 1.8.0-alt1
- 1.7.0 -> 1.8.0

* Thu Nov 25 2021 Anton Farygin <rider@altlinux.ru> 1.7.0-alt1
- first build for ALT
