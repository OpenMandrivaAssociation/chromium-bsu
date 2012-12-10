Name:		chromium-bsu
Version:	0.9.15
Release:	3
Summary:	Fast paced, arcade-style, top-scrolling space shooter
Group:		Games/Arcade
License:	Artistic clarified
URL:		http://chromium-bsu.sourceforge.net/
Source0:	http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Patch0:		chromium-bsu-0.9.15-sformat.patch
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(quesoglc)
BuildRequires:	pkgconfig(openal)
BuildRequires:	pkgconfig(freealut)
BuildRequires:	libglpng-devel
BuildRequires:	imagemagick
Obsoletes:	chromium < 0.9.15-3

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
%makeinstall_std

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48,64x64}/apps
install -m0644 misc/%{name}.png %{buildroot}%{_iconsdir}/hicolor/64x64/apps/%{name}.png
convert -scale 48x48 misc/%{name}.png %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert -scale 32x32 misc/%{name}.png %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16x16 misc/%{name}.png %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS COPYING NEWS README ChangeLog
%{_gamesbindir}/%{name}
%{_gamesdatadir}/%{name}
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/hicolor/*/apps/%{name}.png
%{_mandir}/man6/%{name}.6.*

%changelog
* Wed Dec 14 2011 Andrey Bondrov <abondrov@mandriva.org> 0.9.15-2mdv2011.0
+ Revision: 740877
- Use ImageMagick for icons, obsolete chromium

* Tue Dec 13 2011 Andrey Bondrov <abondrov@mandriva.org> 0.9.15-1
+ Revision: 740681
- imported package chromium-bsu

