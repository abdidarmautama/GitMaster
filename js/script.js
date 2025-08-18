// Header tetap tampil di atas saat scroll
document.addEventListener("DOMContentLoaded", function () {
	var header = document.querySelector("header");
	header.style.position = "fixed";
	header.style.top = "0";
	header.style.left = "0";
	header.style.width = "100%";
	header.style.zIndex = "1000";
});
