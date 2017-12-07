function EJLogin(uidUsername, uidPassword) {
    var getTokenRequest = W3CreateAPI("aidToken");
    if (getTokenRequest == "") {
	return;
    }
    
    W3LogDebug("Trigger API: " + getTokenRequest);
    $.get(getTokenRequest, function(data, status) {
	W3LogDebug("status: " + status);
	W3LogDebug("data: " + data);
	
	for (var index in listeners) {
	    W3ExecuteFuncFromString(listeners[index], data, status);
	}		    
    });
}

function EJOnLogin(data, status) {
    alert("data: " + data + "\nstatus: " + status);
}
