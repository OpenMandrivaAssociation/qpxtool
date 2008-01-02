%define name    qpxtool
%define version 0.6.1
%define beta    rc2
%define release %mkrel 0.%{beta}.1
%define major   0.6.2
%define libname %mklibname %{name}%{major}
%define develname %mklibname %{name} -d 
%define qtdir     %{_prefix}/lib/qt3

Name:       %{name}
Version:    %{version}
Release:    %{release}
Summary:    CD/DVD Drive Quality Checking
Group:      System/Configuration/Hardware
License:    GPL
URL:        http://qpxtool.sourceforge.net/
Source0:    http://prdownloads.sourceforge.net/qpxtool/qpxtool-%{version}%{beta}.tar.bz2
Patch0:     qpxtool-0.6.1rc2-fixbuild.patch
BuildRequires:  qt3-devel
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
%setup -q -n %{name}-%{version}%{beta}
%patch0 -p1

%build
export QTDIR="%{qtdir}"
export PATH="$QTDIR/bin:$PATH"

%make \
	PREFIX="%{_prefix}" \
	LIBDIR="%{_libdir}" \
	MANDIR="%{_mandir}" \
	CFLAGS="%{optflags} -fPIC -DQT_THREAD_SUPPORT" \
	CXXFLAGS="%{optflags} -fPIC -DQT_THREAD_SUPPORT"

%install
%__rm -rf %{buildroot}
%__make \
	PREFIX="%{_prefix}" \
	LIBDIR="%{_libdir}" \
	MANDIR="%{_mandir}" \
	DESTDIR="%{buildroot}" \
	install

%__install -D -m0644 qpxtool-gui/img/q.xpm "%{buildroot}%{_datadir}/pixmaps/qpxtool.xpm"

%clean
%__rm -rf %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/deadreader
%{_bindir}/pioquiet
%{_bindir}/pxcontrol
%{_bindir}/pxfw
%{_bindir}/qpxtool
%{_mandir}/man8/pxcontrol.8*
%{_mandir}/man8/pxfw.8*
%{_datadir}/pixmaps/qpxtool.xpm

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%{_libdir}/*.so
%{_includedir}/*

