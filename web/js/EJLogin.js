function EJLogin(uidUsername, uidPassword) {
    var getTokenRequest = W3CreateAPI("aidToken");
    if (getTokenRequest == "") {
	return;
    }

    var loginFunc = function() {
	var username = W3GetUIValue(uidUsername);
	var password = W3GetUIValue(uidPassword);
	
	var loginRequest = W3CreateAPI("aidLogin", username, password);
	if (loginRequest == "") {
	    return;
	}

	// Step 3: Do login
	W3CallAPIAsync(loginRequest, function(data, status) {
	    W3LogDebug(data);
	    W3LogDebug(status);
	
	    var result = eval("(" + data + ")");
	    if (result[w3ApiResultStatus] != w3ApiResultSuccessful) {
		W3LogWarning("Login failed")
		return;
	    }

	    var apiDef = W3GetAPIDef("aidLogin");
	    var session = result[w3ApiResultData][apiDef[w3ApiResult][w3ApiResultData][0][w3ApiDataValue]];
	    W3LogInfo("Get session: " + session);
	    W3LogInfo("Login successfully");
	});
    }
    
    var sendEncryptionFunc = function (encryption) {
	var sendEncryptionRequest = W3CreateAPI("aidEncryption", encryption);
	if (sendEncryptionRequest == "") {
	    return;
	}

	// Step 2: Generate client encryption which encrypt by server token and send back to server
	W3CallAPIAsync(sendEncryptionRequest, function(data, status) {
	    W3LogDebug(data);
	    W3LogDebug(status);

	    var result = eval("(" + data + ")");
	    if (result[w3ApiResultStatus] != w3ApiResultSuccessful) {
		W3LogWarning("Send encryption failed")
		return;
	    }

	    loginFunc();
	});
    };

    // Step 1: Get token from sever
    W3CallAPIAsync(getTokenRequest, function(data, status) {
	W3LogDebug(data);
	W3LogDebug(status);
	
	var tokenResult = eval("(" + data + ")");
	if (tokenResult[w3ApiResultStatus] != w3ApiResultSuccessful) {
	    W3LogWarning("Get token failed")
	    return;
	}

	var apiDef = W3GetAPIDef("aidToken");
	var token = tokenResult[w3ApiResultData][apiDef[w3ApiResult][w3ApiResultData][0][w3ApiDataValue]];
	W3LogInfo("Get token: " + token);

	// TODO
	var encryption = "def456-"
	sendEncryptionFunc(encryption);
    });
}
