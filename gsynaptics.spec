Summary:	GNOME tool for Synaptics touchpad driver
Summary(pl.UTF-8):	Narzędzie GNOME dla sterownika Synaptics
Name:		gsynaptics
Version:	0.9.12
Release:	1
Epoch:		0
License:	GPL v2
Group:		Applications
Source0:	http://osdn.dl.sourceforge.jp/gsynaptics/25147/%{name}-%{version}.tar.gz
# Source0-md5:	e07afb3fbf61c55433cbbcc72602a3fb
Patch0:		%{name}-desktop.patch
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

%build
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
#%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --all-name
%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%{_datadir}/gnome/autostart/gsynaptics-init.desktop
%{_mandir}/man1/gsynaptics-init.1*
%{_mandir}/man1/gsynaptics.1*
