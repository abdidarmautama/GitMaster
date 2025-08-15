# Copilot Instructions for GitMaster

## Project Overview
- This is a simple static website project using HTML, Tailwind CSS (via CDN), and a custom stylesheet (`css/style.css`).
- JavaScript logic is placed in `js/script.js` and is used for dynamic form handling and output rendering.
- The site consists of a header, three main sections (Welcome, Profile, Message), and a fixed footer.

## Key Files & Structure
- `index.html`: Main entry point. Contains all layout sections and links to CSS/JS.
- `css/style.css`: Custom styles. Tailwind is loaded via CDN for utility classes.
- `js/script.js`: Handles form submission in the Message section and prints results to the output column.
- `RevoU favicon.svg`: Logo image used in the header.

## Patterns & Conventions
- Layout uses Tailwind utility classes for rapid prototyping. Custom styles are minimal and reside in `css/style.css`.
- The header navigation uses anchor tags. The 'Message Us' button scrolls to the Message section using an anchor (`#section-message`) and smooth scroll via JS.
- The Message section is split into two columns: left for the form, right for output. Output is rendered by JS into a div with `id="output-message"`.
- All form fields use unique IDs for easy JS selection.
- Footer is fixed at the bottom using Tailwind and inline styles.

## Developer Workflows
- No build step; all files are static and can be opened directly in a browser.
- For local development, edit `index.html`, `css/style.css`, and `js/script.js` as needed. Refresh browser to see changes.
- To add new sections or navigation, follow the existing pattern in `index.html`.
- To extend JS logic, use event listeners and DOM manipulation as shown in `js/script.js`.

## Integration Points
- Tailwind CSS is loaded via CDN. No local build or configuration required.
- No backend or API integration; all logic is client-side.
- Images and assets should be placed in the root or referenced folders.

## Example: Form Output Pattern
```html
<!-- Form in section-message -->
<form>
  <input id="nama" ...>
  <input id="tanggal" ...>
  <input type="radio" name="gender" ...>
  <textarea id="pesan" ...></textarea>
</form>
<div id="output-message"></div>
```
```js
// js/script.js
form.addEventListener('submit', function(e) {
  // Collect values and print to #output-message
});
```

## Notes
- Keep markup and logic simple; avoid frameworks or complex build tools.
- Use Tailwind utility classes for layout and spacing.
- For accessibility, ensure all form fields have labels and unique IDs.

---

_If any section is unclear or missing, please provide feedback to improve these instructions._
