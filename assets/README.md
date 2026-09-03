# assets — Project Branding

Currently a single file:

| File | Purpose |
|---|---|
| `banner.svg` | the repository banner rendered at the top of the root README (project title, the AB-cloud motif: a Hofstadter-style phase field with vortex flux tubes over the critical-line zeros) |

## Notes

- SVG is used deliberately: it stays crisp on retina displays and costs a
  few kilobytes, unlike a raster banner.
- The banner is referenced from `../README.md` as
  `assets/banner.svg` with a relative path, so it renders both on GitHub
  and on the MkDocs site.
- Adding a new asset? Keep this folder for images only — figures that
  belong to documents live in `../monographs/*/figures/` and
  `../monographs/original-v21/media/`, run plots in `../results/` (to be
  regenerated) — and register the file in this README.

## Кратко (по-русски)

- Папка брендинга: пока только `banner.svg` — баннер корневого README
  (мотив AB-облака: фазовое поле в стиле Хофштадтера с вихревыми трубками
  над нулями критической прямой).
- SVG выбран ради чёткости на retina и малого размера; путь в README
  относительный — работает и на GitHub, и на MkDocs-сайте.
