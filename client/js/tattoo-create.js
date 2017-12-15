var imageData;

var file;

// Add events
$('#imageEditor input[type=file]').on('change', prepareUpload);

// Grab the files and set them to our variable
function prepareUpload(event)
{
  file = event.target.files[0];
}

$('#imageEditor').on('submit', uploadFiles);

// Catch the form submit and upload the files
function uploadFiles(event)
{
    // console.info("DAROVA");
  // event.stopPropagation(); // Stop stuff happening
    event.preventDefault(); // Totally stop stuff happening

    // START A LOADING SPINNER HERE

    // Create a formdata object and add the files
    var formData = new FormData();
    formData.append('name', $("#tattooName").val());
    formData.append('file', file, file.name);
    var xhr = new XMLHttpRequest();

    xhr.open('POST', addHost_("tattoo-upload/"), true);
    xhr.setRequestHeader("Authorization", "Token " + localStorage["token"]);
    xhr.onload = function () {
          if (xhr.status === 201) {
            $("#successAlert").css("display", "block");
          } else {
            console.info("failed");
          }
        };

    xhr.send(formData);
}


$( document ).ready(function() {
 // 	var file = new File("static/d1.jpg");
	// var reader = new FileReader();
	// 	reader.onloadend = function(){
	// 	imageData = reader.result;
	// 	// console.info(imageData)
	// 	// console.info(typeof(imageData));
 //  		$("#imageContainer img").attr("src", reader.result);
 // 	 }

 //    if (file) {
 //    	console.info(file);
 //    	reader.readAsDataURL(file);
 //    }

 //    canvasChange();
});


function addImage(e) {
	var file = document.getElementById('imgUrl').files[0];
	var reader = new FileReader();
		reader.onloadend = function(){
		imageData = reader.result;
		// console.info(imageData)
		// console.info(typeof(imageData));
  		$("#imageContainer img").attr("src", reader.result);
 	 }

    if (file) {
    	console.info(file);
    	reader.readAsDataURL(file);
    } else {

   	}
		// if (imgUrl.length) {
		// 	$("#imageContainer img").attr("src", );
		// }

	e.preventDefault();
}

//on pressing return, addImage() will be called
$("#imgUrl").change(addImage);


// editing image via css properties
function editImage() {
	var gs 		 = $("#gs").val();      // grayscale
	var blur 	 = $("#blur").val();    // blur
	var br 		 = $("#br").val();      // brightness
	var ct 		 = $("#ct").val();      // contrast
	var huer	 = $("#huer").val();    //hue-rotate
	var opacity      = $("#opacity").val(); //opacity
	var invert 	 = $("#invert").val();  //invert
	var saturate     = $("#saturate").val();//saturate
	var sepia 	 = $("#sepia").val();   //sepia

	var filter = 	'grayscale(' + gs+
			'%) blur(' + blur +
			'px) brightness(' + br +
			'%) contrast(' + ct +
			'%) hue-rotate(' + huer +
			'deg) opacity(' + opacity +
			'%) invert(' + invert +
			'%) saturate(' + saturate +
			'%) sepia(' + sepia + '%)';
	// $("#imageContainer img").css("width", "10%");
	$("#imageContainer img").css("filter", filter);
	$("#imageContainer img").css("-webkit-filter", filter);
	// canvasChange();
}


function canvasChange() {
	var canvas = document.getElementById("hiddenCanvas");
	var ctx = document.getElementById("hiddenCanvas").getContext("2d");
	var img = document.getElementById("tattooImage");
	ctx.clearRect(0, 0, canvas.width, canvas.height);

	ctx.drawImage(img, 0, 0);
	var canvasData = document.getElementById("hiddenCanvas").toDataURL("image/png", 1.0);
}


// $("#tattooImage").on(function() {
// 	canvasChange();
// });

//When sliders change image will be updated via editImage() function
$("input[type=range]").change(editImage).mousemove(editImage);

// Reset sliders back to their original values on press of 'reset'
$('#imageEditor').on('reset', function () {
	setTimeout(function() {
		editImage();
	}, 0);
});

// $("#saveTattooImage").click( function(e) {
// 	data = {}
// 	// $("#imageEditor :input").each(function() {
//  // 		var input = $(this);
//  // 		data[input.attr('id')] = input.val();
//  // 		// alert(input.attr('id'));
//  // 		// alert(input.val());
//  // 		console.info(data);
//  // 	});
//  	// obj = $("#imageEditor");
//  	canvasChange();
//  	data["tattooName"] = $("#tattooName").val();
//  	// data["colored"] = $("#tempChb").prop('checked');
//  	// data["temp"] = $("#coloredChb").prop('checked');
//  	// data["place"] = $("#placeSelect").val();
//  	data["imageData"] = imageData;
//  	var canvasData = document.getElementById("hiddenCanvas").toDataURL("image/png", 1.0);

//  	uploadUrl = addHost_("tattoo-upload/");
//  	uploadData = { "bimage": canvasData, "name" : $("#tattooName").val()};
//  	$.ajax({
//     	url: uploadUrl,
//     	type: 'post',
//     data: uploadData,
//     headers: {
//     	"Authorization": "Token " + localStorage["token"]
//     },
//     dataType: 'json',
//     success: function (data) {
//         console.info("success uploading");
//         console.info(canvasData);
//         $("#successAlert").css("display", "block");
//     }

// });

//  	e.preventDefault();
//  	// console.info(canvasData);
//  	// console.info(data);
// 	// localStorage['tattooData'] = JSON.stringify(tattooData);

// });



