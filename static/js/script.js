$(document).ready(function() {

    $("button.login_to_like").click(function(){
        alert("Login to like");
    });

    $("button.empty_quantity_alert").click(function() {
        alert("Please add a quantity");
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
