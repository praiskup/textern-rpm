%global gitrev          5339fb6
%global posttag         git%{gitrev}
%global snapshot        %{version}-%{posttag}

# this enforces us to create non-noarch package
%global native_dir      %_libdir/mozilla/native-messaging-hosts

%global __brp_python_bytecompile :

Name:           textern
Version:        0.%posttag
Release:        2%{?dist}
Summary:        Firefox add-on for editing text in your favorite external editor

License:        GPLv3
URL:            https://github.com/jlebon/textern

# curl https://api.github.com/repos/jlebon/textern/tarball/5339fb6 > tarball
Source0:        jlebon-textern-%gitrev.tar.gz

Patch0:         textern-5339fb6-build.patch

BuildArch:      noarch

Requires:       mozilla-filesystem
Requires:       python3-inotify_simple

BuildRequires:  make
BuildRequires:  python3-devel

%description
Textern is a Firefox add-on that allows you to edit text areas in web pages
using an external editor.  It is similar in functionality to the popular
It's All Text! add-on, though makes use of the WebExtension API and is thus
fully compatible with multiprocessing and supported beyond Firefox 57.

This is not a self-standing Firefox add-on, it's only the "native" application
used by Add-on named "textern".  Please install the Add-on manually.


%prep
%autosetup -p1 -n jlebon-textern-%gitrev


%build


%install
make native-install \
    PREFIX=/usr \
    MOZILLA_NATIVE=%native_dir \
    DESTDIR=%buildroot


%files
%license LICENSE
%doc README.md
%dir %native_dir
%native_dir/textern.json
%dir %_libexecdir/textern
%_libexecdir/textern/textern.py


%changelog
* Tue Aug 21 2018 Pavel Raiskup <praiskup@redhat.com> - 0.git5339fb6-2
- s/simple_inotify/inotify_simple/

* Tue Aug 21 2018 Pavel Raiskup <praiskup@redhat.com> - 0.git5339fb6-1
- initial rpm packaging
