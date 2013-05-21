%define upstream_name    File-Find-Rule-Perl
%define upstream_version 1.10

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

License:	GPL+ or Artistic
Group:		Development/Perl
Summary:	Common rules for searching for Perl things
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/File/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Parse::CPAN::Meta)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Find::Rule)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
I write a lot of things that muck with Perl files. And it always annoyed me
that finding "perl files" requires a moderately complex the
File::Find::Rule manpage pattern.

*File::Find::Rule::Perl* provides methods for finding various Perl-related
files.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc README LICENSE Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.100.0-5mdv2012.0
+ Revision: 765241
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.100.0-4
+ Revision: 763754
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.100.0-3
+ Revision: 676630
- rebuild

* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 1.100.0-2
+ Revision: 656913
- rebuild for updated spec-helper

* Thu Nov 11 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.100.0-1mdv2011.0
+ Revision: 595968
- update to new version 1.10

* Mon Aug 03 2009 Jérôme Quelin <jquelin@mandriva.org> 1.90.0-1mdv2011.0
+ Revision: 408372
- update to 1.09

* Fri Jul 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.80.0-1mdv2010.0
+ Revision: 396740
- update to 1.08
- using %%perl_convert_version
- fixed license field

* Thu Jul 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.07-1mdv2010.0
+ Revision: 396545
- update to new version 1.07

* Fri May 01 2009 Jérôme Quelin <jquelin@mandriva.org> 1.06-1mdv2010.0
+ Revision: 369777
- skipping failing tests
- update to 1.06
- adding missing prereq
- v1.05
- adding missing prereq

* Sat Aug 30 2008 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.04-1mdv2009.0
+ Revision: 277644
- import perl-File-Find-Rule-Perl


