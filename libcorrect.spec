%global optflags        %{optflags} -flto=auto
%global build_ldflags   %{build_ldflags} -flto

%global gitcommit_full f5a28c74fba7a99736fe49d3a5243eca29517ae9
%global gitcommit %(c=%{gitcommit_full}; echo ${c:0:7})
%global date 20181010

Name:           libcorrect
Version:        0
Release:        1.%{date}git%{gitcommit}%{?dist}
Summary:        C library for Convolutional codes and Reed-Solomon
License:        BSD
URL:            https://github.com/quiet/libcorrect
Source0:        %{url}/tarball/%{gitcommit_full}

BuildRequires:  cmake
BuildRequires:  gcc-c++

%description
libcorrect is a library for Forward Error Correction. By using libcorrect,
extra redundancy can be encoded into a packet of data and then be sent
across a lossy channel. When the packet is received, it can be decoded to
recover the original, pre-encoded data.

%package devel
Summary:        Development files for libcorrect
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
libcorrect is a library for Forward Error Correction. By using libcorrect,
extra redundancy can be encoded into a packet of data and then be sent
across a lossy channel. When the packet is received, it can be decoded to
recover the original, pre-encoded data.

This subpackage contains libraries and header files for developing
applications that want to make use of libcorrect.

%prep
%autosetup -p1 -n quiet-%{name}-%{gitcommit}
echo "set_property(TARGET correct PROPERTY SOVERSION 0.0.0)" >> CMakeLists.txt
sed -i "s|DESTINATION lib|DESTINATION %{_lib}|" CMakeLists.txt
sed -i '/CMAKE_C_FLAGS/d' CMakeLists.txt
sed -i 's|}" HAVE_SSE)|}" HAVE_SSE_dd)|' CMakeLists.txt


%build
%cmake \
    -DCMAKE_AR=/usr/bin/gcc-ar \
    -DCMAKE_RANLIB=/usr/bin/gcc-ranlib \
    -DCMAKE_NM=/usr/bin/gcc-nm \
    .
%make_build

%install
%make_install

%files
%license LICENSE
%doc README.md
%{_libdir}/libcorrect.so.*

%files devel
%{_includedir}/correct*.h
%{_libdir}/libcorrect.so

%changelog
* Thu Oct 24 2019 Vasiliy N. Glazov <vascom2@gmail.com> - 0-1.20181010gitf5a28c7
- Initial release for Fedora
