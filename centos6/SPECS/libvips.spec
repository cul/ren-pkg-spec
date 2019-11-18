Summary:            A fast image processing library with low memory needs
Name:               vips
Version:            8.6.2
Release:            1%{?dist}
License:            LGPLv2+
Source0:            https://github.com/libvips/libvips/releases/download/v8.6.2/%{name}-%{version}.tar.gz
URL:                https://github.com/libvips/libvips
BuildRequires:      chrpath, gtk-doc, libxml2-devel, libjpeg-turbo-devel, libpng-devel
BuildRequires:      libtiff-devel, libexif-devel, libgsf-devel, lcms-devel
BuildRequires:      ImageMagick-devel, libwebp-devel
BuildRequires:      expat-devel, poppler-glib-devel, giflib-devel, cfitsio-devel, orc-devel
Requires:           gtk-doc, libxml2, libjpeg-turbo, libpng, libtiff, libexif
Requires:           libgsf, lcms, ImageMagick, libwebp
Requires:           expat, poppler-glib, giflib, cfitsio, orc

%description
libvips is a 2D image processing library. Compared to similar libraries,
libvips runs quickly and uses little memory. libvips is licensed under
the LGPL 2.1+.

It has around 300 operations covering arithmetic, histograms, convolutions,
morphological operations, frequency filtering, colour, resampling, statistics
and others. It supports a large range of numeric formats, from 8-bit int to
128-bit complex. It supports a good range of image formats, including JPEG,
TIFF, PNG, WebP, FITS, Matlab, OpenEXR, PDF, SVG, HDR, PPM, CSV, GIF, Analyze,
DeepZoom, and OpenSlide. It can also load images via ImageMagick or GraphicsMagick.

It has APIs for C and C++ and a command-line interface. Bindings are available for 
Python, Ruby, PHP, Go, Lua, JavaScript and others. There is full documentation. There
are several GUIs as well, see the VIPS website.

%prep
%autosetup -n %{name}-%{version}

%build
%configure
%make_build
%install
%make_install
for f in $(find %{buildroot} -exec file {} \; | grep -i elf | cut -d: -f1); do chrpath --delete $f; done

%files
%doc README.md TODO ChangeLog COPYING
%{_bindir}/*
%{_libdir}/*
%{_includedir}/*
%{_datadir}/**/*
