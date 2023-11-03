Name:		compat-srpm-macros
Version:	2023.11
Release:	1
Summary:	RPM macros for compatible building
Group:		Applications/Engineering
License:	MIT License
Source0:	macros.compat-srpm
BuildArch:	noarch

%description
macros.compat-srpm provides macros for building projects from
various distributions compatibly.

%prep
%setup -T

%build

%install
rm -rf $RPM_BUILD_ROOT
install -Dm644 %{SOURCE0} %{buildroot}%{_rpmconfigdir}/macros.d/macros.compat-srpm
   
%clean 
rm -rf $RPM_BUILD_ROOT

%files
%doc LICENSE
%{_rpmconfigdir}/macros.d/macros.compat-srpm

%changelog
* Sun Nov 05 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2023.11
- Initial package
