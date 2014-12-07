# revision 28331
# category Package
# catalog-ctan /macros/latex/contrib/catoptions
# catalog-date 2012-11-22 12:57:51 +0100
# catalog-license lppl1.3
# catalog-version 0.2.7f
Name:		texlive-catoptions
Version:	0.2.7f
Release:	8
Summary:	Preserving and recalling standard catcodes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/catoptions
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catoptions.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catoptions.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package changes package loading internals so that all
subsequently loaded packages can rely on normal/standard
catcodes of all ASCII characters. The package defines canonical
control sequences to represent all the visible ASCII
characters. It also provides robust option parsing mechanisms
(XDeclareOption, XExecuteOptions and XProcessOptions, which
will be used by \documentclass if the package has already been
loaded). The package also provides a range of other TeX
programming tools.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/catoptions/catoptions-guide.cfg
%{_texmfdistdir}/tex/latex/catoptions/catoptions.sty
%doc %{_texmfdistdir}/doc/latex/catoptions/README
%doc %{_texmfdistdir}/doc/latex/catoptions/catoptions-guide.pdf
%doc %{_texmfdistdir}/doc/latex/catoptions/catoptions-guide.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
