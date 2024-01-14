$(document).ready(function() {
    $("#addContentForm").submit(function(event) {
        event.preventDefault();  // Prevent default form submission

        var formData = new FormData(this);
        $.ajax({
            url: "addContent.php",
            type: "POST",
            data: formData,
            contentType: false,
            processData: false,
            success: function(response) {
                // Handle response from server (e.g., display success message, clear form)
                console.log(response);
                $("#addContentForm").trigger("reset");  // Clear the form
            },
            error: function(jqXHR, textStatus, errorThrown) {
                // Handle errors (e.g., display error message)
                console.error(textStatus + ": " + errorThrown);
            }
        });
    });
});