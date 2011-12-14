Name:		chromium-bsu
Version:	0.9.15
Release:	%mkrel 2
Summary:	Fast paced, arcade-style, top-scrolling space shooter
Group:		Games/Arcade
License:	Artistic clarified
URL:		http://chromium-bsu.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		chromium-bsu-0.9.15-sformat.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:	mesaglu-devel
BuildRequires:	SDL-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	libvorbis-devel
BuildRequires:	SDL_image-devel
BuildRequires:	png-devel
BuildRequires:	libglpng-devel
BuildRequires:	quesoglc-devel
BuildRequires:	openal-devel
BuildRequires:	freealut-devel
BuildRequires:	imagemagick
Obsoletes:	chromium <= %{version}

%description
You are captain of the cargo ship Chromium B.S.U., responsible for delivering
supplies to our troops on the front line. Your ship has a small fleet of
robotic fighters which you control from the relative safety of the Chromium
vessel.

This is an OpenGL-based shoot 'em up game with fine graphics.

%prep
%setup -q
%patch0 -p1 -b .fmt

%build
%configure2_5x --bindir=%{_gamesbindir} --datadir=%{_gamesdatadir}
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

%__mkdir_p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48,64x64}/apps
%__install -m0644 misc/%{name}.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
convert -scale 48x48 misc/%{name}.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert -scale 32x32 misc/%{name}.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16x16 misc/%{name}.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

%find_lang %{name}

%clean
%__rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc AUTHORS COPYING NEWS README ChangeLog
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6.*

