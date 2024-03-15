#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.5
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kompare
Summary:	kompare
Name:		ka5-%{kaname}
Version:	23.08.5
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	28bdbaafb023fa904d129f964b65bfaf
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkomparediff2-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kcodecs-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kjobwidgets-devel >= %{kframever}
BuildRequires:	kf5-kparts-devel >= %{kframever}
BuildRequires:	kf5-ktexteditor-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
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

%description -l pl.UTF-8
Kompare jest programem GUI, który pokazuje różnice między plikami
kodu źródłowego, które mogą być złączone. Może być użyty do
porównania plików, lub zawartości folderów. Wspiera różne
formaty diffa i dostarcza wielu opcji do zmieniania zakresu
wyświetlanej informacji.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


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
%{_libdir}/libkompareinterface.so
%attr(755,root,root) %{_libdir}/libkompareinterface.so.5
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/parts/komparenavtreepart.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kf5/parts/komparepart.so
%{_desktopdir}/org.kde.kompare.desktop
%{_iconsdir}/hicolor/128x128/apps/kompare.png
%{_iconsdir}/hicolor/16x16/apps/kompare.png
%{_iconsdir}/hicolor/22x22/apps/kompare.png
%{_iconsdir}/hicolor/32x32/apps/kompare.png
%{_iconsdir}/hicolor/48x48/apps/kompare.png
%{_iconsdir}/hicolor/scalable/apps/kompare.svgz
%{_datadir}/metainfo/org.kde.kompare.appdata.xml
%{_datadir}/qlogging-categories5/kompare.categories
%{_datadir}/kio/servicemenus/kompare.desktop
