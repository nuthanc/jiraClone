$('#comment-form').submit(function (e) {
  e.preventDefault();
  $.ajax({
    type: 'POST',
    // url: "{% url 'issues:detail' pk=issue.pk%}",
    url: comment_url,
    data: {
      content: $('#content').val(),
      csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val(),
    },
    success: onCommentSuccess,
    error: function (response) {
      alert(response['error']);
    },
  });
});

function onCommentSuccess(response) {
  console.log(response);
  var user = JSON.parse(response['user']);
  // console.log(user);
  var fields = user[0]['fields'];
  $('#comment-form').trigger('reset');
  // Display content, username and created
  $('#comment-content').append(
    `<div id="comment-${response.id}">
      ${fields['username'] || ''}
      <span class="float-right">
      ${response.created || ''}
      </span>

      <div class="card">
        <div class="card-body">
          ${response.content || ''}
        </div>
      </div>
      <div class="mt-1 mb-4">
        <button class="btn btn-danger" id="delete-comment-${response.id}">Delete</button>
      </div>
    </div>`
  );
}