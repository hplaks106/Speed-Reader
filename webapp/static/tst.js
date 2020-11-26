(function displayClass(i) {
    $("#tst").html(classes[i]);
    setTimeout(function() {
        displayClass((i + 1) % classes.length);
    }, 500);
})(0);
