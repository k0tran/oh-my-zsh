Name:      oh-my-zsh
Version:   20240806.7337
Release:   alt1

Summary:   A community-driven framework for managing your zsh configuration
License:   MIT
Group:     Shells
Url:       https://ohmyz.sh
VCS:       https://github.com/ohmyzsh/ohmyzsh
BuildArch: noarch

Source:    %name-%version.tar
Patch:     oh-my-zsh-20240806.7337-alt-config.patch

Requires:  zsh
BuildRequires(pre): rpm-build-python3

%description
A community-driven framework for managing your zsh configuration. Includes 180+ optional plugins
and over 120 themes to spice up your morning, and an auto-update tool so that makes it easy to keep
up with the latest updates from the community.

%prep
%setup
cp templates/zshrc.zsh-template zshrc
%patch -p1

%install
mkdir -p %buildroot%_datadir/%name
cp -r * %buildroot%_datadir/%name/.

%post
echo "You have to execute 'cp %_datadir/%name/zshrc ~/.zshrc' to use it."

%postun
echo "Please remove ~/.zshrc to avoid errors."

%files
%_datadir/%name/

%changelog
* Tue Aug 06 2024 Ilya Sorochan <k0tran@altlinux.org> 20240806.7337
- Initial build for ALT Linux
