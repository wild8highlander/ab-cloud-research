# 🎨 assets/ — фирменные артефакты

| Файл | Что это | Как получен |
|------|---------|-------------|
| `banner.gif` (~331 КБ, 42 кадра) | анимированный баннер: нули ζ поднимаются по критической прямой Re(s)=½, волна Z(t) дышит фазой | `scripts/make_banner.py` (matplotlib → PIL GIF), данные — открытые ординаты Одлыжко, детерминированные |
| `logo_abcloud.svg` | векторный логотип: спираль 12 нулей вокруг критической прямой | генерируется тем же скриптом |
| `logo_abcloud_light.png` / `logo_abcloud_dark.png` | растровые версии для светлой/тёмной темы README (picture-элемент) | matplotlib |

Баннер используется в главном README (GitHub рендерит анимацию в `<img>`).
Цвета — палитра «Critical Line & Copper», единая с фигурами и монографиями.

## English summary

Family branding assets: the animated banner (42 frames, ζ zeros climbing the
critical line), the vector logo and light/dark PNG variants — all generated
deterministically by `scripts/make_banner.py` in the family palette.
