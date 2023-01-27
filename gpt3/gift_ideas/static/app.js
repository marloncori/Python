$(document).ready(function() {
  // Hide the download button
  $("#download-button").hide();

  // Select the loading overlay elemen
  var loadingOverlay = $("#loading-overlay");

  // When the generate button is clicked
  $("#generate-button").click(function() {
    // Get the input data
    loadingOverlay.removeClass("hidden");
    $('#loading-overlay').removeClass('hidden');
    $(this).attr("disabled", true);

    var input_data = {
      "name": $("#name").val(),
      "age": $("#age").val(),
      "gender": $("input[name=gender]:checked").val(),
      "marital_status": $("#marital_status").val(),
      "has_children": $("input[name=has_children]:checked").val(),
      "profession": $("#profession").val(),
      "area_of_interest": $("#area_of_interest").val()
    };

    // Show the loading overlay and disable the button
    loadingOverlay.removeClass("hidden");
    $(this).attr("disabled", true);

    // Send the input data to the Flask app, this is more powerful than $.post()
    $.ajax({
      url: "/generate_gift_ideas",
      type: "POST",
      contentType: "application/json",
      data: JSON.stringify(input_data),
      success: function(response) {
    
         // Hide the loading overlay and re-enable the button
         loadingOverlay.addClass("hidden");
         // Redirect to the results page
         sessionStorage.setItem("gift_ideas", JSON.stringify(response));
         window.location = "/results";
      },
      error: function(error) {
        console.log(error);
      }
    });
  });

    if (document.body.id === "results") {
       // Show the download button
       $("#download-button").show();

       $("#download-button").click(function() {
        // Get the gift ideas
        var gift_ideas = $("ol").child().map(function() {
              return $(this).text();
        }).get();
   
        $.post("/download", { gift_ideas: gift_ideas }, function(response) {
         // Redirect to the home page
         window.location = "/home";
       });
     });
   
    } else {
      // Hide the download button
      $("#download-button").hide();
    }
      // When the download button is clicked  
});
