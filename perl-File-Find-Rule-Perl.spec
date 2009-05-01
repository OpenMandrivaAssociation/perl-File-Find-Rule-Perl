%define realname   File-Find-Rule-Perl
%define version    1.06
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Common rules for searching for Perl things
Source:     http://www.cpan.org/modules/by-module/File/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: perl-devel
BuildRequires: perl(Parse::CPAN::Meta)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(File::Find::Rule)
BuildRequires: perl(File::Spec)
BuildRequires: perl(Params::Util)
BuildRequires: perl(Test::More)

BuildArch: noarch

%description
I write a lot of things that muck with Perl files. And it always annoyed me
that finding "perl files" requires a moderately complex the
File::Find::Rule manpage pattern.

*File::Find::Rule::Perl* provides methods for finding various Perl-related
files.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE Changes
%{_mandir}/man3/*
%perl_vendorlib/*
