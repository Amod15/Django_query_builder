
        $('#query-button').on('click', function(event) {
            event.preventDefault(); // Prevent the form from submitting the default way
            const formData = $('form').serialize();
            debugger;
            $.ajax({
                url: '/catalyst_count/query_data/',
                type: 'POST',
                data: formData, // Serialize the form data
                headers: {
                    'X-CSRFToken': getCookie('csrftoken') // CSRF token for security
                },
                success: function(response) {
                    console.log('Success:', response);
                    $('#results').html(`
                       <div style="background-color: #d4edda; color: #155724; padding: 10px; border-radius: 5px; position: relative;">
                            <button type="button" style="background: none; border: none; color: #155724; position: absolute; top: 5px; right: 10px; font-size: 20px; cursor: pointer;" id="close-btn">&times;</button>
                            <p>Number of matching records: ${response.count}</p>
                       </div>
                    `);

                $('#close-btn').on('click', function() {
                    $('#results').empty();
                });
                },
                error: function(xhr, status, error) {
                    console.error('Error:', error);
                }
            });
        });

        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }



    $('#upload-data-link').on('click', function(event) {
      event.preventDefault(); // Prevent the default link action

      $.ajax({
        url: '/catalyst_count/upload_file_template/', // Replace with the URL to fetch the HTML template
        method: 'GET',
        success: function(response) {
          // Place the response HTML into the container
          $('.container.mt-4').html(response);
          $('#upload-form').on('submit', function(e) {
                e.preventDefault(); // Prevent the form from submitting normally

                var formData = new FormData(this); // Create a FormData object
                var csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

                $.ajax({
                    url: '/catalyst_count/upload_csv/', // Your upload URL
                    type: 'POST',
                    data: formData,
                    processData: false,
                    contentType: false,
                    headers: {
                        'X-CSRFToken': csrfToken // Set the CSRF token header
                    },
                    xhr: function() {
                        var xhr = new window.XMLHttpRequest();
                        // Upload progress event
                        xhr.upload.addEventListener('progress', function(evt) {
                            if (evt.lengthComputable) {
                                var percentComplete = Math.round((evt.loaded / evt.total) * 100);
                                $('#progress-bar-fill').css('width', percentComplete + '%').text(percentComplete + '%');
                            }
                        }, false);
                        return xhr;
                    },
                    success: function(response) {
                        if (response.status === 'success') {
                            $('#status').css('color', 'green').text('File uploaded successfully.'); // Success message in green
                        } else {
                            $('#status').css('color', 'red').text('File upload failed.'); // Handle failure
                        }
                    },
                    error: function(xhr, status, error) {
                        $('#status').text('File upload failed: ' + error);
                    }
                });
            });
        },
        error: function(xhr, status, error) {
          console.error('AJAX error:', status, error);
          // Optionally handle errors here
        }
      });
    });

