%define modname	File-Find-Rule-Perl
%define modver 1.16

Summary:	Common rules for searching for Perl things
Name:		perl-%{modname}
Version:	%{modver}
Release:	1
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://github.com/karenetheridge/File-Find-Rule-Perl
Source0:	https://cpan.metacpan.org/authors/id/E/ET/ETHER/File-Find-Rule-Perl-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(inc::Module::Install::DSL)
BuildRequires:	perl(Parse::CPAN::Meta)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Find::Rule)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Params::Util)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
I write a lot of things that muck with Perl files. And it always annoyed me
that finding "perl files" requires a moderately complex the
File::Find::Rule manpage pattern.

*File::Find::Rule::Perl* provides methods for finding various Perl-related
files.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc README LICENSE Changes
%{perl_vendorlib}/*
%{_mandir}/man3/*



