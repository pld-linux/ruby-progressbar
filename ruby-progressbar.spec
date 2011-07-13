%define pkgname progressbar
Summary:	Text progress bar library for Ruby
Name:		ruby-%{pkgname}
Version:	0.9.1
Release:	1
License:	Ruby License
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	4ca56a4052fbfdaeebae15f3525c4178
Group:		Development/Languages
URL:		https://github.com/peleteiro/progressbar
BuildRequires:	rpmbuild(macros) >= 1.484
BuildRequires:	ruby >= 1:1.8.6
BuildRequires:	ruby-modules
BuildRequires:	setup.rb
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# nothing to be placed there. we're not noarch only because of ruby packaging
%define		_enable_debug_packages	0

%description
Ruby/ProgressBar is a text progress bar library for Ruby.
It can indicate progress with percentage, a progress bar,
and estimated remaining time.

%package rdoc
Summary:	HTML documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie HTML dla %{pkgname}
Group:		Documentation
Requires:	ruby >= 1:1.8.7-4

%description rdoc
HTML documentation for %{pkgname}.

%description rdoc -l pl.UTF-8
Dokumentacja w formacie HTML dla %{pkgname}.

%package ri
Summary:	ri documentation for %{pkgname}
Summary(pl.UTF-8):	Dokumentacja w formacie ri dla %{pkgname}
Group:		Documentation
Requires:	ruby

%description ri
ri documentation for %{pkgname}.

%description ri -l pl.UTF-8
Dokumentacji w formacie ri dla %{pkgname}.

%prep
%setup -q -c

# gem install
%{__tar} xf %{SOURCE0} -O data.tar.gz | %{__tar} xz
find -newer README.rd -o -print | xargs touch --reference %{SOURCE0}

%build
cp %{_datadir}/setup.rb .
%{__ruby} setup.rb config \
	--rbdir=%{ruby_rubylibdir} \
	--sodir=%{ruby_archdir}

%{__ruby} setup.rb setup

rdoc --ri --op ri lib
rdoc --op rdoc lib
rm ri/created.rid

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_rubylibdir},%{ruby_ridir},%{ruby_rdocdir}}
%{__ruby} setup.rb install \
	--prefix=$RPM_BUILD_ROOT

cp -a ri/* $RPM_BUILD_ROOT%{ruby_ridir}
cp -a rdoc $RPM_BUILD_ROOT%{ruby_rdocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README.rd
%{ruby_rubylibdir}/%{pkgname}.rb

%files rdoc
%defattr(644,root,root,755)
%{ruby_rdocdir}/%{name}-%{version}

%files ri
%defattr(644,root,root,755)
%{ruby_ridir}/ProgressBar
%{ruby_ridir}/ReversedProgressBar
