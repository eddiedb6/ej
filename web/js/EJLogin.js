function EJLogin(uidUsername, uidPassword) {
    var username = W3GetUIValue(uidUsername);
    var password = W3GetUIValue(uidPassword);
	
    var loginRequest = W3CreateAPI("aidLogin", username, password);
    if (loginRequest == "") {
	alert("Create login request failed!");
	return;
    }

    W3CallAPIAsync(loginRequest, function(data, status) {
	var result = eval("(" + data + ")");
	if (result[w3ApiResultStatus] != w3ApiResultSuccessful) {
	    W3LogWarning("Login failed!");
	    alert("Login failed!");
	    return;
	}

	var apiDef = W3GetAPIDef("aidLogin");
	var session = result[w3ApiResultData][apiDef[w3ApiResult][w3ApiResultData][0][w3ApiDataValue]];
	W3LogInfo("Get session: " + session);
	W3LogInfo("Login successfully");

	W3SetVariable(w3Session, session);

	// Redirect to finance page
	var pageRequest = W3CreateAPI("aidPage", "uidPageFinance");
	if (pageRequest == "") {
	    alert("Create finance page request failed!");
	    return;
	}
	W3CallAPI(pageRequest);
    });
}
