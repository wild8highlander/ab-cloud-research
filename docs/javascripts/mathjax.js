window.MathJax = {
  tex: { inlineMath: [["\(", "\)"]], displayMath: [["\[", "\]"]] },
  options: { ignoreHtmlClass: ".*", processHtmlClass: "tex2jax_process" }
};
document$.subscribe(() => {
  MathJax.typesetPromise()
})
