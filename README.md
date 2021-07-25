# `ttf-sarasa-gothic-custom-nerd-gitrel`

Arch Linux package builder for customized [Sarasa Gothic][sarasa] + [Nerd Fonts][nerd].

This package can build [Sarasa Gothic][sarasa] with customized [Iosevka][iosevka] plans.
Generated families and styles are limited for faster build time.

Built families:

* Sarasa Nerd Gothic J
* Sarasa Nerd UI J
* Sarasa Nerd Term J
* Sarasa Nerd Fixed J

Built styles:

* Regular
* Bold
* Italic
* Bold Italic

[sarasa]: https://github.com/be5invis/Sarasa-Gothic
[iosevka]: https://github.com/be5invis/Iosevka
[nerd]: https://github.com/ryanoasis/nerd-fonts

## Installation

1. Clone the repository

    ```sh
    $ git clone https://github.com/syuzuki/ttc-sarasa-gothic-custom-git-rel.abs.git
    $ cd ttc-sarasa-gothic-custom-git-rel.abs
    ```

    You can edit `private-build-plans.toml` for your own [Iosevka][iosevka] configuration and update checksum in `PKGBUILD`.
    `sarasa-custom-term` and `sarasa-custom-fixed` build plans is required.

1. Install [AUR][aur] dependencies

    Before building, Install [AUR][aur] dependencies manually because `makepkg -s` cannot install [AUR][aur] packages.
    Below comamnd uses [Yay][yay].

    ```sh
    $ yay -S --asdeps --mflags --nocheck otfcc afdko ttfautohint
    ```

    Note that you need to pass `--nocheck` option to `makepkg` because [python-fontpens][python-fontpens] and [python-fontparts][python-fontparts] depended by [AFDKO][afdko] have circular check dependencies.

    [aur]: https://aur.archlinux.org/
    [yay]: https://github.com/Jguer/yay
    [python-fontpens]: https://aur.archlinux.org/packages/python-fontpens/
    [python-fontparts]: https://aur.archlinux.org/packages/python-fontparts/
    [afdko]: https://aur.archlinux.org/packages/afdko/

1. Build and install the font

    Run `makepkg` to build and install the font.
    Building takes many hours.

    ```sh
    $ makepkg -si
    ```
