$(document).ready(function() {

    $("button.login_to_like").click(function(){
        alert("Login to like");
    });

    $("button.login_to_buy").click(function () {
        alert("Login to purchase a feature");
    });

    $("button.login_to_add_issue").click(function () {
        alert("Login to add a new issue");
    });

    $("button.login_to_send_feedback").click(function(){
        alert("Login to send feedback");
    });
});



// Called on products.html page
// Adds a message to the user that the item has been added to their basket 
// and also adds custom classes as an alert
var confirm = document.getElementsByClassName("add_confirm");

var alertAdd = function() {
    document.getElementById("confirmAlertMessage").innerHTML = "Added to basket";
    $(".productCount").addClass("confirm_alert")
    $("#shopping_bag").addClass("shopping_bag_alert")

};

for (var i = 0; i < confirm.length; i++) {
    confirm[i].addEventListener('click', alertAdd, false);
}
