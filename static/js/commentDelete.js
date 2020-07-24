$(document).ready(function () {
  $('#comment-content').on('click', 'button[id^=delete-comment-]', function (e) {
    e.preventDefault();
    const comment_id = $(this).attr('id').split('-')[2];
    console.log(`Delete button clicked with id#${comment_id}`);
    $.ajax({
      type: 'DELETE',
      // url: "{% url 'issues:detail' pk=issue.pk%}",
      url: comment_url,
      beforeSend: function (xhr) {
        xhr.setRequestHeader("X-CSRFToken", getCookie("csrftoken"));
      },
      data: {
        comment_pk: comment_id
      },
      success: function (json) {
        // hide the post
        console.log("Inside delete success");
        $('#comment-' + comment_id).hide(); // hide the post on success
        console.log("post deletion successful");
      },
      error: function (response) {
        // console.log(response);
        alert(response.statusText); // the message
      }
    })
  });
});

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie != '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) == (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}