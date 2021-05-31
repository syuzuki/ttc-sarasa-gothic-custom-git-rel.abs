# Maintainer: syuzuki <syuzuki15@gmail.com>
pkgname=ttf-sarasa-gothic-custom
_sarasa_ver=0.31.2
_iosevka_ver=6.1.3
pkgver="${_sarasa_ver}_${_iosevka_ver}"
pkgrel=1
pkgdesc='Customized Sarasa Gothic; a CJK programming font.'
arch=('any')
url='https://github.com/be5invis/Sarasa-Gothic'
license=('custom:OFL')
depends=()
makedepends=('git' 'nodejs>=12.16.0' 'npm' 'python-fonttools' 'otfcc' 'afdko' 'ttfautohint')
conflicts=('ttf-sarasa-gothic')
source=(
    private-build-plans.toml
    sarasa-custom-config.patch
    sarasa-epipe-workaround.patch
)
sha256sums=(
    c1067305c1d25ade0896cf87305cdaa64750b333470c96724f29c435ee4c631a
    909396a05bf820b220e4bab8790c55defe70bfdbb86d5fa3c0f39609735e88f0
    9d7dcda23d80073da9539796ad9158ad87e0e222e96f2089c6f35e1a8787de90
)

prepare() {
    for repo in "Iosevka:${_iosevka_ver}" "Sarasa-Gothic:${_sarasa_ver}"; do
        if [[ -e "${repo%%:*}" ]]; then
            (
                cd "${repo%%:*}"
                git fetch
                git reset --hard "v${repo#*:}"
                git clean -fd
            )
        else
            git clone --filter blob:none -b "v${repo#*:}" https://github.com/be5invis/"${repo%%:*}"
        fi
    done

    ln -sf ../private-build-plans.toml Iosevka
    (
        cd Sarasa-Gothic
        patch -N -p 1 <../sarasa-custom-config.patch
        patch -N -p 1 <../sarasa-epipe-workaround.patch
    )
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
}

package() {
    install -D -m 644 -t "${pkgdir}/usr/share/fonts/sarasa-gothic" Sarasa-Gothic/out/ttf/*.ttf
    install -D -m 644 -t "${pkgdir}/usr/share/licenses/${pkgname}" Sarasa-Gothic/LICENSE
}
