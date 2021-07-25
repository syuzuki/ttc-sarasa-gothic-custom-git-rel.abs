# Maintainer: syuzuki <syuzuki15@gmail.com>
pkgname=ttf-sarasa-gothic-custom-nerd-gitrel
pkgver=0.32.14
pkgrel=1
pkgdesc='Customized Sarasa Gothic + Nerd Fonts'
arch=('any')
url='https://github.com/be5invis/Sarasa-Gothic'
license=('custom:OFL')
depends=()
makedepends=('git' 'nodejs>=12.16.0' 'npm' 'python' 'python-fonttools' 'fontforge' 'otfcc' 'afdko' 'ttfautohint')
source=(
    private-build-plans.toml
    sarasa-custom-config.patch
    sarasa-epipe-workaround.patch
    sarasa-export-glyph-names.patch
    fix-name.py
)
sha256sums=(
    SKIP
    SKIP
    9d7dcda23d80073da9539796ad9158ad87e0e222e96f2089c6f35e1a8787de90
    342c7e1c5752105a9998bc4c7d619ed994f17a64f3d6352d0e0cf419a1425b4e
    ba561599a9647bc1719cc9952ad687066ec305f2a40e70e280f32792f8997bb8
)

_fetch_repo() {
    local repo="$1"

    if [[ -e "${repo}" ]]; then
        (
            cd "${repo}"
            git fetch
            git clean -fd
        )
    else
        git clone --filter blob:none --no-checkout https://github.com/be5invis/"${repo}"
    fi
}

prepare() {
    _fetch_repo Iosevka
    _fetch_repo Sarasa-Gothic
    if [[ -e nerd-fonts ]]; then
        (
            cd nerd-fonts
            git fetch
            git clean -fd
        )
    else
        git clone --filter blob:none --no-checkout https://github.com/ryanoasis/nerd-fonts
    fi

    cd Sarasa-Gothic
    local sarasa_tag="$(git for-each-ref --merged=@{u} --sort=-committerdate --count=1 --format='%(refname:lstrip=2)' refs/tags)"
    local sarasa_tag_date="$(git show --format='format:%ct' "${sarasa_tag}")"
    git reset --hard "${sarasa_tag}"
    patch -N -p 1 <../sarasa-custom-config.patch
    patch -N -p 1 <../sarasa-epipe-workaround.patch
    patch -N -p 1 <../sarasa-export-glyph-names.patch

    cd ../Iosevka
    local iosevka_tags="$(git for-each-ref --merged=@{u} --sort=-committerdate --format='%(refname:lstrip=2) %(committerdate:unix)' refs/tags)"
    local iosevka_tag="$(awk "\$2 <= ${sarasa_tag_date} { print \$1; exit }" <<<"${iosevka_tags}")"
    git reset --hard "${iosevka_tag}"
    ln -sf ../private-build-plans.toml .

    cd ../nerd-fonts
    git sparse-checkout init --cone
    git sparse-checkout set src/glyphs
    local nerd_commit="$(git log --first-parent --until "${sarasa_tag_date}" -n 1 --format='%H' @{u})"
    git reset --hard "${nerd_commit}"
}

pkgver() {
    cd Sarasa-Gothic
    local tag="$(git describe --tags)"
    echo "${tag#v}"
}

build() {
    cd Iosevka
    npm install
    npm update
    npm run build -- ttf-unhinted::iosevka-custom-{term,fixed}

    cd ../Sarasa-Gothic
    for style in term fixed; do
        ln -s "../../Iosevka/dist/iosevka-custom-${style}/ttf-unhinted" "sources/iosevka-custom-${style}"
    done
    npm install
    npm update
    npm run build ttf

    cd ../nerd-fonts
    mkdir tmp1 tmp2 out
    for family in gothic:Gothic ui:UI term:Term fixed:Fixed; do
        for style in regular:'' bold:'Bold' italic:'Italic' bolditalic:'Bold Italic'; do
            local style_text="${style#*:}"
            ./font-patcher --material --careful "../Sarasa-Gothic/out/ttf/sarasa-${family%:*}-j-${style%:*}.ttf" --outputdir tmp1
            ./font-patcher --fontawesome --fontawesomeextension --fontlinux --octicons --powersymbols --pomicons --powerline --powerlineextra --weather "tmp1/Sarasa ${family#*:} J${style_text:+ ${style_text}} Nerd Font Plus Material Design Icons.ttf" --outputdir tmp2
            ../fix-name.py "${family#*:}" "${style_text}" "tmp2/Sarasa ${family#*:} J${style_text:+ ${style_text}} Nerd Font Plus Material Design Icons Nerd Font Plus Font Awesome Plus Font Awesome Extension Plus Octicons Plus Power Symbols Plus Pomicons Plus Font Logos (Font Linux) Plus Weather Icons.ttf" "out/sarasa-nerd-${family%:*}-j-${style%:*}.ttf"
        done
    done
}

package() {
    install -D -m 644 -t "${pkgdir}/usr/share/fonts/sarasa-gothic-nerd" nerd-fonts/out/*.ttf
    install -D -m 644 -t "${pkgdir}/usr/share/licenses/${pkgname}" Sarasa-Gothic/LICENSE
}
