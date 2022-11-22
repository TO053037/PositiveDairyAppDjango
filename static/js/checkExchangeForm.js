const textarea1 = document.getElementById("textarea-1");
const textarea2 = document.getElementById("textarea-2");
const textarea3 = document.getElementById("textarea-3");
textarea1.addEventListener("input", (event) => {
	document.getElementById("alert-not-saved-1").innerHTML =
		"変更が記録されていません。";
});

textarea2.addEventListener("input", (event) => {
	document.getElementById("alert-not-saved-2").innerHTML =
		"変更が記録されていません。";
});

textarea3.addEventListener("input", (event) => {
	document.getElementById("alert-not-saved-3").innerHTML =
		"変更が記録されていません。";
});

function deleteAlertMessage(ranking) {
	document.getElementById("alert-not-saved-" + ranking.toString()).innerHTML = "";
}
