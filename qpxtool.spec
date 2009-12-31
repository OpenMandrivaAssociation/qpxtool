%define name    qpxtool
%define version 0.7.0
%define release 1
%define major   0.6.2
%define libname %mklibname %{name}%{major}
%define develname %mklibname %{name} -d 

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    CD/DVD Drive Quality Checking
Group:      System/Configuration/Hardware
License:    GPL
URL:        http://qpxtool.sourceforge.net/
Source0:    http://sourceforge.net/projects/qpxtool/files/qpxtool/0.7.x/0.7.0/qpxtool-%{version}.tar.bz2
BuildRequires:  qt4-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
QPxTool is the linux way to get full control over your CD/DVD drives.

It is the Open Source Solution which intends to give you access to all
available Quality Checks (Q-Checks) on written and blank media, that are
available for your drive. This will help you to find the right media and the
optimized writing speed for your hardware, which will increase the chance for
a long data lifetime.

Includes tool to update your firmware (firmware not included),

%package -n %{libname} 
Group: Development/KDE and Qt
Summary: Shared libraries for qpxtool

%description -n %{libname}
Shared libraries for qpxtool.

%package -n %{develname} 
Group: Development/KDE and Qt
Summary: Development files for qpxtool
Requires: %{libname} = %version-%release

%description -n %{develname}
Development files for qpxtool.

%prep
%setup -q

%build
./configure --prefix=/usr 

pushd gui
mv -vf Makefile Makefile.orig || die "Backup Makefile for install"
qmake qpxtool.pro
popd

%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

install -d -m 755 %{buildroot}%{_datadir}/applications
install -m 644 gui/qpxtool.desktop %{buildroot}%{_datadir}/applications

%clean
%__rm -rf %{buildroot}

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/qscan
%{_bindir}/qscand
%{_bindir}/f1tattoo
%{_bindir}/cdvdcontrol
%{_bindir}/readdvd
%{_sbindir}/pxfw
%{_mandir}/man8/pxfw.8*
%{_mandir}/man1/cdvdcontrol.1*
%{_mandir}/man1/f1tattoo.1*
%{_mandir}/man1/qscan.1*
%{_mandir}/man1/readdvd.1*
%{_datadir}/applications/qpxtool.desktop
%{_libdir}/qpxtool

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/*

