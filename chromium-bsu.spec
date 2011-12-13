Name:		chromium-bsu
Version:	0.9.15
Release:	%mkrel 1
Summary:	Fast paced, arcade-style, top-scrolling space shooter
Group:		Games/Arcade
License:	Artistic clarified
URL:		http://chromium-bsu.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		chromium-bsu-0.9.15-sformat.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	libvorbis-devel
BuildRequires:	SDL_image-devel
BuildRequires:	png-devel
BuildRequires:	libglpng-devel
BuildRequires:	quesoglc-devel
BuildRequires:	openal-soft-devel
BuildRequires:	freealut-devel

%description
You are captain of the cargo ship Chromium B.S.U., responsible for delivering
supplies to our troops on the front line. Your ship has a small fleet of
robotic fighters which you control from the relative safety of the Chromium
vessel. This is an OpenGL-based shoot 'em up game with fine graphics.

%prep
%setup -q
%patch0 -p1 -b .fmt

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README ChangeLog
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man6/%{name}.6.*

