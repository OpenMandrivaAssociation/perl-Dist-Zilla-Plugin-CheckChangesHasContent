%define upstream_name    Dist-Zilla-Plugin-CheckChangesHasContent
%define upstream_version 0.006

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Ensure Changes has content before releasing

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Dist/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Capture::Tiny)
BuildRequires:	perl(Dist::Zilla)
BuildRequires:	perl(Dist::Zilla::Role::BeforeRelease)
BuildRequires:	perl(Dist::Zilla::Tester)
BuildRequires:	perl(File::Find)
BuildRequires:	perl(File::Temp)
BuildRequires:	perl(File::pushd)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl(autodie)
BuildRequires:	perl(namespace::autoclean)
BuildArch:	noarch

%description
Foo the foo.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
#make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*



