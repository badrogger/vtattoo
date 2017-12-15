 if (localStorage.name != undefined) {
        $("#signin-btn").css("display", "none");
        $("#signup-btn").css("display", "none");
        $("#user-btn").css("display", "block");
        $("#create-btn").css("display", "block");
        $("#user-tattoos-btn").css("display", "block");

        $("#logout-btn").css("display", "block");
        $("#user-link").html(
            "Welcome, " + "<span style='color: #ffd500;'>"
            + localStorage.name + "</span>"
        );
    } else {
        $("#signin-btn").css("display", "block");
        $("#signup-btn").css("display", "block");
        $("#user-btn").css("display", "none");
        $("#logout-btn").css("display", "none");
    }

$(document).ready(function(){
    $("#logout-btn").click(function(data) {
        localStorage.clear();
        window.location.href = "index.html";
        return false
    });
    });
