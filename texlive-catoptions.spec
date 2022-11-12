Name:		texlive-catoptions
Version:	35069
Release:	1
Summary:	Preserving and recalling standard catcodes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/catoptions
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catoptions.r35069.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catoptions.doc.r35069.tar.xz
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
%{_texmfdistdir}/tex/latex/catoptions
%doc %{_texmfdistdir}/doc/latex/catoptions

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
