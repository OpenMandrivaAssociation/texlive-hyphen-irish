# revision 23092
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-irish
Version:	20120124
Release:	1
Summary:	Irish hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-irish.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Irish (Gaeilge) in T1/EC and UTF-8
encodings. Visit http://borel.slu.edu/fleiscin/index.html for
more information.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-irish
%_texmf_language_def_d/hyphen-irish
%_texmf_language_lua_d/hyphen-irish

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-irish <<EOF
\%% from hyphen-irish:
irish loadhyph-ga.tex
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_dat_d}/hyphen-irish
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-irish <<EOF
\%% from hyphen-irish:
\addlanguage{irish}{loadhyph-ga.tex}{}{2}{3}
EOF
perl -pi -e 's|\\%%|%%|;' %{buildroot}%{_texmf_language_def_d}/hyphen-irish
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-irish <<EOF
-- from hyphen-irish:
	['irish'] = {
		loader = 'loadhyph-ga.tex',
		lefthyphenmin = 2,
		righthyphenmin = 3,
		synonyms = {  },
		patterns = 'hyph-ga.pat.txt',
		hyphenation = 'hyph-ga.hyp.txt',
	},
EOF
