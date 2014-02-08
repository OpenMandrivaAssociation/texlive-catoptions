# revision 24899
# category Package
# catalog-ctan /macros/latex/contrib/catoptions
# catalog-date 2011-12-19 23:56:31 +0100
# catalog-license lppl1.3
# catalog-version 0.2.7b
Name:		texlive-catoptions
Version:	0.2.7b
Release:	3
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


%changelog
* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2.7b-2
+ Revision: 750037
- Rebuild to reduce used resources

* Mon Dec 26 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2.7b-1
+ Revision: 745161
- texlive-catoptions

* Sat Dec 17 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2.7a-1
+ Revision: 743242
- texlive-catoptions
- texlive-catoptions

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2.6-1
+ Revision: 718014
- texlive-catoptions
- texlive-catoptions
- texlive-catoptions
- texlive-catoptions
- texlive-catoptions

