// $(".ajaxform-reg").submit(function(e) {
//     e.preventDefault();
//     var form = $(this);
//     var first_name = $("#first_name").val();
//     var last_name = $("#last_name").val();
//     var email = $("#email").val();
//     var birth_date = $("#birth_date").val();
//     var current_date = new Date();
//     var password = $("#password").val();
//     var confirmpw = $("#confirmpw").val();
//     var output = 0;

//     $('.errfirst_name').html('');
//     $('.errlast_name').html('');
//     $('.erremail').html('');
//     $('.errbirth_date').html('');
//     $('.errpassword').html('');
//     $('.errconfirmpw').html('');
//     $('.loginfail').html('');


//     if (first_name.length < 2) {
//         output +=1;
//         $('.errfirst_name').html('<p>First name must be at least 2 characters long2</p>');
//         console.log(1);
//     }
//     if (last_name.length < 3) {
//         output +=1;
//         $('.errlast_name').html('<p>Last name must be at least 2 characters long2</p>');
//         console.log(2);
//     }

//     if (!emailregex(email)) {
//         output +=1;
//         $('.erremail').html('<p>Please enter a valid email address2</p>');
//         console.log(3);
//     } 

//     $.ajax({
//         type: 'GET',
//         url: "/ajax/validate-reg",
//         data: {"email": email},
//         success: function (response) {
//             if (response["used"]) {
//                 output +=1;
//                 $('.erremail').html('<p>An account already exists for this email2</p>');
//                 console.log(4);
//             }
//             if (!passwordregex(password)) {
//                 output +=1;
//                 $('.errpassword').html('<p>Password must be between 8-20 characters long and must contain at least one number2</p>');
//                 console.log(5);
//             }
            
//             if (password != confirmpw) {
//                 output +=1;
//                 $('.errconfirmpw').html('<p>Passwords do not match. Please confirm password again2</p>');
//                 console.log(6);
//             }
        
//             if (birth_date == '') {
//                 output +=1;
//                 $('.errbirth_date').html('<p>Please enter date of birth2</p>');
//                 console.log(7);
//             }
//             else {
//                 birth_date = new Date(birth_date);
//                 var target_date = new Date(birth_date.getFullYear()+13, birth_date.getMonth(), birth_date.getDate());
//                 console.log(target_date);
//                 if (birth_date.getTime() > current_date.getTime()) {
//                     output +=1;
//                     $('.errbirth_date').html('<p>Date of birth must be in the past2</p>');
//                     console.log(7-2);
//                 } else if (target_date.getTime() > current_date.getTime()) {
//                     output +=1;
//                     $('.errbirth_date').html('<p>You must be at least 13 years old to register2</p>');
//                     console.log(7-3);
//                 }
//             }
        
//             if (output > 0) {
//                 console.log(8);
//                 return false;
//             } else {
//                 form.unbind('submit').submit();
//             } 
//         },
//         error: function(response) {
//             console.log(response);
//             if (!passwordregex(password)) {
//                 output +=1;
//                 $('.errpassword').html('<p>Password must be between 8-20 characters long and must contain at least one number2</p>');
//                 console.log(5);
//             }
            
//             if (password != confirmpw) {
//                 output +=1;
//                 $('.errconfirmpw').html('<p>Passwords do not match. Please confirm password again2</p>');
//                 console.log(6);
//             }
        
//             if (birth_date == '') {
//                 output +=1;
//                 $('.errbirth_date').html('<p>Please enter date of birth2</p>');
//                 console.log(7);
//             }
//             else {
//                 birth_date = new Date(birth_date);
//                 var target_date = new Date(birth_date.getFullYear()+13, birth_date.getMonth(), birth_date.getDate());
//                 if (birth_date.getTime() > current_date.getTime()) {
//                     output +=1;
//                     $('.errbirth_date').html('<p>Date of birth must be in the past2</p>');
//                     console.log(7-2);
//                 } else if (target_date.getTime() > current_date.getTime()) {
//                     output +=1;
//                     $('.errbirth_date').html('<p>You must be at least 13 years old to register2</p>');
//                     console.log(7-3);
//                 }
//             }
        
//             if (output > 0) {
//                 console.log(8);
//                 return false;
//             } else {
//                 form.unbind('submit').submit();
//             } 
//         }
//     })
// });

// $(".ajaxform-login").submit(function(e) {
//     e.preventDefault();
//     var form = $(this);

//     $('.errfirst_name').html('');
//     $('.errlast_name').html('');
//     $('.erremail').html('');
//     $('.errbirth_date').html('');
//     $('.errpassword').html('');
//     $('.errconfirmpw').html('');
//     $('.loginfail').html('');

//     $.ajax({
//         type: 'POST',
//         url: "/ajax/validate-login",
//         data: $(this).serialize(),
//         success: function (response) {
//             if (!response["match"]) {
//                 $('.loginfail').html('<p>Incorrect email or password2</p>');
//                 return false
//             } 
//             else {
//                 form.unbind('submit').submit();
//             }
//         },
//         error: function(response) {
//             console.log(response);
//         }
//     })

// });

// function emailregex(email) {
//     var re= /^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$/;
//     return re.test(email);
// }

// function passwordregex(password) {
//     var re2= /^(?=.*\d)[a-zA-Z\d]{8,20}$/;
//     return re2.test(password);
// }