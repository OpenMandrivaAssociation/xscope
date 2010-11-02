Name:    xscope
Version: 1.3
Release: %mkrel 1

Summary:   X Window Protocol Viewer
Group:     Development/X11
License:   MIT
BuildRoot: %{_tmppath}/%{name}-root

Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2

BuildRequires: libx11-devel
BuildRequires: x11-xtrans-devel

%description
Xscope sits in-between an X11 client and an X11 server and prints the contents
of each request, reply, error, or event that is communicated between them.
Xscope can decode the core X11 protocol and several extensions, including
BIG-REQUESTS, LBX, MIT-SHM, NCD-WinCenterPro, RANDR, and RENDER. This
information can be useful in debugging and performance tuning of X11 servers
and clients.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xscope
%{_mandir}/man1/xscope.1*
