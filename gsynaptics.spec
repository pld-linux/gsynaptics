Summary:	GNOME tool for Synaptics touchpad driver
Summary(pl):	Narz�dzie GNOME dla sterownika Synaptics
Name:		gsynaptics
Version:	0.9.0
Release:	1
Epoch:		0
License:	GPL v.2
Group:		Applications
Source0:	http://osdn.dl.sourceforge.jp/gsynaptics/15189/%{name}-%{version}.tar.gz
# Source0-md5:	b4fd084433662414e81408b88b5fb971
Patch0:		%{name}-desktop.patch
URL:		http://gsynaptics.sourceforge.jp/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	intltool
BuildRequires:	libglade2-devel
BuildRequires:	libgnomeui-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
Requires:	X11-synaptics
ExcludeArch:	sparc sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GSynaptics is a setting tool for Synaptics touchpad driver.

%description -l pl
GSynaptics jest narz�dziem s�u��cym do zmieniania ustwie� sterownika
touchpada Synaptics.

%prep
%setup -q
%patch0 -p1

%build
%{__glib_gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
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
