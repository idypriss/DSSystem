function init() {
  // initialisation stuff here
}

function findById() {
      document.getElementById("indexButton").disabled = true;
      var id = document.getElementById("indices").value;
      $.ajax({
        url: "https://localhost:5001/api/Indici/" + id,
        type: "GET",
        contentType: "application/json",
        data: "",
        success: function(result) {
          showResult(JSON.parse(result));
        },
        error: function(xhr, status, p3, p4) {
          var err = "Error " + status + " " + p3;
          if (xhr.responseText && xhr.responseText[0] == "{") {
            err = JSON.parse(xhr.responseText).message;
          }
          alert(err);
        }
      });
}
function showResult(res) {
	document.getElementById('txtarea').value += res.text;
	renderImage(res.img);
	document.getElementById("indexButton").disabled = false;
}

function renderImage(images) {
	images.forEach(base64ImageString => {
		var baseStr64 = base64ImageString;
		baseStr64 = baseStr64.substring(0, baseStr64.length - 1);
		baseStr64 = baseStr64.substring(2, baseStr64.length);
		var image = new Image();
		image.style = "width: 100%";
		image.src = 'data:image/png;base64,' + baseStr64;
		document.getElementById("charts").appendChild(image);
	});
}


//portfoglio stampa

$(document).ready(function portfoglio_asset() {
  //fetching data from json file
  $.getJson("./Dataset.json",function (data){
    var obj=''; 
    $.each(data,function(key, value){
      student += "sp500: " + value.sp500; 
      student += "b: " + value.b; 
    
    });
    $('#portafoglioButton').append(student);
  });
});
  
  
    