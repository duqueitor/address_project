$(document).ready(function(){
	$('#submit').click(function(){

		name = $("#firstname").val()
		lastname = $("#lastname").val()
		email = $("#email").val()
		address = $("#address").val()
		phone = $("#phone").val()

		route = $('#route').val()
		locality = $('#locality').val()
		comunity = $('#comunity').val()
		comunity = $('#country').val()
		comunity = $('#postal_code').val()

		$( "#target" ).submit();
	});

	$('#search').click(function(){
		$( "#target" ).submit();
	});
});