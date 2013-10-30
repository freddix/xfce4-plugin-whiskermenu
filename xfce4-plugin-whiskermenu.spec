%define		org_name	xfce4-whiskermenu-plugin

Summary:	An alternate menu for the Xfce desktop environment
Name:		xfce4-plugin-whiskermenu
Version:	1.2.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://gottcode.org/xfce4-whiskermenu-plugin/%{org_name}-%{version}-src.tar.bz2
# Source0-md5:	bf57b4c8cc629c93ee435e7ac5d46b45
URL:		http://gottcode.org/xfce4-whiskermenu-plugin/
BuildRequires:	cmake
BuildRequires:	exo-devel
BuildRequires:	garcon-devel
BuildRequires:	libstdc++-devel
BuildRequires:	xfce4-panel-devel
Requires(post,postun):	/usr/bin/gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	exo
Requires:	garcon
Requires:	xfce4-panel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
iWhisker Menu is an alternate application launcher for Xfce. When you
open it you are shown a list of applications you have marked as
favorites. You can browse through all of your installed applications
by clicking on the category buttons on the side. Top level categories
make browsing fast, and simple to switch between. Additionally,
Whisker Menu keeps a list of the last ten applications that you’ve
launched from it.

%prep
%setup -qn %{org_name}-%{version}

%build
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{org_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{org_name}.lang
%defattr(644,root,root,755)
%doc COPYING CREDITS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/xfce4-popup-whiskermenu
%attr(755,root,root) %{_libdir}/xfce4/panel/plugins/libwhiskermenu.so
%{_datadir}/xfce4/panel/plugins/whiskermenu.desktop
%{_iconsdir}/hicolor/*/apps/xfce4-whiskermenu.*
%{_mandir}/man1/xfce4-popup-whiskermenu.1*

