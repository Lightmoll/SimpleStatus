var hash = window.location.hash.substr(1);
if (hash == "email_added") {
	document.getElementById("pop_up").style.display = "unset";
}

time_array = document.getElementsByClassName("time");

for (var i = 0; i < time_array.length; i++) {
	try {
		if (time_array[i].innerHTML.slice(-1) == "Z") {
			date_object = new Date(time_array[i].innerHTML);
			time_array[i].innerHTML = date_object.toLocaleString();
		}
	} catch(err) {
		console.log(err);
	}
}