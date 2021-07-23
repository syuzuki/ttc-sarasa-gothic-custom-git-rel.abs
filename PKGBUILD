# Maintainer: syuzuki <syuzuki15@gmail.com>
pkgname=ttc-sarasa-gothic-custom-git-rel
pkgver=0.32.13
pkgrel=1
pkgdesc='Customized Sarasa Gothic; a CJK programming font.'
arch=('any')
url='https://github.com/be5invis/Sarasa-Gothic'
license=('custom:OFL')
depends=()
makedepends=('git' 'nodejs>=12.16.0' 'npm' 'python-fonttools' 'otfcc' 'afdko' 'ttfautohint')
replaces=('ttf-sarasa-gothic')
source=(
    private-build-plans.toml
    sarasa-custom-config.patch
    sarasa-epipe-workaround.patch
)
sha256sums=(
    SKIP
    909396a05bf820b220e4bab8790c55defe70bfdbb86d5fa3c0f39609735e88f0
    9d7dcda23d80073da9539796ad9158ad87e0e222e96f2089c6f35e1a8787de90
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

    cd Sarasa-Gothic
    local sarasa_tag="$(git for-each-ref --merged=@{u} --sort=-committerdate --count=1 --format='%(refname:lstrip=2)' refs/tags)"
    local sarasa_tag_date="$(git show --format='format:%ct' "${sarasa_tag}")"
    git reset --hard "${sarasa_tag}"
    patch -N -p 1 <../sarasa-custom-config.patch
    patch -N -p 1 <../sarasa-epipe-workaround.patch

    cd ../Iosevka
    local iosevka_tags="$(git for-each-ref --merged=@{u} --sort=-committerdate --format='%(refname:lstrip=2) %(committerdate:unix)' refs/tags)"
    local iosevka_tag="$(awk "\$2 <= ${sarasa_tag_date} { print \$1; exit }" <<<"${iosevka_tags}")"
    git reset --hard "${iosevka_tag}"
    ln -sf ../private-build-plans.toml .
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
    npm run build ttc
}

package() {
    install -D -m 644 -t "${pkgdir}/usr/share/fonts/sarasa-gothic" Sarasa-Gothic/out/ttc/*.ttc
    install -D -m 644 -t "${pkgdir}/usr/share/licenses/${pkgname}" Sarasa-Gothic/LICENSE
}
