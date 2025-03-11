Name:		xscope
Version:	1.4.5
Release:	1

Summary:	X Window Protocol Viewer
Group:		Development/X11
License:	MIT

URL:		https://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xtrans)
BuildRequires:	pkgconfig(xorg-macros) >= 1.8

%description
Xscope sits in-between an X11 client and an X11 server and prints the contents
of each request, reply, error, or event that is communicated between them.
Xscope can decode the core X11 protocol and several extensions, including
BIG-REQUESTS, LBX, MIT-SHM, NCD-WinCenterPro, RANDR, and RENDER. This
information can be useful in debugging and performance tuning of X11 servers
and clients.

%prep
%autosetup -p1
%configure

%build
%make_build

%install
%make_install

%files
%{_bindir}/xscope
%{_mandir}/man1/xscope.1*
