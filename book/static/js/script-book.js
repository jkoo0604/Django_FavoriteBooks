// // New Post
// $(".newpostform").submit(function(e) {
//     e.preventDefault();

//     $.ajax({
//         type: 'POST',
//         url: "/wall/post",
//         data: $(this).serialize(),
//         success: function (response) {
//             // console.log(response);
//             $('.posts').html(response);
//         },
//         error: function(response) {
//             console.log(response);
//         }
//     })
//     $(this).trigger('reset');
//     $('.btn').blur();

// });

// // New Comment

// $(".posts").on('submit', '.newcommentform', function(e) {
//     e.preventDefault();
//     $.ajax({
//         type: 'POST',
//         url: "/wall/comment",
//         data: $(this).serialize(),
//         success: function (response) {
//             // console.log(response);
//             $('.posts').html(response);
//         },
//         error: function(response) {
//             console.log(response);
//         }
//     })
//     $(this).trigger('reset');
//     $('.btn').blur();
// });

// // Delete Comment
// $(".posts").on('click', '.deletecommenta', function(e) {
//     e.preventDefault();
//     url = $(this).attr('href')
//     console.log(url);
//     url = url.substring(20);
//     console.log(url);
//     var message_date = new Date($(this).attr('data-timestamp')).getTime()-(1000*60*420);
//     var current_date = new Date().getTime();
//     var diff = (current_date - message_date) / 1000;
//     diff /= 60;
//     console.log(message_date);
//     console.log($(this).attr('data-timestamp'));
//     console.log(current_date);
//     console.log(diff);

//     if (diff <= 30) {
//         $.ajax({
//             type: 'GET',
//             url: "/wall/deletecomment/" + url,
//             data: $(this).serialize(),
//             success: function (response) {
//                 // console.log(response);
//                 $('.posts').html(response);
                
//             },
//             error: function(response) {
//                 console.log(response);
//             }
//         })
//     } else {
//         $(this).append("<span id='nodelete'>Comments older than 30 minutes cannot be deleted</span>");
//         $('#nodelete').fadeOut(3000);
//         setTimeout(function() {

//             $('#nodelete').remove();
//         }, 3000);
//     }

    
//     $(this).trigger('reset')
//     $('.btn').blur();

// });

// // Delete Message
// $(".posts").on('click', '.deleteposta', function(e) {
//     e.preventDefault();
//     url = $(this).attr('href')
//     console.log(url);
//     url = url.substring(20);
//     console.log(url);
//     var message_date = new Date($(this).attr('data-timestamp')).getTime()-(1000*60*420);
//     var current_date = new Date().getTime();
//     var diff = (current_date - message_date) / 1000;
//     diff /= 60;
//     console.log(message_date);
//     console.log($(this).attr('data-timestamp'));
//     console.log(current_date);
//     console.log(diff);

//     if (diff <= 30) {

//         $.ajax({
//             type: 'GET',
//             url: "/wall/deletepost/" + url,
//             data: $(this).serialize(),
//             success: function (response) {
//                 // console.log(response);
//                 $('.posts').html(response);
                
//             },
//             error: function(response) {
//                 console.log(response);
//             }
//         })
//     } else {
//         $(this).append("<span id='nodelete'>Messages older than 30 minutes cannot be deleted</span>");
//         $('#nodelete').fadeOut(3000);
//         setTimeout(function() {

//             $('#nodelete').remove();
//         }, 3000);
//     }
//     $(this).trigger('reset')
//     $('.btn').blur();

// });


// // Create Post
// //  Create post and reload the list
// //  return the partial html page, $(.post).html = response


// // Create Comment
// //  Create comment and reload the list
// //  return the partial html page, $(.post).html = response


// // Delete Post
// //  If created_at > 30 min then display a message
// //  Make the message disappear after a few seconds
// //  If not, delete the post (and any comments) and reload the list
// //  return the partial html page, $(.post).html = response


// // Delete Comment
// //  If created_at > 30 min then display a message
// //  Make the message disappear after a few seconds
// //  If not, delete the comment and reload the list
// //  return the partial html page, $(.post).html =response