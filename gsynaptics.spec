Summary:	GNOME tool for Synaptics touchpad driver
Summary(pl.UTF-8):	Narzędzie GNOME dla sterownika Synaptics
Name:		gsynaptics
Version:	0.9.14
Release:	3
License:	GPL v2
Group:		X11/Applications
Source0:	http://osdn.dl.sourceforge.jp/gsynaptics/29684/%{name}-%{version}.tar.gz
# Source0-md5:	5cf556b26085444288f087587a92484c
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-pixmap.patch
Patch2:		%{name}-dot-fixes.patch
Patch3:		%{name}-do-not-set-zero.patch
URL:		http://gsynaptics.sourceforge.jp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel >= 0.15
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	xorg-driver-input-synaptics
ExcludeArch:	sparc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GSynaptics is a setting tool for Synaptics touchpad driver.

%description -l pl.UTF-8
GSynaptics jest narzędziem służącym do zmieniania ustwień sterownika
touchpada Synaptics.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__intltoolize}
#%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_datadir}/gnome/autostart/gsynaptics-init.desktop
%{_mandir}/man1/gsynaptics-init.1*
%{_mandir}/man1/gsynaptics.1*
%{_datadir}/gnome/help/%{name}
