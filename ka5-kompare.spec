%define		kdeappsver	18.12.1
%define		qtver		5.9.0
%define		kaname		kompare
Summary:	kompare
Name:		ka5-%{kaname}
Version:	18.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/applications/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	03b9c26dcd0f9135af29df770aa7e705
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkomparediff2-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= 5.35.0
BuildRequires:	kf5-kcodecs-devel >= 5.28.0
BuildRequires:	kf5-kconfig-devel >= 5.28.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.28.0
BuildRequires:	kf5-kdoctools-devel >= 5.28.0
BuildRequires:	kf5-kiconthemes-devel >= 5.28.0
BuildRequires:	kf5-kjobwidgets-devel >= 5.28.0
BuildRequires:	kf5-kparts-devel >= 5.53.0
BuildRequires:	kf5-ktexteditor-devel >= 5.28.0
BuildRequires:	kf5-kwidgetsaddons-devel >= 5.28.0
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kompare is a GUI front-end program that enables differences between
source files to be viewed and merged. It can be used to compare
differences on files or the contents of folders, and it supports a
variety of diff formats and provide many options to customize the
information level displayed.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kompare
%dir %{_includedir}/kompare
%{_includedir}/kompare/kompareinterface.h
%attr(755,root,root) %{_libdir}/libkomparedialogpages.so.5
%attr(755,root,root) %{_libdir}/libkompareinterface.so
%attr(755,root,root) %{_libdir}/libkompareinterface.so.5
%attr(755,root,root) %{_libdir}/qt5/plugins/komparenavtreepart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/komparepart.so
%{_desktopdir}/org.kde.kompare.desktop
%{_iconsdir}/hicolor/128x128/apps/kompare.png
%{_iconsdir}/hicolor/16x16/apps/kompare.png
%{_iconsdir}/hicolor/22x22/apps/kompare.png
%{_iconsdir}/hicolor/32x32/apps/kompare.png
%{_iconsdir}/hicolor/48x48/apps/kompare.png
%{_iconsdir}/hicolor/scalable/apps/kompare.svgz
%{_datadir}/kservices5/ServiceMenus/kompare.desktop
%{_datadir}/kservices5/komparenavtreepart.desktop
%{_datadir}/kservices5/komparepart.desktop
%{_datadir}/kservicetypes5/komparenavigationpart.desktop
%{_datadir}/kservicetypes5/kompareviewpart.desktop
%{_datadir}/kxmlgui5/kompare
%{_datadir}/kxmlgui5/komparepart
%{_datadir}/metainfo/org.kde.kompare.appdata.xml
