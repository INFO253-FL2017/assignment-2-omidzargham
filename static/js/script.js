var inputName = document.getElementById('inputName');
var subject = document.getElementById('subject');
var message = document.getElementById('message');
var form = document.getElementById('form');
var messageArea = document.getElementById('messageArea');

form.addEventListener('submit', handleSubmit);

function handleSubmit(event) {
	if (subject.value != "" && inputName.value != "" && message.value != "") {
		messageArea.innerHTML = "Your message has been sent";
	}
	else {
		messageArea.innerHTML = "Missing fields: " + handleSubmitHelper();
	}
	//event.preventDefault();
}

function handleSubmitHelper() {
	finalString = ""
	if (inputName.value == "") {
		finalString += "name, ";
	}
	if (subject.value == "") {
		finalString += "subject, ";
	}
	if (message.value == "") {
		finalString += "message, ";
	}
	finalString = finalString.slice(0, -2)
	return finalString
}

