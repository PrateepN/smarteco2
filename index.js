'use strict';

const express = require('express');
const bodyParser = require('body-parser');

const restService = express();

//added for SC testing
var OAuth = require('oauth-1.0a');
var crypto = require('crypto');
var request = require('request');
var json = require('json');

restService.use(bodyParser.urlencoded({
    extended: true
}));

restService.use(bodyParser.json());

restService.post('/echo', function(req, res) {
	//var speech = "Something went wrong. Please try again.";

	if(req.body.result.parameters.NewFolderName)
	{
		var speech="Folder created. Please check the CMS.";
	var oauth = new OAuth({
    consumer: {
      key: '6e83adcc-09b3-4514-bb4f-442cfa21c019!TradeDocsThunderhead@sapient.com.trial',
      secret: 'ab97a83f-bc76-4784-a559-bac258fb7dde'
    },signature_method: 'HMAC-SHA1',
    hash_function: function(base_string, key) {
      return crypto.createHmac('sha1', key).update(base_string).digest('base64');
    }
  });
  
  var request_data = {
    url: 'https://na4.smartcommunications.cloud/one/oauth1/cms/v4/folders',
	//url: 'https://na4.smartcommunications.cloud/one/',
	//url: 'https://na4.smartcommunications.cloud/one/',
    method: 'POST',
    data: {
      name: req.body.result.parameters.NewFolderName,
	  parentId: req.body.result.parameters.ParentID
    },

};


request({
    url: request_data.url,
    method: request_data.method,
    form: request_data.data,
    headers: oauth.toHeader(oauth.authorize(request_data))
}, function(error, response, body) {
    if (error){ 
	    console.error(error);
	    
    }
	else{
		if(body)
		{
		var xml2js = require('xml2js');
  		var parser = new xml2js.Parser();
  		parser.parseString(body, function (err, result) {
  		var locspeech = result['errorinfo']['msg'];
  		if (locspeech)
		{
			speech=locspeech;
		}		
});
		}
		console.log("Final speech: "+speech);
		console.log(body);
	return res.json({
        speech: speech,
        displayText: speech,
        source: 'webhook-echo-sample'
	
	});
	}

		
    });
	}
	else{
	
   var speech = req.body.result && req.body.result.parameters && req.body.result.parameters.PolicyNumber ? req.body.result.parameters.PolicyNumber+" is available but SC is not connected." : "Seems like some problem. Speak again."
	
	console.log("Final speech: "+speech);
    return res.json({
        speech: speech,
        displayText: speech,
        source: 'webhook-echo-sample'
    });
	}
});
restService.listen((process.env.PORT || 8000), function() {
    console.log("Server up and listening");
});
