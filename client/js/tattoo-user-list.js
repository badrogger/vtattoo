$(document).ready(function(){
    var userTattoos;
    userCardsEl = document.getElementsByClassName("card-img-top");
    // console.log(indexCardsEl);
    $.ajax({
           url: addHost_("tattoo-users/"),
           type: 'GET',
           headers: {"Authorization": "Token " + localStorage.getItem('token')},
           data: { get_param: 'value' },
           dataType: 'json',
           success: function (data) {
               // console.info(data)
               var len = 6;
               userTattoos = data.results.slice(0, len);
               len = Math.min(len, userTattoos.length);
               var cardsHtml = "";
               for (var i = 0; i < len; ++i) {
                    cardsHtml +=  '<div class="col-lg-4 col-md-6 mb-4"> <div id="test" class="card h-100"> <a href="#"><img class="card-img-top" src="' + userTattoos[i].image_file
                    + '" alt=""></a> <div class="card-body"> <h4 class="card-title"> </h4> <p class="card-text"></p> </div> <div class="card-footer"> <small class="text-muted">&#9733; &#9733; &#9733; &#9733; &#9734;</small> </div> </div> </div>';


                    // userCardsEl[i].src = userTattoos[i].image_file;
               }
               $("#mainRow").html(cardsHtml);
           }
        });
});
