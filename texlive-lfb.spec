# revision 15878
# category Package
# catalog-ctan /fonts/greek/lfb
# catalog-date 2006-10-18 08:58:01 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-lfb
Version:	1.0
Release:	6
Summary:	A Greek font with normal and bold variants
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/greek/lfb
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lfb.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/lfb.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a Greek font written in MetaFont, with inspiration from
the Bodoni typefaces in old books. It is stylistically a little
more exotic than the standard textbook Greek fonts,
particularly in glyphs like the lowercase rho and kappa. It
aims for a rather calligraphic feel, but seems to blend well
with Computer Modern. There is a ligature scheme which
automatically inserts the breathings required for ancient
texts, making the input text more readable than in some
schemes.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/source/public/lfb/accents.mf
%{_texmfdistdir}/fonts/source/public/lfb/alpha.mf
%{_texmfdistdir}/fonts/source/public/lfb/beta.mf
%{_texmfdistdir}/fonts/source/public/lfb/capitals.mf
%{_texmfdistdir}/fonts/source/public/lfb/charmap.mf
%{_texmfdistdir}/fonts/source/public/lfb/delta.mf
%{_texmfdistdir}/fonts/source/public/lfb/epsilon.mf
%{_texmfdistdir}/fonts/source/public/lfb/eta.mf
%{_texmfdistdir}/fonts/source/public/lfb/gamma.mf
%{_texmfdistdir}/fonts/source/public/lfb/iota.mf
%{_texmfdistdir}/fonts/source/public/lfb/kappa.mf
%{_texmfdistdir}/fonts/source/public/lfb/khi.mf
%{_texmfdistdir}/fonts/source/public/lfb/lambda.mf
%{_texmfdistdir}/fonts/source/public/lfb/lfb.mf
%{_texmfdistdir}/fonts/source/public/lfb/lfb10.mf
%{_texmfdistdir}/fonts/source/public/lfb/lfb11.mf
%{_texmfdistdir}/fonts/source/public/lfb/lfb12.mf
%{_texmfdistdir}/fonts/source/public/lfb/lfb5.mf
%{_texmfdistdir}/fonts/source/public/lfb/lfb6.mf
%{_texmfdistdir}/fonts/source/public/lfb/lfb7.mf
%{_texmfdistdir}/fonts/source/public/lfb/lfb8.mf
%{_texmfdistdir}/fonts/source/public/lfb/lfb9.mf
%{_texmfdistdir}/fonts/source/public/lfb/lfbb10.mf
%{_texmfdistdir}/fonts/source/public/lfb/lfbb11.mf
%{_texmfdistdir}/fonts/source/public/lfb/lfbb12.mf
%{_texmfdistdir}/fonts/source/public/lfb/lfbb5.mf
%{_texmfdistdir}/fonts/source/public/lfb/lfbb6.mf
%{_texmfdistdir}/fonts/source/public/lfb/lfbb7.mf
%{_texmfdistdir}/fonts/source/public/lfb/lfbb8.mf
%{_texmfdistdir}/fonts/source/public/lfb/lfbb9.mf
%{_texmfdistdir}/fonts/source/public/lfb/ligature.mf
%{_texmfdistdir}/fonts/source/public/lfb/mu.mf
%{_texmfdistdir}/fonts/source/public/lfb/nu.mf
%{_texmfdistdir}/fonts/source/public/lfb/omega.mf
%{_texmfdistdir}/fonts/source/public/lfb/omikron.mf
%{_texmfdistdir}/fonts/source/public/lfb/others.mf
%{_texmfdistdir}/fonts/source/public/lfb/phi.mf
%{_texmfdistdir}/fonts/source/public/lfb/pi.mf
%{_texmfdistdir}/fonts/source/public/lfb/psi.mf
%{_texmfdistdir}/fonts/source/public/lfb/rho.mf
%{_texmfdistdir}/fonts/source/public/lfb/serifs.mf
%{_texmfdistdir}/fonts/source/public/lfb/sigma.mf
%{_texmfdistdir}/fonts/source/public/lfb/sigmafin.mf
%{_texmfdistdir}/fonts/source/public/lfb/tau.mf
%{_texmfdistdir}/fonts/source/public/lfb/theta.mf
%{_texmfdistdir}/fonts/source/public/lfb/upsilon.mf
%{_texmfdistdir}/fonts/source/public/lfb/xi.mf
%{_texmfdistdir}/fonts/source/public/lfb/zeta.mf
%{_texmfdistdir}/fonts/tfm/public/lfb/lfb10.tfm
%{_texmfdistdir}/fonts/tfm/public/lfb/lfb11.tfm
%{_texmfdistdir}/fonts/tfm/public/lfb/lfb12.tfm
%{_texmfdistdir}/fonts/tfm/public/lfb/lfb5.tfm
%{_texmfdistdir}/fonts/tfm/public/lfb/lfb6.tfm
%{_texmfdistdir}/fonts/tfm/public/lfb/lfb7.tfm
%{_texmfdistdir}/fonts/tfm/public/lfb/lfb8.tfm
%{_texmfdistdir}/fonts/tfm/public/lfb/lfb9.tfm
%{_texmfdistdir}/fonts/tfm/public/lfb/lfbb10.tfm
%{_texmfdistdir}/fonts/tfm/public/lfb/lfbb11.tfm
%{_texmfdistdir}/fonts/tfm/public/lfb/lfbb12.tfm
%{_texmfdistdir}/fonts/tfm/public/lfb/lfbb5.tfm
%{_texmfdistdir}/fonts/tfm/public/lfb/lfbb6.tfm
%{_texmfdistdir}/fonts/tfm/public/lfb/lfbb7.tfm
%{_texmfdistdir}/fonts/tfm/public/lfb/lfbb8.tfm
%{_texmfdistdir}/fonts/tfm/public/lfb/lfbb9.tfm
%doc %{_texmfdistdir}/doc/fonts/lfb/README
%doc %{_texmfdistdir}/doc/fonts/lfb/example.pdf
%doc %{_texmfdistdir}/doc/fonts/lfb/example.tex
%doc %{_texmfdistdir}/doc/fonts/lfb/lfb.make
%doc %{_texmfdistdir}/doc/fonts/lfb/lfbacc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 753298
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718850
- texlive-lfb
- texlive-lfb
- texlive-lfb
- texlive-lfb

