%global tl_name lfb
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	A Greek font with normal and bold variants
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/lfb
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lfb.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/lfb.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a Greek font written in Metafont, with inspiration from the
Bodoni typefaces in old books. It is stylistically a little more exotic
than the standard textbook Greek fonts, particularly in glyphs like the
lowercase rho and kappa. It aims for a rather calligraphic feel, but
seems to blend well with Computer Modern. There is a ligature scheme
which automatically inserts the breathings required for ancient texts,
making the input text more readable than in some schemes.

