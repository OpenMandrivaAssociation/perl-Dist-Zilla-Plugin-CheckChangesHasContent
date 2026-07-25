%define upstream_name    Dist-Zilla-Plugin-CheckChangesHasContent
%define upstream_version 0.011

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Ensure Changes has content before releasing

License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/dagolden/Dist-Zilla-Plugin-CheckChangesHasContent
Source0:	https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Dist-Zilla-Plugin-CheckChangesHasContent-%{upstream_version}.tar.gz

BuildRequires:	make
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



