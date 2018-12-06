# http://github.com/hashicorp/go-checkpoint

%global goipath         github.com/hashicorp/go-checkpoint
%global commit          e4b2dc34c0f698ee04750bf2035d8b9384233e1b


%gometa -i

Name:           golang-github-hashicorp-go-checkpoint
Version:        0
Release:        0.15%{?dist}
Summary:        Hashicorp checkpoint client
License:        MPLv2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/hashicorp/go-cleanhttp)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
%gochecks -d .

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Tue Jun 12 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.14.gite4b2dc3
- Upload glide files

* Wed Feb 28 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.13.20151022gite4b2dc3
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.12.gite4b2dc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gite4b2dc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.10.gite4b2dc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.9.gite4b2dc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.gite4b2dc3
- https://fedoraproject.org/wiki/Changes/golang1.7

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.7.gite4b2dc3
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.6.gite4b2dc3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 06 2016 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.5.gite4b2dc3
- Bump to upstream e4b2dc34c0f698ee04750bf2035d8b9384233e1b
  related: #1250463

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.git88326f6
- Update to spec-2.1
  related: #1250463

* Wed Aug 05 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.2.git88326f6
- Update spec file to spec-2.0
  resolves: #1250463

* Wed Apr 15 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git88326f6
- First package for Fedora
  resolves: #1212044

