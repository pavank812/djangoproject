$(document).ready(function(){
	$('#login_form').validate({
		
		rules: {
			id_login: {
				required: true,
				email: true
			},
			id_password: {
				required:true,
				minlength:6
			}	
		},
		
		highlight: function(label) {
            $(label).closest('.control-group').addClass('error');     
		},
        
        success: function(label) {
            label.closest('.control-group').addClass('success');
            label.remove();
        }, 
        
        invalidHandler: function(){
            return false;
        },
        
        submitHandler: function(){
        	doLogin();
            return false;
        }
	});
});