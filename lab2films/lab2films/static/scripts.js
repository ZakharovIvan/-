$(document).ready(function () {

	$('input[name=birth_year]').mask('9999');
	$('input[name=creation_year]').mask('9999');
	$('input[name=year]').mask('9999');
	$('input[name=duration]').mask('99:99:99');

	// $('#add-actor').validate({
	// 	rules: { name: 'required', surname: 'required', country: 'required' }
	// });

	// $('#add-studio').validate({
	// 	rules: { name: 'required' }
	// });

	// $('#add-album').validate({
	// 	rules: { album: 'required', style: 'required', year: 'required', artist: 'required', studio: 'required' }
	// });

	// $('#add-track').validate({
	// 	rules: { track: 'required', album: 'required', style: 'required', date_record: 'required',
	// 			 duration: 'required', artist: 'required', studio: 'required' }
	// });

	$('.add-actor').click(function (e) {
		e.preventDefault();
		// if (!$('#add-actor').valid())
		// 	return false;
		sendAjax('/actors/add', $('#add-actor').serialize(), function (answer) {
			setResultOfOperation(answer, 'http://localhost:8000/actors/get', 'actor was not added')});
	});

	$('.add-studio').click(function (e) {
		e.preventDefault();
		// if (!$('#add-studio').valid())
		// 	return false;
		sendAjax('/studios/add', $('#add-studio').serialize(), function (answer) {
			setResultOfOperation(answer, 'http://localhost:8000/studios/get', 'studio was not added')});
	});

	$('.add-director').click(function (e) {
		e.preventDefault();
		// if (!$('#add-director').valid())
		// 	return false;
		sendAjax('/directors/add', $('#add-director').serialize(), function (answer) {
			setResultOfOperation(answer, 'http://localhost:8000/directors/get', 'director was not added')});
	});

	$('.add-film').click(function (e) {
		e.preventDefault();
		// if (!$('#add-track').valid())
		// 	return false;
		sendAjax('/films/add', $('#add-film').serialize(), function (answer) {
			setResultOfOperation(answer, 'http://localhost:8000/films/get', 'film was not added')});
	});

	$('.add-films-actor').click(function (e) {
		e.preventDefault();
		$('#' + $(this).parent().parent().attr('class') + '-add-films-actor-form').parent().parent().show();
	});

	$('a[href$=fill-db-from-json]').click(function (e) {
		e.preventDefault();
		sendAjax('/fill-db-from-json', '', function (answer) {
			setResultOfOperation(answer, 'http://localhost:8000/actors/get', 'data was not added')});
	});

	$('.update-actor').click(function (e) {
		e.preventDefault();
		addUpdateForm({ form: $('#upd-actor'), id: $(this).parent().parent().attr('class')}, function ($id, $form) {
			$form.children('.name').val($('.' + $id).children('.name').text());
			$form.children('.country').val($('.' + $id).children('.country').text());
			$form.children('.ganre').val($('.' + $id).children('.ganre').text());
		});
	});

	$('.upd-actor').click(function (e) {
		e.preventDefault();
		sendAjax('/actors/upd', $('#upd-actor').serialize(), function (answer) {
			setResultOfOperation(answer, 'http://localhost:8000/actors/get', 'actor was not updated')});
	});

	$('.update-director').click(function (e) {
		e.preventDefault();
		addUpdateForm({ form: $('#upd-director'), id: $(this).parent().parent().attr('class')}, function ($id, $form) {
			$form.children('.name').val($('.' + $id).children('.name').text());
			$form.children('.country').val($('.' + $id).children('.country').text());
			$form.children('.ganre').val($('.' + $id).children('.ganre').text());
		});
	});

	$('.upd-director').click(function (e) {
		e.preventDefault();
		sendAjax('/directors/upd', $('#upd-director').serialize(), function (answer) {
			setResultOfOperation(answer, 'http://localhost:8000/directors/get', 'director was not updated')});
	});

	$('.update-studio').click(function (e) {
		e.preventDefault();
		addUpdateForm({ form: $('#upd-studio'), id: $(this).parent().parent().attr('class')}, function ($id, $form) {
			$form.children('.name').val($('.' + $id).children('.name').text());
			$form.children('.country').val($('.' + $id).children('.country').text());
		});
	});

	$('.upd-studio').click(function (e) {
		e.preventDefault();
		sendAjax('/studios/upd', $('#upd-studio').serialize(), function (answer) {
			setResultOfOperation(answer, 'http://localhost:8000/studios/get', 'studio was not updated')});
	});

});

function setResultOfOperation(res, link, message) {
	if (res == 1)
		$(location).attr("href", link);
	else
		alert(message);
}

function sendAjax(link, data, callback) {
	$.ajax({ url: link, type: 'get', data: data, success: callback });
}

function addUpdateForm(params, callback) {
	params.form.children('.id').remove();
	params.form.append('<input class="id" name="id" type="hidden" value="' + params.id + '" />');
	callback(params.id, params.form);
	params.form.show();
}

function addActorToFilm($form) {
	// if (!$('#add-track').valid())
	// 	return false;
	sendAjax('/film/add/actor', $('#' + $form + '-form').serialize(), function (answer) {
		setResultOfOperation(answer, 'http://localhost:8000/films/get', 'actor was not added to film')});
	return false;
}