Name:           gstreamer1-plugins-ugly
Version:        1.4.5
Release:        1%{?dist}
Summary:        GStreamer v1.x Ugly Plug-ins

License:        LGPLv2.1
URL:            https://gstreamer.freedesktop.org/modules/gst-plugins-ugly.html
Source0:        https://gstreamer.freedesktop.org/src/gst-plugins-ugly/gst-plugins-ugly-%{version}.tar.xz

BuildRequires:  gstreamer1-devel >= 1.0.0
BuildRequires:  gstreamer1-plugins-base-devel >= 1.0.0
BuildRequires:  gettext-devel
BuildRequires:  gtk-doc
BuildRequires:  orc-devel

BuildRequires:  liba52-devel
BuildRequires:  opencore-amr-devel
BuildRequires:  libcdio-devel
BuildRequires:  libdvdread-devel
BuildRequires:  libmp3lame-devel
BuildRequires:  libmad-devel
BuildRequires:  libmpeg2-devel
BuildRequires:  libtwolame-devel
BuildRequires:  libx264-devel

%description
GStreamer Ugly Plug-ins is a set of plug-ins that have good quality and correct
functionality, but distributing them might pose problems. The license on either
the plug-ins or the supporting libraries might not be how we'd like. The code
might be widely known to present patent problems.


# a52dec {{{
%package a52dec
Summary:        Decodes ATSC A/52 encoded audio streams
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description a52dec
%{summary}.
# }}}

# opencore-amr {{{
%package opencore-amr
Summary:        Adaptive Multi-Rate decoders and encoders
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description opencore-amr
%{summary}.
# }}}

# cdio {{{
%package cdio
Summary:        Read audio from audio CDs
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description cdio
%{summary}.
# }}}

# dvdreadsrc {{{
%package dvdreadsrc
Summary:        Access a DVD title/chapter/angle using libdvdread
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description dvdreadsrc
%{summary}.
# }}}

# lame {{{
%package lame
Summary:        Encode MP3s with LAME
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description lame
%{summary}.
# }}}

# mad {{{
%package mad
Summary:        mp3 decoding based on the mad library
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description mad
%{summary}.
# }}}

# mpeg2dec {{{
%package mpeg2dec
Summary:        Uses libmpeg2 to decode MPEG video streams
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description mpeg2dec
%{summary}.
# }}}

# twolame {{{
%package twolame
Summary:        Encode MP2s with TwoLAME
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description twolame
%{summary}.
# }}}

# x264 {{{
%package x264
Summary:        libx264-based H264 plugins
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description x264
%{summary}.
# }}}


%prep
%setup -q -n gst-plugins-ugly-%{version}


%build
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'
%find_lang gst-plugins-ugly-1.0


%files -f gst-plugins-ugly-1.0.lang
%license COPYING
%doc AUTHORS ChangeLog README
%doc %{_datadir}/gtk-doc/
%dir %{_datadir}/gstreamer-1.0/presets/
%{_libdir}/gstreamer-1.0/libgstasf.so
%{_libdir}/gstreamer-1.0/libgstdvdlpcmdec.so
%{_libdir}/gstreamer-1.0/libgstdvdsub.so
%{_libdir}/gstreamer-1.0/libgstrmdemux.so
%{_libdir}/gstreamer-1.0/libgstxingmux.so

%files a52dec
%{_libdir}/gstreamer-1.0/libgsta52dec.so

%files opencore-amr
%{_libdir}/gstreamer-1.0/libgstamrnb.so
%{_libdir}/gstreamer-1.0/libgstamrwbdec.so
%{_datadir}/gstreamer-1.0/presets/GstAmrnbEnc.prs

%files cdio
%{_libdir}/gstreamer-1.0/libgstcdio.so

%files dvdreadsrc
%{_libdir}/gstreamer-1.0/libgstdvdread.so

%files lame
%{_libdir}/gstreamer-1.0/libgstlame.so

%files mad
%{_libdir}/gstreamer-1.0/libgstmad.so

%files mpeg2dec
%{_libdir}/gstreamer-1.0/libgstmpeg2dec.so

%files twolame
%{_libdir}/gstreamer-1.0/libgsttwolame.so

%files x264
%{_libdir}/gstreamer-1.0/libgstx264.so
%{_datadir}/gstreamer-1.0/presets/GstX264Enc.prs


%changelog
* Mon May 16 2016 Jajauma's Packages <jajauma@yandex.ru> - 1.4.5-1
- Public release

# vim: foldmethod=marker
