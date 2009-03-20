%define	_module	i2400m
Summary:	Microcode image for Intel Wireless WiFi Link 5000AGN Adapter
Summary(pl.UTF-8):	Obraz mikrokodu dla układów bezprzewodowych Intel Wireless WiFi Link 5000AGN
Name:		wimax-%{_module}-fw
Version:	1.4.0
Release:	1
License:	distributable
Group:		Base/Kernel
Source0:	http://www.linuxwimax.org/Download?action=AttachFile&do=get&target=%{_module}-fw-%{version}.tar.bz2
# Source0-md5:	d2aa2da73926fc23d5ff748f64bd520d
URL:		http://www.linuxwimax.org/
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The file provided in this package must be present on your system in
order for the Intel WiMAX/WiFi devices to operate on your system.

%prep
%setup -q -n %{_module}-fw-%{version}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/lib/firmware

install i2400m-fw-usb-1.4.sbcf $RPM_BUILD_ROOT/lib/firmware
install LICENSE $RPM_BUILD_ROOT/lib/firmware/%{name}-LICENSE

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
/lib/firmware/%{name}-LICENSE
/lib/firmware/*.sbcf
