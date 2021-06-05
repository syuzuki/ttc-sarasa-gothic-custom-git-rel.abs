# `ttc-sarasa-gothic-custom-git-rel`

Arch Linux package builder for customized [Sarasa Gothic][sarasa].

This package can customize [Iosevka][iosevka], one of the bases of [Sarasa Gothic][sarasa].

[sarasa]: https://github.com/be5invis/Sarasa-Gothic
[iosevka]: https://github.com/be5invis/Iosevka

## Installing

1. Clone the repository

    ```sh
    $ git clone https://github.com/syuzuki/ttc-sarasa-gothic-custom-git-rel.abs.git
    $ cd ttc-sarasa-gothic-custom-git-rel.abs
    ```

    You can edit `private-build-plans.toml` for your own [Iosevka][iosevka] configuration and update checksum in `PKGBUILD`.

1. Install [AUR][aur] dependencies

    Install [AUR][aur] dependencies before building because `makepkg -s` cannot install [AUR][aur] packages.
    Below comamnd uses [Yay][yay].

    ```sh
    $ yay -S --asdeps --mflags --nocheck otfcc afdko ttfautohint
    ```

    Note that pass `--nocheck` to `makepkg` because [python-fontpens][python-fontpens] and [python-fontparts][python-fontparts] have circular check dependencies.

    [aur]: https://aur.archlinux.org/
    [yay]: https://github.com/Jguer/yay
    [python-fontpens]: https://aur.archlinux.org/packages/python-fontpens/
    [python-fontparts]: https://aur.archlinux.org/packages/python-fontparts/

1. Build and install the font

    Run `makepkg` to build and install the font.
    Building takes many hours.

    ```sh
    $ makepkg -si
    ```
