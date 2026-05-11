// Check if the user is on a Mac and update the shortcut key for search accordingly.
// Preserve the responsive `.search-shortcut.d-none.d-sm-inline` wrapper so the label
// stays hidden on small screens (keeping only the magnifying glass icon).
document.addEventListener("readystatechange", () => {
  if (document.readyState === "interactive") {
    let isMac = navigator.platform.toUpperCase().indexOf("MAC") >= 0;
    let shortcutKeyElement = document.querySelector("#search-toggle .nav-link");
    if (shortcutKeyElement && isMac) {
      shortcutKeyElement.innerHTML =
        '<span class="search-shortcut d-none d-sm-inline">&#x2318; k </span><i class="fa-solid fa-magnifying-glass"></i>';
    }
  }
});
